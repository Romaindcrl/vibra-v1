# Monter Vibra V1 — Rev E-HS

**Carte porteuse de 48 × 38 mm, à assembler au fer.** Les deux circuits difficiles à souder sont déjà montés sur le XIAO et le breakout LIS3DH. Sur Vibra : composants 0805 à grandes pastilles, bouton PTS526 accessible et connecteurs traversants au pas de 2,54 mm. Les 0805 restent de petits CMS : une pince fine, du flux et une loupe sont utiles.

## Avant de faire fabriquer

1. Vérifier le module LIS3DH : **ancien Adafruit 2809, carte carrée 20,32 mm, une seule rangée de 8 broches** dans cet ordre : VIN, 3Vo, GND, SCL, SDA, SDO, CS, INT. Le modèle STEMMA QT récent n'est pas compatible, même s'il porte aussi la référence commerciale 2809. Le capteur LIS3DH est déjà soudé sur ce module.
2. Vérifier que le XIAO est bien un ESP32S3 standard, avec deux rangées de 7 broches. Imprimer `Vibra_V1_assembly.pdf` à **100 %, taille réelle, sans ajustement**. Mesurer le contour : 48 × 38 mm. Faire un essai à blanc avec les modules, les barrettes et le câble USB. Le PDF `_x4` est réservé à la lecture, pas à cet essai.
3. Prévoir les fixations du breakout. Il doit être rigidement lié à Vibra pour mesurer ses vibrations. H5/H6 sont deux trous de 2,5 mm, entraxe 15,24 mm. Employer de la visserie M2 et deux entretoises isolantes, diamètre extérieur ≤4 mm. Hauteur cible sous le breakout : **11,04 mm au-dessus de Vibra**, pour les barrettes choisies. Une entretoise de 11 mm peut convenir après contrôle et ajustement par rondelles fines ; ne pas plier le module en serrant. Pour deux entretoises tubulaires, prévoir deux vis M2 d'environ 16 mm, deux écrous et des rondelles isolantes ; vérifier la longueur réelle et l'absence de contact avec les composants. Ces éléments génériques figurent ici, pas sous un MPN arbitraire dans la BOM électronique.

## Pièces

La liste électronique regroupée est `fabrication/rev_E/LISTE_ACHAT.csv`. La BOM détaillée par repère est `Vibra_V1_BOM.csv`. Les lignes TP et H sont des pastilles/trous du PCB, pas des composants à acheter. Les barrettes mâles ne sont nécessaires que si les modules n'en ont pas déjà.

| Quantité | Pièce | Repères / référence |
|---:|---|---|
| 1 | Seeed XIAO ESP32S3 | U1 ; 113991114 ; module fourni par l'utilisateur |
| 1 | Adafruit LIS3DH ancien, 1×8 | 2809 original uniquement ; version à confirmer |
| 1 | Résistance 10 kΩ, 0805, 1 % | R4 ; RC0805FR-0710KL |
| 2 | Résistance 4,7 kΩ, 0805, 1 % | R7/R8 ; RC0805FR-074K7L |
| 5 | Résistance 680 Ω, 0805, 1 % | R9–R13 ; RC0805FR-07680RL |
| 2 | Condensateur céramique 10 µF, 16 V, 0805 | C5/C9 ; GRM21BR61C106KE15L |
| 3 | Condensateur céramique 100 nF, 16 V, 0805 | C6/C8/C10 ; GRM21BR71C104KA01L |
| 5 | LED rouge 0805 | D1–D5 ; LTST-C170KRKT |
| 1 | Bouton PTS526, hauteur 1,5 mm | SW2 ; PTS526 SK15 SMTR2 LFS |
| 2 | Embase femelle 1×7, hauteur 8,5 mm | Sous U1 ; 61300711821 |
| 2 | Barrette mâle 1×7 | Sous le XIAO ; 61300711121 |
| 1 | Embase femelle 1×8, hauteur 8,5 mm | J3 ; 61300811821 |
| 1 | Barrette mâle 1×8 | Sous le LIS3DH ; 61300811121 |
| 1 | Barrette mâle 1×3 | J2 UART ; 61300311121 |

