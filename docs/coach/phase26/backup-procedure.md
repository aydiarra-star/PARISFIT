# Procédure reproductible — Phase26

## Préconditions

Ne modifier ni visibilité, refs distantes, branches, permissions ni sources. Aucun transfert autorisé. Disposer d'un répertoire temporaire neuf, suffisamment d'espace et d'un historique local complet pour les refs annoncées. Relever HEAD, refs et état du travail. Ne jamais utiliser `git push --mirror` pour « sauvegarder » vers un dépôt public.

## Opérations exécutées

1. `python3 tools/durable-backup/assess.py` : API en lecture seule, destinations visibles et métadonnées des artefacts. Aucune création de stockage.
2. `git ls-remote origin` et `git for-each-ref` : comparer les refs annoncées aux refs locales déjà récupérées en Phase25. Les preuves de correspondance sont dans `remote-coverage.json`.
3. `python3 tools/durable-backup/probe_artifacts.py` : trois essais d'entrée de données depuis le dépôt existant, aucun transfert sortant ; ZIP valide et CRC requis avant de compter un artefact comme récupéré. Résultat actuel : zéro ZIP récupéré.
4. `python3 tools/durable-backup/local_backup.py` : capture explicite des fichiers, SHA256, création des deux tar et du bundle. Les dossiers de sortie doivent être absents : le script refuse leur réutilisation, ne supprime pas les copies précédentes. Les fichiers Phase24/25 non committés sont inclus dans le tar de projet.
5. Restauration réelle des tar vers `.cache/phase26-work/restored/files` : refus de chemins absolus, traversée `..`, liens et écrasement ; comparaison SHA256 de chaque fichier avec son manifeste.
6. Restauration du pack bundle dans `.cache/phase26-work/restored/objects` via `git index-pack --stdin --strict` et `GIT_OBJECT_DIRECTORY`. Pas de nouvel init Git, pas de nouvelle branche, pas de checkout. Aucune alternance vers les objets source. Comparaison SHA256 de tous les objets et résolution de tous les refs du bundle.
7. Extraction de HEAD à partir de ce magasin isolé dans `restored/committed-head` : 901 fichiers. `git fsck --full --no-reflogs` contre les objets restaurés. Les noms de refs de référence restent lus depuis le dépôt source ; leurs cibles et tous leurs objets sont restaurés indépendamment.
8. `python3 tools/durable-backup/security_scan.py` : motifs de secrets dans les octets restaurés et blobs Git, plus un niveau d'archives imbriquées. Valeurs suspectes jamais imprimées.
9. Depuis `restored/files` : `npm test` et `python3 tools/animation-lock/test_static.py`. Aucune ancienne animation modifiée, aucune nouvelle capture ni calcul biomécanique.

Ces scripts ne sont pas à relancer pour écraser les preuves de cette campagne. Pour une nouvelle campagne, utiliser de nouveaux chemins de sortie et un nouveau dossier de preuves approuvés. Les archives gzip peuvent avoir un hash différent si la date ou les métadonnées changent : la reproductibilité porte sur le périmètre et les contrôles, pas sur un faux déterminisme binaire.

## Transfert durable — NON exécuté, à autoriser

1. Le propriétaire désigne une destination privée existante et gratuite, sa capacité, son contrôle d'accès, ses règles de rétention et les personnes autorisées. Vérifier l'accès sans y déposer de contenu non autorisé.
2. Résoudre les artefacts/logs manquants ou accepter explicitement leur exclusion documentée. Faire examiner les données personnelles/licences ; traiter toute alerte de secret avant partage.
3. Autoriser précisément les archives et manifestes à transférer. Chiffrer si nécessaire avec une clé détenue par le propriétaire, jamais demandée dans le chat. Conserver aussi le hash du conteneur chiffré ; un bon hash d'archive ne remplace pas la gestion des clés.
4. Vérifier taille/SHA256 sur la destination ; retélécharger une copie et restaurer dans un autre répertoire/machine. Comparer objets Git, refs et fichiers, puis exécuter les tests. Vérifier la récupération après fermeture du sandbox.
5. Confirmer la rétention et si possible une deuxième copie sur un support déjà possédé. Tant que le seul support reste le sandbox, ne pas déclarer la sauvegarde durable.

Tout changement de visibilité, création de dépôt public, purge, suppression, fusion ou déploiement nécessite encore une **autorisation séparée**, indépendamment du succès des sauvegardes.
