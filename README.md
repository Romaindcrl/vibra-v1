# Vibra V1

Détecteur de vibrations **XIAO ESP32S3 + LIS3DH**. Carte de **48 × 38 mm**, 2 couches, prévue pour être soudée à la main. **Révision E-HS.**

<img src="rendu/apercu.png" width="640" alt="Vibra V1 assemblée, rendu 3D">

## Les fichiers utiles

| Pour… | Fichier |
|---|---|
| Ouvrir ou modifier le projet | [kicad/Vibra_V1.kicad_pro](kicad/Vibra_V1.kicad_pro) — KiCad 10.0.6 ou ultérieur |
| Lire le circuit | [Schéma PDF](rendu/schema.pdf) |
| Souder et vérifier l'implantation | [Plan de montage](rendu/montage.pdf) — page 1 agrandie, page 2 à taille réelle |
| Préparer les composants | [Liste des composants](rendu/composants.csv) |
| Faire fabriquer le PCB | [Gerbers et perçages](rendu/fabrication.zip) |

Télécharger **Code → Download ZIP**, extraire le dossier, puis ouvrir le projet. Garder le dossier `kicad/` entier : les empreintes sont intégrées au PCB, et les symboles et modèles 3D sont fournis. Toutes les instructions de montage sont ci-dessous.

**Avant fabrication : confirmer que le LIS3DH acheté est l'ancien Adafruit 2809 à une seule rangée de 8 broches. La version STEMMA QT est incompatible.** L'essai mécanique à blanc et la validation du premier prototype restent à faire. Aucun firmware de détection validé n'est fourni.

L'USB-C du XIAO alimente et programme la carte. La porteuse utilise le **3,3 V** ; le **5 V reste dans le XIAO**. Pistes de puissance et liaisons thermiques GND : **0,6 mm**. Cinq LED rouges, bouton CAL, UART sans alimentation, composants 0805 à grandes pastilles.

## Montage et mise en service

<details>
<summary><strong>Ouvrir le guide de montage</strong></summary>

### Avant de faire fabriquer

1. Vérifier le module LIS3DH : **ancien Adafruit 2809, carte carrée 20,32 mm, une seule rangée de 8 broches** dans cet ordre : VIN, 3Vo, GND, SCL, SDA, SDO, CS, INT. Le modèle STEMMA QT récent n'est pas compatible, même s'il porte aussi la référence commerciale 2809. Le capteur LIS3DH est déjà soudé sur ce module.
2. Vérifier que le XIAO est bien un ESP32S3 standard, avec deux rangées de 7 broches. Imprimer la **page 2 de [montage.pdf](rendu/montage.pdf)** à **100 %, taille réelle, sans ajustement**. Mesurer le contour : 48 × 38 mm. Faire un essai à blanc avec les modules, les barrettes et le câble USB. La page 1 agrandie ×4 est réservée à la lecture, pas à cet essai.
3. Prévoir les fixations du breakout. Il doit être rigidement lié à Vibra pour mesurer ses vibrations. H5/H6 sont deux trous de 2,5 mm, entraxe 15,24 mm. Employer de la visserie M2 et deux entretoises isolantes, diamètre extérieur ≤4 mm. Hauteur cible sous le breakout : **11,04 mm au-dessus de Vibra**, pour les barrettes choisies. Une entretoise de 11 mm peut convenir après contrôle et ajustement par rondelles fines ; ne pas plier le module en serrant. Pour deux entretoises tubulaires, prévoir deux vis M2 d'environ 16 mm, deux écrous et des rondelles isolantes ; vérifier la longueur réelle et l'absence de contact avec les composants. Ces éléments génériques figurent ici, pas sous un MPN arbitraire dans la BOM électronique.

### Pièces

La [liste unique des composants](rendu/composants.csv) donne les quantités, références fabricant et repères du plan. Les barrettes mâles ne sont nécessaires que si les modules n'en ont pas déjà. TP et H désignent des pastilles de test et des trous du PCB, sans composant à acheter.

Ajouter : le PCB, un câble USB-C **de données**, l'antenne fournie avec le XIAO branchée sur son U.FL, les fixations M2 ci-dessus et, pour fixer Vibra au support mesuré, quatre fixations M3 adaptées à ce support. Pas de batterie prévue par ce dossier. Pas de port USB-C, AZ1117, PTC ni antenne à souder sur Vibra.

### Alimentation et largeur des pistes

