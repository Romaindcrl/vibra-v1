# Revue Rev E-HS — 27 septembre 2026

Projet existant corrigé pour une transmission et un montage manuel. PCB compact 48 × 38 mm, schéma réorganisé en A4 ; pas de reconstruction du circuit. Les 32 empreintes reprises conservent leurs UUID ; H5/H6 sont les deux ajouts mécaniques de la révision compacte.

## Corrections de cette révision

- Schéma lisible sur une page, sans débordement dans le cartouche ; symboles LED et bouton explicites, liaisons résistances/LED dessinées, alimentation et brochage documentés.
- Pistes 3V3 déjà à 0,6 mm conservées. Plans GND F.Cu/B.Cu : thermiques passées de 0,3 à **0,6 mm**, largeur minimale du cuivre **0,6 mm**. Surcharge locale de J3.6 passée de 0,2 à **0,6 mm**.
- Une courte piste GND de 0,6 mm ajoutée au dos depuis J3.6 pour corriger une connexion thermique insuffisante après élargissement. Contrôle thermique maintenu actif.
- Netclasse de puissance complétée pour GND et règles minimales explicites dans `Vibra_V1.kicad_dru`. Aucun réseau 5V sur la porteuse : U1.14 isolé, alimentation par le 3V3 du XIAO.
- PTS526 vérifié contre la fiche C&K : paires 1–2/3–4 correctes. Pastilles augmentées de 1,0 × 0,7 à **1,2 × 0,8 mm**, côté extérieur ; largeur libre intérieure de 5,0 mm conservée. Bibliothèque locale synchronisée.
- Guide de montage et de mise en service, liste d'achat regroupée, plan d'assemblage 1:1 et agrandi ×4. BOM sans référence TBD ; trous et points de test identifiés comme éléments du PCB.

## Résultats dans KiCad 10.0.6

| Contrôle | Résultat |
|---|---:|
| ERC, erreurs / avertissements | 0 / 0 |
| DRC, erreurs / avertissements | 0 / 0 |
| Connexions non routées | 0 |
| Écarts schéma / PCB | 0 |
| Comparaison indépendante broche / réseau | 71 / 71 |
| Conformité au brochage fonctionnel attendu | 71 / 71 |
| Broches raccordées / volontairement NC | 69 / 2 |
| Empreintes / pastilles physiques | 34 / 77 |
| Segments / vias | 133 / 15 |
| Pistes 3V3 / GND | 0,60 mm / 0,60 mm |
| Thermiques GND, y compris surcharges locales | 0,60 mm |

Le projet Rev E a été ouvert dans l'application KiCad. Les zones ont été remplies et sauvegardées dans l'éditeur PCB. DRC natif avec remplissage et comparaison schéma : 0/0/0. ERC natif, erreurs/avertissements/exclusions affichés : 0. Vue PCB, schéma A4, rendu 3D et plans d'assemblage inspectés. Rapports CLI JSON/texte, audit des largeurs et correspondance indépendante joints dans `fabrication/rev_E/reports/`.

Routage de la révision compacte réalisé auparavant avec MCP KiCad + Freerouting 2.4.1 ; cette révision conserve ce routage avec une liaison GND supplémentaire. MCP disponible en backend SWIG, sans synchronisation automatique de l'éditeur. Le fichier PCB final et ses plans remplis font référence, pas les échanges d'autoroutage d'une ancienne révision.

## Règles et limites

Isolation de netclasse 0,20 mm ; minimum global 0,15 mm ; cuivre/bord 0,30 mm. Les pistes signal sont à 0,25 mm, avec trois courts rétrécissements hérités à 0,1874 mm ; la règle de 0,6 mm concerne l'alimentation et GND. Vias : perçage 0,30 mm. Support : 1,05 mm ; UART : 1,10 mm ; trous M3 : 3,20 mm NPTH ; supports LIS3DH : 2,50 mm NPTH.

Cinq contrôles DRC hérités restent désactivés : centrage piste/via, géométrie des profils de tuning, filtres d'empreintes, PTH dans courtyard, NPTH dans courtyard. Quatre ERC restent désactivés : filtres d'empreintes, jonctions à quatre branches, modèle SPICE, label global unique. **Aucune exclusion individuelle DRC**. Les contrôles électriques, d'isolation, thermiques, de perçage, de routage et de parité sont actifs. Ces paramètres sont visibles dans les rapports.

**Le dossier est prêt à être transmis pour assembler un prototype sous les conditions du guide ; le matériel n'est pas encore validé physiquement.** Il reste à confirmer la révision 1×8 du breakout acheté, à vérifier les connecteurs/entretoises/câble sur un montage à blanc, puis à tester alimentation, USB, LED, CAL, I²C, interruption et fixation du capteur sur le premier exemplaire. Aucun firmware de détection validé ni achat de composants/PCB inclus.

Le modèle du LIS3DH est une représentation simplifiée dérivée des données Adafruit ; antenne et visserie absentes du STEP. La présence des modèles 3D ne valide pas les tolérances des pièces achetées. Si le professeur impose explicitement une piste 5V sur la porteuse, la présente architecture 3V3 doit être discutée avec lui ; aucune piste 5V fictive n'a été ajoutée.
