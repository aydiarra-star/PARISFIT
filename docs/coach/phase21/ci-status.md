# CI — clôture de la référence exacte5eeb144

Source : [API runs/jobs/étapes et annotations](ci-reference-runs.json), requête filtrée par SHA complet,3 résultats, une tentative par run. Les horodatages GitHub sont conservés comme tels, sans réinterpréter la date de session.

| Exécution | État final | Détail |
|---|---|---|
| [46129783038 — validation du socle](https://github.com/aydiarra-star/PARISFIT/actions/runs/46129783038) | completed / success | validate réussi, étape navigateur comprise ;4 jobs authoring skipped |
| [46129783002 — passive review contracts](https://github.com/aydiarra-star/PARISFIT/actions/runs/46129783002) | completed / success | passive-contracts réussi ;28 tests historiques +8 contrôles20 |
| [46129783004 — passive evidence only](https://github.com/aydiarra-star/PARISFIT/actions/runs/46129783004) | completed / success | public-archive-metadata réussi |

**Aucun job échoué, annulé ou encore en attente pour ces3 runs.** Le diagnostic conditionnel d'échec navigateur est normalement skipped ; cela n'est pas un test supprimé. `blender-control`, `source-qualification`, `michaud-qualification`, `model-qualification` sont ignorés/skipped, pas déclarés PASS. Leurs pipelines n'ont pas été exécutés.

Le workflow validate et ses gardes n'ont pas changé depuis la référence. Dispatch explicite legacy_authoring=true reste techniquement possible, mais n'est pas autorisé ni utilisé. Le workflow séparé de contrats ne lance ni acquisition ni main des modules de traitement : fixtures synthétiques et preuves préservées. Le navigateur valide le coach existant ; ce n'est pas une reconstruction AB01. Le probe lit les archives publiques sans exécuter leur contenu.

Les annotations incluent les avis du runner sur les versions Node des actions ; aucun échec associé. Les annotations d'archives ne sont pas des validations anatomiques. La limite de propagation d'erreur du probe déjà documentée20 demeure : succès du job seul ne prouve pas chaque acquisition ; aucune modification du probe ni nouvelle acquisition locale21.

Tentative de lecture du journal complet : [résultat](log-access.json). Métadonnées détaillées/annotations consultées ; ne pas prétendre avoir lu un journal inaccessible. Aucun lien signé ou information d'accès copié.

Ces conclusions concernent **5eeb144**, pas un futur commit21. Les résultats locaux21 sont séparés dans [verification.json](verification.json). Toute CI lancée par la livraison21 doit être rapportée selon son état observé, sans présumer un PASS.
