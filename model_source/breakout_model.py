"""Simplified assembly model derived from Adafruit's original Eagle PCB, CC BY-SA 3.0.
Board outline, hole positions and component centres follow the source. Component
bodies are approximate; this model is a placement aid, not a manufacturing model.
"""
from pathlib import Path
import math, xml.etree.ElementTree as ET
from OCP.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCP.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCP.gp import gp_Pnt, gp_Trsf, gp_Ax1, gp_Dir, gp_Vec
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_ColorGen
from OCP.TDataStd import TDataStd_Name
from OCP.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCP.STEPCAFControl import STEPCAFControl_Writer
from OCP.STEPControl import STEPControl_AsIs

P=Path(__file__).resolve().parents[1]
doc=TDocStd_Document(TCollection_ExtendedString('MDTV-XCAF'))
shapes=XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
colours=XCAFDoc_DocumentTool.ColorTool_s(doc.Main())
transform=gp_Trsf(); transform.SetRotation(gp_Ax1(gp_Pnt(0,0,0),gp_Dir(0,0,1)),-math.pi/2)
transform.SetTranslationPart(gp_Vec(-2.54,1.27,0))
def box(x,y,z,w,h,d): return BRepPrimAPI_MakeBox(gp_Pnt(x,y,z),w,h,d).Shape()
def cyl(x,y,z,r,h):
    shape=BRepPrimAPI_MakeCylinder(r,h).Shape(); t=gp_Trsf();t.SetTranslation(gp_Vec(x,y,z))
    return BRepBuilderAPI_Transform(shape,t,True).Shape()
def add(shape,name,rgb):
    shape=BRepBuilderAPI_Transform(shape,transform,True).Shape()
    label=shapes.AddShape(shape,False)
    TDataStd_Name.Set_s(label,TCollection_ExtendedString(name))
    colours.SetColor(label,Quantity_Color(*rgb,Quantity_TOC_RGB),XCAFDoc_ColorGen)
def cut(shape,tool): return BRepAlgoAPI_Cut(shape,tool).Shape()
def fuse(a,b): return BRepAlgoAPI_Fuse(a,b).Shape()
board=fuse(box(2.54,0,0,15.24,20.32,1.6),box(0,2.54,0,20.32,15.24,1.6))
for x in [2.54,17.78]:
    for y in [2.54,17.78]: board=fuse(board,cyl(x,y,0,2.54,1.6))
holes=[(2.54,17.78,1.25),(17.78,17.78,1.25)]
holes += [(1.27+2.54*i,2.54,.508) for i in range(8)]
holes += [(8.89+2.54*i,15.24,.508) for i in range(3)]
for x,y,r in holes: board=cut(board,cyl(x,y,-.1,r,1.8))
add(board,'Adafruit 2809 original PCB 20.32 mm',(.02,.19,.34))
for i,(x,y,r) in enumerate(holes):
    pad=cut(cyl(x,y,1.602,r+.36,.035),cyl(x,y,1.59,r,.1))
    add(pad,'Pad '+str(i+1),(.76,.58,.17))
root=ET.parse(P/'model_source/Adafruit_LIS3DH_Original.brd').getroot()
for e in root.findall('.//board/elements/element'):
    ref=e.get('name'); pkg=e.get('package'); x=float(e.get('x'));y=float(e.get('y'))
    angle=float(e.get('rot','R0').replace('R','').replace('M',''))
    if pkg.startswith('0805'): w,h,d=2,1.25,.7; rgb=(.30,.24,.16) if ref.startswith('C') else (.10,.10,.11)
    elif ref=='U1': w,h,d=3,3,1;rgb=(.12,.12,.13)
    elif pkg.startswith('SOT23'):w,h,d=2.9,1.6,1.1;rgb=(.12,.12,.13)
    elif pkg=='SOD-323':w,h,d=1.8,1.25,.8;rgb=(.12,.12,.13)
    else:continue
    body=box(x-w/2,y-h/2,1.65,w,h,d)
    rot=gp_Trsf();rot.SetRotation(gp_Ax1(gp_Pnt(x,y,0),gp_Dir(0,0,1)),math.radians(angle))
    add(BRepBuilderAPI_Transform(body,rot,True).Shape(),ref+' '+str(e.get('value')),rgb)
    if ref=='U1': add(cyl(x-1.05,y-1.05,2.66,.16,.02),'LIS3DH pin 1 mark',(.75,.75,.75))
writer=STEPCAFControl_Writer();writer.SetColorMode(True);writer.SetNameMode(True)
writer.Transfer(doc,STEPControl_AsIs)
out=P/'packages3D/Adafruit_LIS3DH_2809_Original.step'
assert int(writer.Write(str(out)))==1
print(out)
