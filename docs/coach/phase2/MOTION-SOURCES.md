# Sources étudiées — aucune nouvelle mocap importée

Vérifications effectuées le 27 novembre 2026 dans les dépôts officiels via l’API GitHub. Aucune dépense, aucun crédit, aucun fichier d’origine incertaine intégré.

| Solution | Droits constatés | Utilité / limite | Décision |
|---|---|---|---|
| Microsoft Rocketbox | MIT, notice incluse dans PARISFIT ; README officiel annonce également 417 animations généralistes | Rig directement compatible. La bibliothèque consultée ne fournit pas les huit démonstrations sportives ciblées prêtes à l’emploi. | Modèle conservé ; ne pas rebaptiser une animation généraliste en exercice sportif. |
| Microsoft MoCapAct | README officiel : code MIT, dataset **CDLA-Permissive-2.0** | Jeux de trajectoires et politiques d’humanoïde simulé à partir de clips CMU ; pas un pack GLB sportif avec doigts. Les téléchargements sont désormais sur Hugging Face, hôte inaccessible dans cet environnement. Couverture exacte des huit exercices non vérifiée. Retargeting et revue resteraient nécessaires. | Piste ouverte et potentiellement commercialement compatible à instruire ; aucun dataset téléchargé ni droit étendu supposé sur un fichier non examiné. |
| Ubisoft LaFAN1 | `license.txt` : **CC BY-NC-ND 4.0** | Restrictions d’usage commercial et d’adaptation incompatibles avec l’intégration envisagée. | Exclu. |
| Mixamo | Aucun fichier ni licence de redistribution du matériau brut vérifié dans cette phase | Usage d’animations dans une application et redistribution des fichiers sources dans un dépôt sont deux questions différentes. | Aucun asset repris depuis un compte tiers ; pas de conclusion juridique inventée. |

## Références consultées
- https://github.com/microsoft/Microsoft-Rocketbox/blob/master/LICENSE.md
- https://github.com/microsoft/Microsoft-Rocketbox/blob/master/README.md
- https://github.com/microsoft/MoCapAct/blob/main/README.md — section « Licenses » et liens de téléchargement
- https://github.com/microsoft/MoCapAct/blob/main/LICENSE
- https://github.com/ubisoft/ubisoft-laforge-animation-dataset/blob/master/license.txt

## Alternative honnête réalisée

Les huit clips restent des animations **créées par cinématique inverse et interpolation**, avec correction d’appuis sur le maillage et tests de trajectoires. Ils ne sont pas de la motion capture et ne deviennent pas des références biomécaniques parce qu’ils passent des tests numériques.

## Étape professionnelle proposée, non effectuée

Faire filmer les huit démonstrations et les transferts debout/sol par un professionnel, avec consentement écrit et droits de redistribution commerciale. Faire ensuite réaliser le retargeting sur Rocketbox, les contacts et la revue des amplitudes. Une reconstruction de pose depuis une vidéo monoculaire ne garantit ni la profondeur, ni les doigts, ni des appuis exacts : cette étape nécessite encore du travail d’animation et une vérification qualifiée. Aucune commande payante n’a été passée.