L'USB apporte le 5 V **au XIAO**. Son régulateur fournit le 3,3 V à Vibra par U1.12. U1.14 (5V/VBUS) reste volontairement non connecté : **aucune piste 5 V ne circule sur la carte porteuse**. Ne pas relier cette broche au 3,3 V. Ne pas alimenter la carte par J2 ou un point de test.

Toutes les pistes de puissance présentes, 3V3 et GND, sont à **0,60 mm**. La masse utilise aussi des plans sur les deux faces, avec liaisons thermiques de **0,60 mm** aux pastilles et largeur minimale de cuivre de **0,60 mm**. Une règle KiCad impose cette largeur minimale aux pistes GND/3V3 et réserve la même limite aux éventuels réseaux 5V/VBUS. Les traits verts du schéma représentent des connexions logiques ; leur épaisseur sur papier n'est pas la largeur du cuivre.

Si le professeur exige une piste 5 V physiquement présente sur la porteuse, cela constitue une autre architecture à valider : la présente version respecte le choix d'alimenter uniquement par le XIAO.

### Ordre de soudure

La **page 1 de [montage.pdf](rendu/montage.pdf)** indique tous les repères, avec l'USB vers le haut. Tout se pose sur la face supérieure ; les barrettes traversantes se soudent au dos. Ne jamais souder avec l'USB branché.

1. Trier les résistances et condensateurs, puis souder R4/R7/R8/R9–R13 et C5/C6/C8/C9/C10. Ils ne sont pas polarisés. Déposer un peu d'étain sur une pastille, positionner la pièce à la pince, la fixer puis souder l'autre côté avec du flux. Les pastilles 0805 dépassent du corps pour laisser passer la panne.
2. Souder D1–D5. **Cathode K = pastille 1 = GND, à gauche sur ce plan ; anode A = pastille 2, à droite.** Vérifier la polarité du composant au mode diode avant de le poser ; ne pas se fier uniquement à sa couleur. Les cinq LED ont le même sens.
3. Souder SW2/CAL : aligner les quatre pattes avec les quatre pastilles. Le composant relie déjà 1 à 2 et 3 à 4 en interne ; l'appui relie les deux paires. Ne pas le tourner de 90°. L'orientation à 180° conserve la fonction.
4. Souder J2 et les supports femelles U1/J3. Immobiliser les barrettes perpendiculaires à la carte ; souder d'abord une broche, vérifier l'alignement, puis les autres. Garder les modules débranchés pendant la chauffe ; un gabarit mécanique hors tension peut servir à aligner les deux supports U1.
5. Si nécessaire, souder les mâles sous les modules, extrémités courtes dans les cartes et longues vers les supports. Vérifier les joints, les ponts d'étain et nettoyer les résidus selon le flux utilisé.
6. Effectuer les contrôles hors tension ci-dessous. Enficher ensuite le XIAO, **USB vers l'extérieur du bord supérieur**. Enficher le LIS3DH composants vers le haut, **VIN dans J3.1, carré, côté bas marqué 1 VIN**. Aucune broche ne doit dépasser latéralement du support. Les 0805 sous le breakout doivent avoir été soudés avant cette étape.
7. Fixer le breakout à H5/H6 sans fléchir son PCB. Fixer Vibra au support à mesurer par ses quatre trous M3. Prévoir l'emplacement de l'antenne XIAO dans le boîtier, à l'écart du métal ; elle et les entretoises ne sont pas représentées en 3D.

La masse à 0,6 mm absorbe davantage de chaleur qu'une piste signal : chauffer ensemble la patte et la pastille, utiliser du flux et une panne adaptée. Les liaisons thermiques sont conservées pour faciliter cette opération ; ne pas compenser un mauvais contact par une chauffe prolongée du composant.

### Contrôles avant le premier branchement

Modules retirés et USB débranché : vérifier l'absence de pont entre 3V3 (TP3) et GND (TP4). Un bref bip dû à la charge des condensateurs n'est pas à lui seul un court-circuit ; une résistance très faible persistante exige de rechercher le défaut. Ne pas mesurer la résistance sur une carte alimentée.

Vérifier au multimètre : TP4 ↔ U1.13/J2.1/J3.3/J3.6 ; TP3 ↔ U1.12/J3.1/J3.7 ; CAL TP6 ↔ U1.3. CAL devient conducteur vers GND à l'appui. U1.14 et J3.2 doivent rester sans liaison aux autres réseaux. Vérifier l'orientation des LED au mode diode ; la méthode peut être perturbée par les chemins en parallèle après montage.

### Première mise sous tension et logiciel

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

