# Architecture proposée dans le seul dépôt PARISFIT

## Choix

Conserver **uniquement `aydiarra-star/PARISFIT`**. Proposer, après autorisation de chiffrement réel et de publication, une archive initiale chiffrée, bornée et vérifiable dans ce dépôt. Aucun second dépôt requis. Cette phase ne crée que des rapports et outils de test, sans déplacer/chiffrer les originaux.

### A — Application publiable

Le paquet web reste la liste positive de 28 fichiers validée en Phase25/26 : shell, textes, huit exercices, illustrations, dépendances de rendu, registre verrouillé, licence et Rocketbox **statique**. Aucun dossier de données scientifiques ou d'archives, même chiffrées, n'est copié dans Pages. Le workflow futur doit publier uniquement l'artefact contrôlé, jamais `path: .`.

### B — Archives chiffrées dans Git, proposition non exécutée

```text
archives-encrypted/
  snapshot-<identifiant-opaque>/
    archive-01/manifest.json
    archive-01/volume-000000.agepart
    archive-01/volume-000001.agepart
    archive-02/...
docs/coach/phase27/             # procédure et limites, jamais de clé
```

Les archives sont compressées **avant** chiffrement au format age vers la clé publique du propriétaire, puis le fichier chiffré est découpé en volumes de **20 MiB maximum**. Chiffrer d'abord évite d'exposer des morceaux en clair. L'index public contient seulement ordre, tailles, version de format et SHA256 des volumes/ciphertext. Le manifeste détaillé des originaux et leurs SHA256 est à l'intérieur de l'archive chiffrée. Ne pas y inclure les archives chiffrées précédentes, les clés ou les caches d'authentification.

Le chiffrement ne masque pas la taille, la date, le nombre de volumes, le format ni toutes les métadonnées de transport. Aucun secret de déchiffrement dans Git, les releases, les logs, les secrets Actions ou la documentation. La clé publique n'est pas secrète mais doit être vérifiée par le propriétaire à partir de sa copie indépendante pour prévenir une substitution.

### C — Ce qui reste en clair aujourd'hui

Originaux, rapports et lecteurs historiques déjà présents dans la branche/histoire publique. **Les deux zones ci-dessus ne les rendent pas confidentiels.** La suppression/dépublication/purge n'est ni autorisée ni réalisée. Le dépôt n'est donc pas transformé en « archives privées » par l'ajout de `archives-encrypted/`.

## Bornes de fonctionnement

Un instantané des quatre archives Phase26 représente environ 370,28 MiB avant chiffrement, soit **21 volumes estimés de 20 MiB** répartis entre quatre archives. Pas de vrai chiffrement de ce volume testé ici. Le premier snapshot est techniquement compatible avec les limites Git ordinaires ; il ne s'agit pas d'une politique de sauvegarde quotidienne illimitée.

Chaque rechiffrement produit des octets nouveaux, peu compressibles et généralement non dédupliqués par Git. Interdire une tâche automatique qui ajoute un snapshot intégral à chaque commit. Fixer une enveloppe initiale de 500 MiB pour les volumes et revoir la stratégie avant de dépasser ~1 Go de dépôt ; ce sont des garde-fous proposés, pas des quotas accordés par GitHub.

**Attention à la récursion :** un futur `git bundle --all` inclurait les anciens volumes committés dans Git. Le chiffrer et le recommitter ferait grossir les sauvegardes. Conserver un bundle historique initial identifié, puis préparer explicitement le périmètre des mises à jour (export de données hors coffre, historique complémentaire à qualifier) ; ne pas promettre un miroir Git complet renouvelé sans coût croissant. Un export de fichiers sans historique doit être étiqueté comme tel.

## Variante même dépôt : Releases

Pour des mises à jour volumineuses, les pièces jointes d'une release du **même dépôt** évitent d'alourdir chaque clone Git. Les volumes et leur manifeste restent chiffrés, dans le même projet GitHub ; cela ne crée pas un deuxième dépôt. Mais ces pièces ne sont **pas des objets Git**, ne sont pas incluses dans un clone/bundle et nécessitent un téléchargement explicite. Leur récupération n'est pas testée ici ; les échecs de téléchargements Actions Phase26 imposent de vérifier la chaîne réseau avant de dépendre des pièces de release.

Aucune release, aucun tag, aucun volume réel ni transfert créé. Cette variante doit être choisie explicitement si le propriétaire ne souhaite pas ajouter ~370 MiB à Git.
