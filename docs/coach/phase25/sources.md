# Sources et méthode — Phase25

Date de session : 2026-11-27 UTC. Les réponses GitHub comportent aussi des horodatages du 2026-11-28 ; ils sont conservés tels quels, sans les réinterpréter comme une preuve de date locale. Audit ponctuel, pas surveillance continue.

Sources officielles consultées en lecture seule :

- S1 — https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility : passage privé, forks publics détachés, conséquences Pages sur Free, domaine personnalisé/DNS, perte de certaines fonctionnalités et métriques.
- S2 — https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages : Pages disponible sur dépôt public en Free, sur dépôt privé avec plans compatibles payants. Dépôt privé ne signifie pas site Pages privé.
- S3 — https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository : purge, nouveaux SHA, clones/forks/PR/caches persistants, rotation des secrets en priorité, assistance GitHub non garantie pour données non sensibles.
- S4 — https://docs.github.com/en/get-started/learning-about-github/githubs-plans : dépôts privés gratuits avec collaborateurs et fonctions limitées ; consommation Actions privée soumise à quotas/facturation. Aucun forfait du propriétaire n'est supposé connu.
- S5 — https://docs.github.com/en/repositories/archiving-a-github-repository/backing-up-a-repository : sauvegarde Git miroir, objets LFS séparés si présents, métadonnées GitHub distinctes d'une sauvegarde Git.

Droits biomécaniques : dossiers de provenance et licences déjà conservés, notamment Phase5/6/7, Phase12 `SOURCES-AND-RIGHTS.md`, Phase13 `RIGHTS-AND-DATA.md`, Phase17 `source-manifest.json`, Phase20–22. Pas de nouvelle conclusion juridique ni de renouvellement prétendu des licences amont.

API lues avec `gh` : repository, Pages (404), collaborators, releases, deployments/statuses, Actions artifacts, PR11. `keys` et `invitations` refusés (403). Aucun token ou valeur de secret n'a été demandé, imprimé ou archivé.

Git : `ls-remote`, récupération de l'historique complet et des branches distantes/refs PR dans les références locales de lecture ; aucun checkout, aucune branche créée, aucun push. Historique initial superficiel, devenu complet pour les refs annoncées. Objets supprimés devenus inaccessibles, refs serveur cachées et clones externes non exhaustivement récupérables.
