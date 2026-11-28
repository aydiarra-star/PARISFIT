> Supplément Phase19 — 2026-11-27 (date de session). Référence immuable : `71bae7d1ed34227b2fc2c1c4e79aa7fdf1be22f1`. AB01 / Squat / 1 et Static / 1. Les phases17–18 ne sont ni remplacées ni réexécutées.

# Inventaire des versions et environnements

Les versions **déclarées**, **mesurées maintenant** et **historiques** ne sont pas interchangeables. « inconnue » signifie que la preuve disponible ne permet pas une version exacte.

| Composant / périmètre | Version établie et preuve | Limite |
|---|---|---|
| Exportateur des deux C3D AB01 | `MANUFACTURER` : OptiTrack / Motive / **3.0.3 Final**, lecture métadonnées dans [inventaire](local-and-preserved-inventory.json), hashes identiques au manifest17 | Métadonnée d'export, pas journal de chaque correction |
| Traitement auteurs | MATLAB **2023b**, OpenSim **4.4**, article section Data Processing, [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12717423/), Readme officiel | Builds, OS complet, Java et patch MATLAB : **inconnue** ; déclaration de méthode non preuve d'une exécution précise |
| Lecteur C3D Parisfit | Python `c3d==0.6.0`, CI et environnement local ; [analyse historique du lecteur](../phase18/python-c3d-reader-evidence.txt) | Distinct du lecteur des auteurs ; anomalie de dernier index documentée phase18, pas perte physique démontrée |
| Lecteur indépendant | `tools/independent-review/audit.py` à la référence, lecture Intel/float restreinte | Pas une bibliothèque générale certifiée ; pas relancé pour refaire l'audit |
| Lecteur auteurs / conversion | OpenSim MATLAB, EpicToolbox et MoCapTools modifiés ; archives officielles identifiées par SHA256 des membres dans [probe](archive-probe.json) | Versions sémantiques/commits exacts des bibliothèques modifiées : **inconnue**. Code publié ≠ preuve qu'il a produit chaque sortie |
| Scripts Python passifs actuels | Python **3.11.2**, NumPy **1.26.4**, scipy **1.17.1**, c3d **0.6.0**, Pillow **13.0.0**, imageio-ffmpeg **0.8.2** | Mesurés dans `.venv` maintenant, non réattribuables aux phases3–4 ni aux auteurs |
| Runtime / tests actuels | Node **22.22.3**, Three **0.169.0**, Playwright **1.65.1**, package-lock hashé dans l'inventaire | Chromium exact des anciens tests : **inconnue**. Lock npm ne verrouille ni OS ni GPU |
| Export Blender historique phase9 | Blender **4.0.2**, Python embarqué **3.12.3**, glibc **2.39**, [rapport](../phase9/blender-report.json), [environnements](../phase9/ENVIRONMENTS.md) | Ne décrit pas le traitement AB01. Tentatives bpy4.2.0 négatives préservées |
| CI historique | Node22 majeur ; Python3.11 demandé pour certains jobs ; apt Blender/ffmpeg/numpy non verrouillés | Python shell ≠ Python Blender ; versions exactes de chaque paquet/run : **inconnue** sans artefact consulté |
| Sonde Michaud historique | NumPy2.1.3 / roue OpenSim4.6-2 cp312 dans `.github/workflows/validate.yml` | Ce n'est ni OpenSim4.4 des auteurs ni une preuve de compatibilité AB01 |
| Modèle et configurations AB01 | 24 fichiers sources et hashes : [manifest17](../phase17/source-manifest.json) ; modèles/setup dans l'index officiel phase19 | Configurations présentes ≠ paramètres effectivement utilisés pour toutes les exécutions |

## Phase3 → Phase4, preuves conservées

[Diff historique](../phase18/historical-diff.json), [code](../phase18/historical-code-evidence.txt), [code mobile](../phase18/historical-mobile-code-evidence.txt) : garde UUID de phase4 au commit `52d903122a0e8179f5ecee6a7038565adac0a563`, ancien second clip dupliqué et cache Three ; changements caméra et versions d'import `-8 → -9 → -10`. Rapport mobile introduit à `697523f7f11661eb385c9b8ada821b1edbf1aa3b`. L'amélioration ne peut pas être attribuée exclusivement à une dépendance ou à une amélioration du mouvement. Le commit du lock npm (`3b92230`) n'identifie pas le navigateur historique.

## Traçabilité CI

[Jobs du run46117733974](prior-ci-jobs.json), [index d'artefacts](prior-ci-artifact-index.json) : métadonnées consultées, pas prétention d'avoir extrait tous les artefacts. Le téléchargement des anciens logs a échoué ; la cause du premier échec navigateur phase18 reste inconnue. Les anciens jobs ont exécuté de l'authoring ; depuis `e2b43a9`, les quatre jobs historiques exigent `workflow_dispatch` et `legacy_authoring=true`. Aucun tel lancement n'est autorisé ici. Le nouveau probe ne lit que des plages d'archives publiques.
