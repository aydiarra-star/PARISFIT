# Reproduire les contrôles, sans opération distante

Depuis la racine, tant que le paquet et les copies locales existent :

```sh
python3 tools/confidentiality-audit/test_audit.py
python3 tools/animation-lock/test_static.py
npm test
```

Résultats lors de Phase25 : six tests d'audit PASS, contrôle du modèle statique PASS, régressions npm PASS. `preservation-verification.json` : 1 739 fichiers vérifiés, aucun modifié, dont 676 fichiers sous `docs/coach/` (rapports et pièces jointes antérieurs).

`publication.py` peut répéter les tests HTTP locaux contre le paquet existant (aucun déploiement). Il écrit un nouveau résultat ; garder l'ancienne preuve avant une nouvelle campagne. Aucun test n'appelle `build_public.py` en tant que commande de build pendant cet audit : le constructeur statique est seulement importé pour une comparaison en mémoire.

`inventory.py` décrit la méthode de collecte originale : worktree/cache sélectionnés, tous les arbres de commits accessibles et hashes SHA256 des blobs. Il ne faut pas écraser l'instantané Phase25 pour faire croire qu'une base ultérieure est la base initiale. Réaliser une nouvelle campagne dans un nouveau dossier de preuves.

`backup.py` décrit la sauvegarde réellement exécutée ; une seconde exécution dans le même dossier est volontairement refusée. Ne pas supprimer la première copie pour faire passer le script. Le bundle n'est pas un clone complet des métadonnées de service GitHub.

Aucune commande de purge, changement de visibilité, création de dépôt, push ou déploiement n'est incluse dans cette procédure de vérification. Les opérations de sécurisation sont proposées, non autorisées/exécutées, dans `decision-report.md`.

Après disparition du cache du sandbox, certains tests locaux échoueront par absence de fichiers : c'est la limite explicitement annoncée de la copie éphémère, pas une raison de considérer les originaux sauvegardés durablement. Les inventaires et rapports conservés restent consultables mais ne reconstituent pas les données manquantes.
