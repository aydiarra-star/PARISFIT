> Phase23 — audit de consolidation, date de session2026-11-27. État audité : `5379624ffab37417a43546d6cdb6e454956c530d`. Aucun merge, déploiement, contact, devis, dépense ou changement d’animation.

# CI exacte du commit5379624

Source : [réponse API détaillée](ci-evidence.json), requête actions/runs filtrée par SHA complet, total_count3, une tentative par run. GitHub rapporte :

| Run | Résultat | Jobs |
|---|---|---|
|46131035354 — validation du socle | completed / success | validate success ; blender-control, source-qualification, michaud-qualification, model-qualification skipped |
|46131035352 — passive review contracts | completed / success | passive-contracts success |
|46131035349 — passive evidence only | completed / success | public-archive-metadata success |

**3 jobs exécutés réussis,4 jobs ignorés/non exécutés,0 échoué,0 annulé,0 en attente** sur ce commit. Étapes de diagnostic d'échec navigateur skipped normalement ; elles ne sont pas comptées comme un pipeline réussi. Aucun autre workflow/run associé à ce SHA trouvé par la requête. Déploiement non exécuté sur ce commit dans cet inventaire ; pas de workflow dispatch déclenché par cet audit.

Les gardes authoring exigent événementworkflow_dispatch ET legacy_authoring=true. Aucun changement de seuil/assertion/workflow23. Validate exécute le runtime déjà existant et les régressions navigateur ; ce n'est pas entièrement de la lecture passive, mais pas un pipeline source Blender/IK/retargeting. Contrats passifs : documents/fixtures ; probe : lecture publique sans exécution du code acquis. La limite du probe (certaines erreurs stockées en JSON sans code de sortie non nul) documentée20 reste une réserve : success du job n'est pas une validation scientifique.

États jobs/étapes consultés ; pas de journal complet téléchargé en phase23, aucun contenu supposé. La CI de la référence n'est pas la CI du futur commit livrant ce rapport. Les essais locaux23 et leurs deux échecs initiaux du harnais cache sont distingués dans [cache-audit.md](cache-audit.md).
