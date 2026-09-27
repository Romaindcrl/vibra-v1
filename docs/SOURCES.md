# Sources de la révision XIAO

- Seeed : https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/
- SKU du XIAO ESP32S3 : https://www.seeedstudio.com/XIAO-ESP32S3-p-5627.html
- Empreinte porteuse dérivée des positions DIP officielles, sans pastilles CMS : https://files.seeedstudio.com/wiki/XIAO-KiCad-Library/New_XIAO_Series_Footprints.zip
- Symboles officiels, utilisés pour vérifier le brochage à 14 broches : https://files.seeedstudio.com/wiki/XIAO-KiCad-Library/XIAO_Series_SCH_Symbols.zip
- Modèle STEP officiel : https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/res/seeed-studio-xiao-esp32s3-3d_model.zip
- Embases XIAO : https://www.we-online.com/components/products/datasheet/61300711821.pdf (7 broches, pas 2,54, entre première et dernière 15,24, hauteur 8,5, perçage recommandé 1,02 ±0,15)
- Broches mâles XIAO : https://www.we-online.com/components/products/datasheet/61300711121.pdf
- GPIO3 et JTAG : https://documentation.espressif.com/esp32-s3_datasheet_en.pdf
- Adafruit original et STEMMA QT : https://github.com/adafruit/Adafruit-LIS3DH-Breakout-PCB

Les modèles génériques des barrettes proviennent des bibliothèques KiCad installées ; leurs enveloppes sont indicatives. Les modèles et fichiers Seeed conservent leur provenance ; aucune revendication de création originale. Les fichiers téléchargés sont des données CAO, pas des instructions d'exécution.

- Registre WHO_AM_I 0x33 : https://raw.githubusercontent.com/adafruit/Adafruit_LIS3DH/master/Adafruit_LIS3DH.cpp

- Géométrie exacte du breakout ancien : `Adafruit LIS3DH Breakout Original.brd`, dépôt officiel Adafruit ci-dessus. Contour 20,32 × 20,32 mm, trous 2,5 mm à (2,54 ; 17,78) et (17,78 ; 17,78). Source incluse dans `model_source/`.
- Modèle 3D bleu : adaptation simplifiée créée pour cette révision à partir du PCB Adafruit. Contour, perçages et centres des composants issus du fichier Eagle ; volumes des composants approximatifs. Ce n'est pas un modèle STEP officiel Adafruit. Attribution et licence dans `licenses/Adafruit_model_NOTICE.md`.


## Vérification Rev E-HS — 27 septembre 2026

- C&K PTS526, fiche fabricant du 4 avril 2022, page 2 : contacts 1–2 et 3–4 reliés en interne ; fermeture entre les deux paires à l'appui. Implantation G-leads sans broche de masse, hauteur 1,5 mm. Pastilles fabricant 1,0 × 0,7 mm, entraxes 6,0 × 3,7 mm ; adaptation manuelle 1,2 × 0,8 mm étendue vers l'extérieur, intervalle intérieur 5,0 mm conservé. [Fiche C&K](https://www.ckswitches.com/media/2780/pts526.pdf), [copie fabricant consultée](https://4donline.ihs.com/images/VipMasterIC/IC/CKCI/CKCI-S-A0014471833/CKCI-S-A0014948334-1.pdf?hkey=6D3A4C79FDBF58556ACFDE234799DDF0).
- Documentation Seeed relue : brochage XIAO ESP32S3, sortie 3V3, USB-C et antenne U.FL. L'antenne fournie avec le XIAO n'est pas une antenne ajoutée à la carte porteuse.
- LED : symbole graphique standard KiCad `Device:LED`, adapté aux positions des broches existantes. Bibliothèques KiCad : https://www.kicad.org/libraries/license/ (CC-BY-SA 4.0 avec exception KiCad pour les conceptions).

Les contrôles de prix, de stock et de révision de la pièce effectivement achetée ne font pas partie des validations numériques.
