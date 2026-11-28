> Supplément Phase19 — 2026-11-27 (date de session). Référence immuable : `71bae7d1ed34227b2fc2c1c4e79aa7fdf1be22f1`. AB01 / Squat / 1 et Static / 1. Les phases17–18 ne sont ni remplacées ni réexécutées.

# Journaux et résultats originaux AB01

## Méthode et périmètre

Recherche ciblée dans l'arbre Git officiel fixé à `a26fe4852a78f30c5e8a437b158847031cb8dc3c` (8020 entrées, non tronqué), deux dossiers sélectionnés, noms AB01 contenant log/calib/quality/sync ; résultat exact dans [inventaire local](local-and-preserved-inventory.json). Puis lecture HTTP Range des répertoires centraux des archives publiques Figshare v1 **AB01.zip** (1589 entrées) et **MATLAB tools.zip** (853 entrées). [Résultats, tailles, CRC32, SHA256 et extraits numérotés](archive-probe.json). Aucun script original exécuté, aucune sortie régénérée. MD5 publié de l'archive complète non revérifié : seules les plages ciblées sont téléchargées.

## Preuves retrouvées — supplément aux absences dans Git

- `Static\1\Processing\opensim (1).log` : **21048 octets**, SHA256 `4edb4fcf69fffbeafbc49c510ad1cfae309f1b87b208d998ac3f541e7da7cdda`. Journal original publié, horodatages 2025-03-23 ; chemins AB01/Static/1 aux lignes53 et133. Moyenne de57 marqueurs/1565 frames, 0–7.82s. Aux lignes50/130 : RMS **0.0416775**, max **0.0737885 (LTH)**. Ce sont les valeurs du journal, pas un recalcul ; la sortie OpenSim est normalement en mètres, mais aucune transformation supplémentaire n'est appliquée ici. Plusieurs opérations et chemins Sit to stand figurent aussi dans ce fichier : ne pas attribuer son intégralité au squat. Pas de preuve que ces valeurs sont les statistiques GUI finales publiées.
- `Static\1\Processing\opensim.log` : **15965054 octets**, présence vérifiée dans l'index, lecture traitée séparément dans le probe et son supplément de résultats. Sa localisation ne suffit pas à attribuer toutes ses lignes à Static/1.
- `Squat/1/Results/squat_1_IKError.mat`, figures `squat_1_ik_err_markers.png` et `squat_1_ik_err_rms.png` : **présence vérifiée**, contenu non interprété. Résultats existants, pas journaux d'acquisition ; aucune erreur dynamique chiffrée inventée à partir du nom.
- `MoCapTools/+Osim/Scale.m` et `IK.m`, `trial_class.m`, licences/README EpicToolbox et MoCapTools : récupérés par plages, hashés, extraits conservés. Les bibliothèques ne sont donc pas globalement absentes du dépôt de données, même si absentes de l'arbre Git inspecté phase17. Leur provenance au niveau du membre est établie ; leur version exacte demeure inconnue.
- `one_leg_squat_shoe_lace_samples.mat` : l'[API officielle](https://api.figshare.com/v2/articles/28689221) référence le fichier57221192,268128 octets, MD5 `a5bf9fd2c4e9b0970f9ceafd8c110acb`. **Présence publique vérifiée, contenu non inspecté**, aucune borne de phase AB01 déduite.

## Ce qui n'est pas fermé

Aucun journal d'acquisition AB01, rapport individuel de calibration, relevé d'exclusion/reprise, journal des gaps et corrections marqueur par marqueur, ni configuration matérielle de synchronisation n'a été identifié dans le périmètre inspecté. Ce constat n'affirme pas leur inexistence mondiale. Raw TAK et Processed TAK sont annoncés par les auteurs ; leurs contenus n'ont pas été ouverts avec Motive ni utilisés pour refaire le traitement. Un journal OpenSim ne remplace pas ces preuves. Les paramètres génériques de laboratoire de l'article ne sont pas des logs AB01.

Les chemins de profils Windows sont masqués dans les extraits publiés ; SHA256 porte sur les octets originaux. Pas de photographie privée, contact auteur ou transmission externe à un expert.

## Résultat complémentaire — grand journal effectivement lu

Le run passif [46118632585](https://github.com/aydiarra-star/PARISFIT/actions/runs/46118632585), commit `77bb5fa`, a lu et contrôlé CRC32/SHA256 du membre `opensim.log` (207653 lignes), sans exécution. SHA256 : `3cb10df0990b5213c37ae24beead0665b1b551f40984c60277850cbad7c14ba6`. Total des plages des deux archives : **1876836 octets**, sous budget24Mo. Ce journal n'est donc plus simplement « localisé mais non lu ».

Les mentions ciblées sont conservées dans `archive-probe.json → targetMentions` : lignes13369 et13562, modèle sous **AB01/Squat/1** le2025-03-24 ; ligne13555, lecture de `squat_1_IKOut.mot`, **2948 lignes /43 colonnes**. Deuxième passage aux lignes58181,58367,58374. Cela documente des opérations originales sur l'essai sélectionné ; cela ne démontre pas que les sorties publiées sont exactement celles de ce passage (pas de hash de sortie dans le log). D'autres mentions relatives de squat_1 ont des tailles différentes : elles ne doivent pas être rattachées à AB01 uniquement par nom de fichier. Les extraits sont limités, pas une édition exhaustive du journal ; les versions du moteur exactes restent inconnues. La lecture de logs existants ne constitue pas une réexécution IK.