CAL ne remplace pas BOOT. Le GPIO3 a aussi une fonction de sélection JTAG au démarrage selon les eFuses ; laisser CAL relâché lors du démarrage et voir le brochage ci-dessous. Le comportement réel du détecteur et sa calibration devront être vérifiés avec le firmware sur un prototype rigidement fixé.

### Fichiers de fabrication

Ouvrir [`kicad/Vibra_V1.kicad_pro`](kicad/Vibra_V1.kicad_pro) dans KiCad 10.0.6 ou ultérieur. Fabrication : FR-4 **1,6 mm**, **2 couches**, cuivre nominal **35 µm**, masque sur les deux faces. Les Gerbers et perçages sont réunis dans **[fabrication.zip](rendu/fabrication.zip)** ; ne pas mélanger les révisions.

Il s'agit d'un PCB à faire fabriquer puis à assembler à domicile. Les vias et trous métallisés requis ne sont pas adaptés à une simple gravure maison sans métallisation.

La vérification numérique est propre, mais elle ne remplace pas la confirmation du breakout acheté, l'essai mécanique à blanc et les mesures sur le premier exemplaire. Aucune commande n'a été passée.

</details>

<details>
<summary><strong>Brochage complet</strong></summary>

Vue de dessus, USB du XIAO vers le bord supérieur. Deux rangées de 7 broches au pas de 2,54 mm, espacées de 15,24 mm. Pastille carrée 1 = D0, en haut à gauche. Une seule alimentation : USB-C du XIAO. Sa broche 5V/VBUS reste isolée de la carte porteuse.

| U1 | Marquage XIAO | GPIO S3 | Fonction Vibra |
|---:|---|---:|---|
| 1 | D0 | 1 | LED1 |
| 2 | D1 | 2 | LED2 |
| 3 | D2 | 3 | CAL, actif à zéro, pull-up 10 kΩ |
| 4 | D3 | 4 | LED3 |
| 5 | D4 / SDA | 5 | I²C SDA |
| 6 | D5 / SCL | 6 | I²C SCL |
| 7 | D6 / TX | 43 | UART TX → J2.2 |
| 8 | D7 / RX | 44 | UART RX ← J2.3 |
| 9 | D8 | 7 | LED4 |
| 10 | D9 | 8 | LED5 |
| 11 | D10 | 9 | LIS3DH INT1 |
| 12 | 3V3 | — | Sortie régulée du XIAO vers Vibra |
| 13 | GND | — | Masse commune |
| 14 | 5V | — | Non connectée |

Les LED sont actives à l'état haut, chacune avec 680 Ω. Les numéros GPIO de l'ancien ESP32-C3 ne sont plus valables. Initialiser I²C sur SDA=5, SCL=6 et INT1 sur GPIO9. Ne pas confondre D10 (GPIO9) et GPIO10. CAL ne met pas le XIAO en mode téléchargement ; employer ses boutons BOOT et RESET pour cette fonction.

