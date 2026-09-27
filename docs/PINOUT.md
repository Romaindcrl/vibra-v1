# Brochage — Rev E-HS

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