Ajouter : le PCB, un câble USB-C **de données**, l'antenne fournie avec le XIAO branchée sur son U.FL, les fixations M2 ci-dessus et, pour fixer Vibra au support mesuré, quatre fixations M3 adaptées à ce support. Pas de batterie prévue par ce dossier. Pas de port USB-C, AZ1117, PTC ni antenne à souder sur Vibra.

## Alimentation et largeur des pistes

L'USB apporte le 5 V **au XIAO**. Son régulateur fournit le 3,3 V à Vibra par U1.12. U1.14 (5V/VBUS) reste volontairement non connecté : **aucune piste 5 V ne circule sur la carte porteuse**. Ne pas relier cette broche au 3,3 V. Ne pas alimenter la carte par J2 ou un point de test.

Toutes les pistes de puissance présentes, 3V3 et GND, sont à **0,60 mm**. La masse utilise aussi des plans sur les deux faces, avec liaisons thermiques de **0,60 mm** aux pastilles et largeur minimale de cuivre de **0,60 mm**. Une règle KiCad impose cette largeur minimale aux pistes GND/3V3 et réserve la même limite aux éventuels réseaux 5V/VBUS. Les traits verts du schéma représentent des connexions logiques ; leur épaisseur sur papier n'est pas la largeur du cuivre.

Si le professeur exige une piste 5 V physiquement présente sur la porteuse, cela constitue une autre architecture à valider : la présente version respecte le choix d'alimenter uniquement par le XIAO.

## Ordre de soudure

Le plan `Vibra_V1_assembly_x4.pdf` indique tous les repères, avec l'USB vers le haut. Tout se pose sur la face supérieure ; les barrettes traversantes se soudent au dos. Ne jamais souder avec l'USB branché.

1. Trier les résistances et condensateurs, puis souder R4/R7/R8/R9–R13 et C5/C6/C8/C9/C10. Ils ne sont pas polarisés. Déposer un peu d'étain sur une pastille, positionner la pièce à la pince, la fixer puis souder l'autre côté avec du flux. Les pastilles 0805 dépassent du corps pour laisser passer la panne.
2. Souder D1–D5. **Cathode K = pastille 1 = GND, à gauche sur ce plan ; anode A = pastille 2, à droite.** Vérifier la polarité du composant au mode diode avant de le poser ; ne pas se fier uniquement à sa couleur. Les cinq LED ont le même sens.
3. Souder SW2/CAL : aligner les quatre pattes avec les quatre pastilles. Le composant relie déjà 1 à 2 et 3 à 4 en interne ; l'appui relie les deux paires. Ne pas le tourner de 90°. L'orientation à 180° conserve la fonction.
4. Souder J2 et les supports femelles U1/J3. Immobiliser les barrettes perpendiculaires à la carte ; souder d'abord une broche, vérifier l'alignement, puis les autres. Garder les modules débranchés pendant la chauffe ; un gabarit mécanique hors tension peut servir à aligner les deux supports U1.
5. Si nécessaire, souder les mâles sous les modules, extrémités courtes dans les cartes et longues vers les supports. Vérifier les joints, les ponts d'étain et nettoyer les résidus selon le flux utilisé.
6. Effectuer les contrôles hors tension ci-dessous. Enficher ensuite le XIAO, **USB vers l'extérieur du bord supérieur**. Enficher le LIS3DH composants vers le haut, **VIN dans J3.1, carré, côté bas marqué 1 VIN**. Aucune broche ne doit dépasser latéralement du support. Les 0805 sous le breakout doivent avoir été soudés avant cette étape.
7. Fixer le breakout à H5/H6 sans fléchir son PCB. Fixer Vibra au support à mesurer par ses quatre trous M3. Prévoir l'emplacement de l'antenne XIAO dans le boîtier, à l'écart du métal ; elle et les entretoises ne sont pas représentées en 3D.

