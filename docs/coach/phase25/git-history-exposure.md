# Exposition Git et GitHub — Phase25

## État observé

Dépôt `aydiarra-star/PARISFIT` **public**, propriétaire de type utilisateur. Branche de travail `arena/a03f64da-parisfit`, HEAD `fc51383e1a28f649a700057bb4d19bcb420c8eaf`. PR11 ouverte en brouillon. **Phase24 est encore dans l'arbre de travail, non commitée/non poussée** : sa protection locale ne doit pas être attribuée au commit distant fc51383.

Après récupération en lecture seule des refs annoncées :

- **12 branches distantes**, **0 tag annoncé**, **13 refs de PR** (head et merge).
- 28 références locales examinées au total, incluant les deux branches locales préexistantes et `origin/HEAD` ; aucune nouvelle branche de travail créée.
- **158 commits**, **1 135 blobs uniques**, **1 158 couples chemin/version**.
- **7 versions uniques de GLB animés**, **2 versions de BVH**, **141 versions de vidéos** ; zéro pointeur Git LFS détecté.

`remote-refs.txt` conserve les refs réellement annoncées ; `fetched-refs.txt` les refs locales après fetch. `refs-exposure.json` décrit chaque pointe de branche/PR ; `history-inventory.json` contient chemin, blob Git, SHA256, taille, nombre de commits contenant cette version et un commit témoin. Le scan couvre tous les arbres des commits récupérés, pas seulement le dernier état.

## Où se trouve l'exposition ?

La branche distante `arena/a03f64da-parisfit` contient 901 fichiers, six GLB animés, deux BVH, vidéos et rapports. La PR11/head en expose le même contenu ; sa ref merge doit aussi être prise en compte. Les 11 autres pointes de branches, dont main, n'ont aucun GLB animé/BVH dans l'arbre courant. Cela ne dispense pas de l'analyse de leur historique, incluse dans le scan global. Le dépôt public permet de consulter une branche non fusionnée : **ne pas fusionner ne protège pas ses fichiers**.

Le nombre de forks API est zéro à l'instant de collecte. Ce n'est ni un inventaire de clones, ni une garantie contre copies, miroirs, caches et téléchargements. Aucun tag annoncé ne signifie pas absence certaine de tags supprimés historiques ou de références cachées côté serveur.

## Exposition hors Git

- **216 artefacts Actions**, total de tailles API **1 638 598 572 octets** (~1,64 Go décimal). Familles : browser-review, contrôles Blender, diagnostics anatomiques, benchmark sources, qualification Michaud/modèles, metadata passive. Métadonnées de tous les artefacts listés conservées ; **leurs contenus distants n'ont pas été tous téléchargés ni audités**.
- Certains workflows historiques transportent des rapports compressés/base64 dans les logs. L'absence d'un C3D dans l'arbre Git n'exclut pas un équivalent ou des trajectoires dans un log/artefact. Les logs distants ne sont pas intégralement sauvegardés par un bundle Git.
- Aucune release listée (`releases.json`). Issues, commentaires PR, wiki, caches serveur, objets non annoncés et intégrations ne sont pas intégralement sauvegardés par cet audit.
- Liste collaborateurs renvoyée : le propriétaire administrateur seulement. Les endpoints deploy keys et invitations répondent **403** ; leur absence n'est pas établie. Les accès des GitHub Apps/tokens existants ne sont pas certifiés. Ne pas changer la visibilité avant vérification par le propriétaire.

Les artefacts d'un dépôt public ne doivent pas être qualifiés de privés au prétexte qu'un téléchargement requiert une connexion GitHub. Les paramètres exacts de téléchargement anonyme et toutes les URL signées n'ont pas été testés.

## Ce qu'une suppression ne fait pas

Supprimer dans un nouveau commit ou déplacer vers un dépôt privé laisse les versions anciennes disponibles. Un `.gitignore` ne retire pas un blob déjà suivi. Rendre privé ne retire pas les clones/forks publics déjà obtenus. Une purge force-push ne maîtrise pas toutes les refs PR, caches ou copies externes. Aucun de ces mécanismes ne constitue une révocation rétroactive universelle.

Conclusion : fermer l'accès au dépôt historique réduit l'accès futur à l'origine ; créer un nouveau dépôt public sans son historique évite de republier ces objets. Purger l'historique n'est pas une première mesure proportionnée ici tant qu'une sauvegarde durable, le périmètre et les accès ne sont pas autorisés et vérifiés.