GPIO3 est aussi une broche de sélection JTAG au reset selon les eFuses. CAL peut donc affecter cette sélection si ces eFuses ont été configurés ; il ne remplace pas GPIO0/BOOT. Référence : [Espressif](https://documentation.espressif.com/esp32-s3_datasheet_en.pdf).

| J3 | Ancien breakout Adafruit 2809 | Connexion |
|---:|---|---|
| 1, carré, côté bas | VIN | +3V3 du XIAO |
| 2 | 3Vo | Non connectée |
| 3 | GND | GND |
| 4 | SCL | GPIO6 |
| 5 | SDA | GPIO5 |
| 6 | SDO | GND : adresse 0x18 |
| 7 | CS | +3V3 : mode I²C |
| 8, côté haut | INT | GPIO9 |

J2 : 1 GND, 2 TX, 3 RX. Relier TX de l'adaptateur au RX de Vibra et inversement. Adaptateur logique 3,3 V ; ne raccorder aucune sortie d'alimentation de l'adaptateur.

</details>

<details>
<summary><strong>Contrôles KiCad et modification du projet</strong></summary>

Contrôles dans KiCad 10.0.6 : **DRC : 0 erreur, 0 avertissement, 0 liaison non routée et 0 écart schéma/PCB. ERC : 0 erreur et 34 avertissements de liaison aux empreintes.** Ces avertissements viennent de la suppression de la bibliothèque d'empreintes séparée ; le contrôle reste actif. La revue de Rev E a aussi confirmé **71/71 associations broche–réseau**. Les fichiers détaillés de la revue restent accessibles dans l'historique Git ; le dossier de rendu ne contient que les fichiers utiles à la réalisation.

Les 34 empreintes complètes, dont les grandes pastilles de soudure manuelle, restent intégrées au fichier `.kicad_pcb`. Pour réutiliser une empreinte personnalisée sur un nouveau composant, l'exporter depuis le PCB vers une bibliothèque personnelle, puis l'assigner dans le schéma. La bibliothèque d'origine reste récupérable dans l'historique Git.

Cinq contrôles DRC hérités restent désactivés : centrage piste/via, géométrie des profils de tuning, filtres d'empreintes, PTH dans courtyard, NPTH dans courtyard. Quatre ERC restent désactivés : filtres d'empreintes, jonctions à quatre branches, modèle SPICE, label global unique. Aucune exclusion individuelle DRC. Les contrôles électriques, d'isolation, thermiques, de perçage, de routage et de parité sont actifs.

Après une modification : mettre le PCB à jour depuis le schéma, remplir et sauvegarder les zones, relancer ERC et DRC avec parité, puis régénérer les fichiers de fabrication. Les contrôles numériques ne remplacent pas les essais physiques.

</details>

<details>
<summary><strong>Sources et attributions</strong></summary>

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

- Géométrie exacte du breakout ancien : `Adafruit LIS3DH Breakout Original.brd`, dépôt officiel Adafruit ci-dessus. Contour 20,32 × 20,32 mm, trous 2,5 mm à (2,54 ; 17,78) et (17,78 ; 17,78). Source disponible dans le dépôt officiel Adafruit lié ci-dessus.
- Modèle 3D bleu : adaptation simplifiée créée pour cette révision à partir du PCB Adafruit. Contour, perçages et centres des composants issus du fichier Eagle ; volumes des composants approximatifs. Ce n'est pas un modèle STEP officiel Adafruit. Attribution et lien vers la licence ci-dessous.


## Vérification Rev E-HS — 27 septembre 2026

- C&K PTS526, fiche fabricant du 4 avril 2022, page 2 : contacts 1–2 et 3–4 reliés en interne ; fermeture entre les deux paires à l'appui. Implantation G-leads sans broche de masse, hauteur 1,5 mm. Pastilles fabricant 1,0 × 0,7 mm, entraxes 6,0 × 3,7 mm ; adaptation manuelle 1,2 × 0,8 mm étendue vers l'extérieur, intervalle intérieur 5,0 mm conservé. [Fiche C&K](https://www.ckswitches.com/media/2780/pts526.pdf), [copie fabricant consultée](https://4donline.ihs.com/images/VipMasterIC/IC/CKCI/CKCI-S-A0014471833/CKCI-S-A0014948334-1.pdf?hkey=6D3A4C79FDBF58556ACFDE234799DDF0).
- Documentation Seeed relue : brochage XIAO ESP32S3, sortie 3V3, USB-C et antenne U.FL. L'antenne fournie avec le XIAO n'est pas une antenne ajoutée à la carte porteuse.
- LED : symbole graphique standard KiCad `Device:LED`, adapté aux positions des broches existantes. Bibliothèques KiCad : https://www.kicad.org/libraries/license/ (CC-BY-SA 4.0 avec exception KiCad pour les conceptions).

Les contrôles de prix, de stock et de révision de la pièce effectivement achetée ne font pas partie des validations numériques.

### Modèle Adafruit

PCB original conçu par Limor Fried/Ladyada pour Adafruit Industries :
https://github.com/adafruit/Adafruit-LIS3DH-Breakout-PCB

Le modèle `Adafruit_LIS3DH_2809_Original.step` est une adaptation réalisée pour Vibra Rev D le 25 septembre 2026. Il reprend le contour, les perçages et les positions de composants du PCB original ; les volumes des composants et couleurs sont simplifiés. Il n'inclut pas la sérigraphie officielle. Il est distribué sous la même licence Creative Commons Attribution-ShareAlike 3.0, accessible ci-dessous. Adafruit n'a pas validé cette adaptation.

Le fichier Eagle original et ses révisions sont disponibles dans le dépôt officiel Adafruit lié ci-dessus. Les autres modèles conservent leurs provenances Seeed et KiCad détaillées ici.

[Licence CC BY-SA 3.0 du modèle Adafruit](https://creativecommons.org/licenses/by-sa/3.0/legalcode). Les éléments tiers conservent leurs licences respectives. Aucune licence globale supplémentaire n'est accordée par ce dépôt.

</details>
