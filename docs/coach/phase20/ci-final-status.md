> Phase20 — 2026-11-27, date de session. Référence `25ebee0ec3161ca5415d4961bd8d04ea4404af84`. Consultation documentaire uniquement ; aucun avis indépendant reçu.

# CI phase19 — état final de la référence exacte

Source : [réponse API archivée](ci-reference-runs.json), recherche `actions/runs?head_sha=25ebee0ec3161ca5415d4961bd8d04ea4404af84`, total_count=2. Deux exécutions, une tentative chacune ; aucun autre run annoncé par cette requête au contrôle. Ne pas substituer les runs des commits antérieurs ni ceux de phase20.

| Run | Résultat final | Jobs |
|---|---|---|
| [46118842443 — validation du socle](https://github.com/aydiarra-star/PARISFIT/actions/runs/46118842443) | completed / success | validate : success ; blender-control, source-qualification, michaud-qualification, model-qualification : skipped |
| [46118842425 — passive evidence only](https://github.com/aydiarra-star/PARISFIT/actions/runs/46118842425) | completed / success | public-archive-metadata : success |

Aucun job échoué, annulé, en attente ou en cours sur ces runs. Les étapes conditionnelles de diagnostic d'échec sont sautées normalement ; les états par étape sont dans le JSON. **Skipped n'est pas PASS** des traitements bloqués.

## Journaux réellement accessibles

Métadonnées jobs/étapes et annotations check-runs consultées, fichiers `annotations-*.json` dans ce dossier. Annotations du probe renvoient aux preuves archivées19 ; payloads encodés non dupliqués. Le téléchargement `gh run view 46118842443 --log` échoue avec EOF sur le service de logs GitHub : journal intégral non lu. URL signée et paramètres d'accès volontairement non conservés. Les conclusions success viennent de l'API GitHub, non d'une lecture exhaustive inventée du log.

## Intégrité du verrouillage

[Diff exact71bae7d→25ebee0](authoring-guard.diff) : ajout d'un input booléen false par défaut et d'une garde au niveau de chacun des4 jobs, aucune assertion supprimée ni modifiée. Condition : événement `workflow_dispatch` **et** `inputs.legacy_authoring == true`. PR/push, dispatch sans input ou avec false n'exécutent pas ces jobs. Les4 skips observés confirment le comportement sur cette PR. Un dispatch explicitement true peut toujours les lancer : ce n'est pas une interdiction technique universelle, et aucune telle autorisation n'est donnée ici.

Le job validate est inchangé : chaînes `&&`, `set -o pipefail` avant tee et absence de `continue-on-error` conservent la propagation des échecs. Les diagnostics `if: failure()` n'altèrent pas le résultat. Aucun échec connu n'a été reclassé en succès par suppression d'assertion.

## Nature des contrôles et anomalie de couverture

- Probe public : lecture d'index ZIP et de textes, CRC/hash, aucun code acquis exécuté. **Limite** : son script capture certaines erreurs dans le JSON sans toujours sortir en échec ; success du job seul ne garantit donc pas le succès d'acquisition. Le JSON19 vérifié ne contient aucune erreur ; cette réserve reste explicite.
- Validate : syntaxe/contrats documentaires et fixtures ; navigateur exécutant le runtime/animations existants et générant des rapports, pas une reconstruction source ou un export Blender. Ce n'est donc pas entièrement de la lecture passive, mais cela ne lance pas les traitements biomécaniques interdits.
- Jobs bloqués : Blender retarget/export/biomécanique, acquisition/analyse de sources et sondes modèle. `model-qualification` comprend aussi des contrôles passifs : le verrouillage large a donc **réduit la couverture automatique**, même si leurs assertions sont intactes.
- Correction minimale phase20 : workflow séparé `preliminary-review.yml`, quatre suites de contrats existantes(28 tests) sur documents/fixtures synthétiques, sans acquire/analyze main ni Blender/OpenSim. Ajout du contrôle documentaire phase20. Aucun job historique réactivé, aucun seuil changé. Les entrées `main()` des modules importés ne sont pas exécutées par ces tests.

Correction minimale proposée pour le probe réseau (non appliquée ici, aucun nouveau téléchargement requis) : ajouter après son exécution une assertion sur l'absence de `error` global/par archive dans le JSON, afin qu'un HTTP en échec fasse échouer le job. Le nouveau test documentaire20 vérifie cette propriété sur la preuve19 conservée ; il ne remplace pas ce contrôle réseau futur.

Le résultat des tests de cette correction est distinct du succès historique25ebee0 ; voir [vérifications20](verification.json). Pas de relance historique pour fabriquer une preuve manquante.
