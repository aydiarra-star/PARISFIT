# Décision Phase27 — solution réalisable dans PARISFIT, sécurité limitée

## Recommandation

**Oui à une archive initiale chiffrée au format age, stockée en volumes de 20 MiB dans le dépôt principal `aydiarra-star/PARISFIT`, après autorisation explicite. Aucun deuxième dépôt nécessaire.**

La proposition est bornée à un instantané contrôlé : environ **370,28 MiB**, **21 volumes estimés** pour le périmètre Phase26. Pas de LFS, achat ou dépendance à Actions. L'application continue à publier uniquement son paquet statique par liste positive ; les archives ne vont pas dans Pages. Pour des renouvellements volumineux, étudier les Releases du **même dépôt**, sans prétendre que leurs assets sont sauvegardés par Git.

## Ce qui a été réellement validé

- Petit fichier **fictif de 141 octets** : tar, chiffrement age via pyrage 1.4.0, découpage, contrôle SHA256, déchiffrement et restauration identique : **PASS**.
- Mauvaise clé, altération, troncature, volume absent et ordre inversé : refus.
- Clé de test uniquement en mémoire, jamais sérialisée ou publiée ; aucune clé de production créée.
- Inventaire de 158 commits et 1 158 versions chemin/blob : six GLB actuels, une ancienne version GLB, 204 versions historiques seulement et huit chemins retirés de toutes les pointes mais toujours récupérables.
- Originaux, animations et preuves Phase26 préservés ; aucun volume réel créé, aucune archive originale chiffrée ou déplacée.

## Ce qui n'est pas validé

CLI age officielle non téléchargée avec succès ; GPG absent. Le format age est testé via l'implémentation Rust exposée par pyrage, **pas** via la CLI Go ni un test d'interopérabilité entre les deux. Pas de benchmark gros fichiers, test de publication/retéléchargement GitHub, réception d'une vraie clé propriétaire ou sauvegarde indépendante durable.

Les **216 artefacts Actions restent métadonnées seulement** selon Phase26, sans nouvelle tentative dans cette phase. Leur contenu n'est pas inclus dans les 370,28 MiB. Les archives originales Phase26 restent dans le cache temporaire ; elles ne sont pas devenues durables par la rédaction de cette proposition.

## Ce qui reste impossible avec les contraintes actuelles

1. **Confidentialité rétroactive des originaux déjà publics : impossible à affirmer.** Les nouvelles archives chiffrées ne protègent pas les anciennes versions Git/PR, téléchargements ou clones.
2. **Copie indépendante de GitHub : absente** si les seuls volumes durables sont dans ce compte/dépôt. Le chiffrement ne remplace pas un second domaine de panne.
3. **Récupération après perte de toutes les clés : impossible** avec un chiffrement correctement mis en œuvre. Le propriétaire doit accepter une conservation indépendante de la clé, même sans stockage externe dédié aux archives.
4. **Rétention illimitée gratuite : non garantie.** Les snapshots chiffrés répétés grossissent Git, les suppressions à HEAD ne récupèrent pas cet espace, et un bundle incluant son propre coffre crée une croissance récursive.

## Accord à obtenir avant réalisation

- Choix du support : un premier snapshot dans Git, ou pièces Releases du même dépôt ; périmètre et taille acceptés.
- Conservation effective de la clé par le propriétaire hors Git, avec test de récupération et copie de secours ; jamais de clé/phrase envoyée dans le chat.
- Autorisation distincte de chiffrer les originaux, de créer les volumes et de les transférer vers PARISFIT. Ces actes ne sont pas autorisés par le simple test fictif.
- Validation d'un test complet sur les vrais volumes, d'abord localement, puis après retéléchargement autorisé. Aucun statut « sauvegarde durable vérifiée » avant cette étape.

**Conclusion : solution techniquement réaliste et sans dépense prévue pour un archivage initial borné, mais ni confidentialité historique ni sauvegarde indépendante garantie.** Le choix de garder le dépôt public implique d'accepter que les ressources déjà publiées restent accessibles. Aucun changement de visibilité ou purge n'est demandé implicitement.

Aucun changement de permissions/visibilité, réécriture Git, suppression, transfert sortant, dépense, création de dépôt/release/tag, fusion, déploiement ou modification d'animation pendant Phase27. Aucune clé ou phrase secrète publiée.