La masse à 0,6 mm absorbe davantage de chaleur qu'une piste signal : chauffer ensemble la patte et la pastille, utiliser du flux et une panne adaptée. Les liaisons thermiques sont conservées pour faciliter cette opération ; ne pas compenser un mauvais contact par une chauffe prolongée du composant.

## Contrôles avant le premier branchement

Modules retirés et USB débranché : vérifier l'absence de pont entre 3V3 (TP3) et GND (TP4). Un bref bip dû à la charge des condensateurs n'est pas à lui seul un court-circuit ; une résistance très faible persistante exige de rechercher le défaut. Ne pas mesurer la résistance sur une carte alimentée.

Vérifier au multimètre : TP4 ↔ U1.13/J2.1/J3.3/J3.6 ; TP3 ↔ U1.12/J3.1/J3.7 ; CAL TP6 ↔ U1.3. CAL devient conducteur vers GND à l'appui. U1.14 et J3.2 doivent rester sans liaison aux autres réseaux. Vérifier l'orientation des LED au mode diode ; la méthode peut être perturbée par les chemins en parallèle après montage.

## Première mise sous tension et logiciel

Brancher seulement l'USB du XIAO, avec les modules en place. Mesurer environ **3,3 V entre TP3 et TP4**. Si une pièce chauffe anormalement ou si la tension s'effondre, débrancher et inspecter le montage. Vérifier ensuite le 3,3 V au démarrage et lors des émissions Wi-Fi.

Le dossier est une conception matérielle : **aucun firmware de détection/calibration validé n'est fourni**. Pour la mise au point du logiciel :

| Fonction | Test attendu |
|---|---|
| USB | XIAO détecté et programmable ; utiliser ses boutons BOOT/RESET si nécessaire |
| I²C | SDA GPIO5, SCL GPIO6 ; commencer à 100 kHz ; LIS3DH détecté à 0x18 |
| Identité capteur | WHO_AM_I, registre 0x0F, retourne 0x33 |
| Interruption | INT1 relié à GPIO9 ; configurer l'interruption dans le LIS3DH avant le test |
| LED | GPIO1, 2, 4, 7, 8 ; état haut = allumée ; 680 Ω chacune, courant de l'ordre de 2 mA |
| CAL | GPIO3 ; haut au repos, bas à l'appui ; prévoir l'anti-rebond logiciel |
| UART facultatif | J2.1 GND, J2.2 TX(GPIO43), J2.3 RX(GPIO44) ; logique 3,3 V, TX/RX croisés, sans VCC |

CAL ne remplace pas BOOT. Le GPIO3 a aussi une fonction de sélection JTAG au démarrage selon les eFuses ; laisser CAL relâché lors du démarrage et voir `PINOUT.md`. Le comportement réel du détecteur et sa calibration devront être vérifiés avec le firmware sur un prototype rigidement fixé.

## Fichiers de fabrication

Ouvrir `Vibra_V1.kicad_pro` dans KiCad 10.0.6 ou ultérieur, avec les bibliothèques locales du dossier. Fabrication : FR-4 **1,6 mm**, **2 couches**, cuivre nominal **35 µm**, masque sur les deux faces. Toutes les sorties correspondantes sont dans `fabrication/rev_E/` ; ne pas mélanger les révisions.

Il s'agit d'un PCB à faire fabriquer puis à assembler à domicile. Les vias et trous métallisés requis ne sont pas adaptés à une simple gravure maison sans métallisation.

La vérification numérique est propre, mais elle ne remplace pas la confirmation du breakout acheté, l'essai mécanique à blanc et les mesures sur le premier exemplaire. Aucune commande n'a été passée.
