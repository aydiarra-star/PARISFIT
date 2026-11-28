# Périmètre de sauvegarde — Phase26

## Inclus dans les trois archives locales restaurées

1. **`history.bundle`** : 158 commits, 28 refs nommées + HEAD (29 entrées bundle), dont 12 branches distantes et 13 refs PR récupérables, ainsi que les références locales préexistantes. Aucun tag annoncé. Les 26 lignes de refs distantes (HEAD compris) correspondent aux refs récupérées : `remote-coverage.json`. Historique non superficiel, sans prérequis externe au bundle. Les 1 779 objets Git incluent 1 135 blobs, tous vérifiés par SHA256 à la restauration.
2. **`project.tar.gz`** : 972 fichiers du projet actuel, dont modèles/textures/animations suivis, sources, licences, rapports et preuves des phases antérieures jusqu'à Phase25, workflows et configuration applicative, fichiers modifiés/non suivis Phase24/25 et outils de sauvegarde existant au moment de la capture. Inclut la liste exacte des fichiers publics et les manifestes historiques. Le fichier GLB source aux huit animations reste intact.
3. **`working-data.tar.gz`** : 811 fichiers ignorés du cache, ressources sources/captures C3D, BVH, FBX, OSIM, textures, données scientifiques, pièces de travail et paquet statique. Ces octets ne sont pas présents dans un simple bundle Git. Les copies de sauvegarde Phase25 et les produits temporaires Phase26 sont exclus pour éviter les duplications récursives.

Au total, **1 783 fichiers de travail restaurés**. Le bundle couvre en plus leurs versions historiques suivies ; ne pas additionner ses 901 fichiers à HEAD à ces 1 783 pour prétendre à autant de sources distinctes. Les manifestes détaillent chemins, tailles, SHA256 et archive d'appartenance.

## Métadonnées et reconstruction

`refs-manifest.json`, `remote-refs.txt`, `local-refs.txt`, `git-object-manifest.json`, `backup-file-manifest.json`, `archive-register.json` et les scripts Phase26 accompagnent les archives. URL sans credential : `https://github.com/aydiarra-star/PARISFIT.git`. Branche de travail : `arena/a03f64da-parisfit`, HEAD `fc51383e1a28f649a700057bb4d19bcb420c8eaf`. Il faut restaurer le bundle puis le snapshot du travail, car Phase24–26 ne sont pas dans ce HEAD.

La configuration applicative et les workflows sont inclus. **La configuration d'authentification locale Git ne l'est pas** : `.git/config`, credential helpers/credentials, hooks, reflogs et objets inaccessibles ne sont pas requis pour restaurer les preuves et ne doivent pas être partagés. Une future authentification sera reconfigurée par le propriétaire sans clé en archive.

Les rapports Phase26 produits après la capture des trois archives ne sont pas prétendus contenus rétroactivement dans ces archives. Le dossier `docs/coach/phase26/` et les outils complets seront regroupés dans un supplément de preuves avec un reçu séparé, afin d'éviter qu'une archive soit censée contenir son propre hash.

## Actions : distinction stricte

**216 artefacts listés par l'API, tous au statut métadonnées seulement dans cette campagne.** Trois tentatives représentatives : IDs 15259561640 (metadata passive), 15252890458 (qualification modèle), 15258944854 (browser-review), toutes avec code retour 1, zéro octet et aucun ZIP valide. Les fichiers de tentative vides restent hors des archives utiles et ne sont pas comptés comme contenu récupéré.

Aucun artefact n'est déclaré récupérable sur la seule base de `expired: false`. Les 213 autres n'ont pas été essayés individuellement : leur téléchargeabilité reste inconnue. Les erreurs/URL de redirection signées ne sont pas recopiées dans les rapports. Les pièces déjà présentes dans des dossiers historiques restent sauvegardées en tant que fichiers locaux, sans affirmer leur équivalence au contenu complet des ZIP distants.

`actions-metadata.json` contient IDs, noms, tailles, dates et expiration ; `artifact-retrieval.json` distingue les tentatives et les IDs connus uniquement par métadonnées. Aucun upload, aucune requête de génération d'archive côté serveur ni nouvelle exécution CI.

## Exclus / non sauvegardés

- Contenus des artefacts Actions distants, ensemble des logs distants, caches serveur, packages, wiki et commentaires/issues/PR complets ; seuls les métadonnées/refs explicitement collectés sont présents.
- Clones/forks externes, refs cachées/supprimées, données hors des comptes visibles et fichiers privés inconnus.
- Environnements installés `.venv`, `node_modules`, bytecode ; versions/outils documentés pour reconstruction. Quelques paquets déjà dans le cache sont conservés, sans garantie de compatibilité multiplateforme.
- Configurations d'accès/credentials, `.env` éventuels et liens symboliques exclus par le script ; liste concrète dans `exclusions.json`.

Cette sauvegarde est **partielle à l'échelle de l'ensemble du service GitHub**, même si le périmètre local déclaré a passé la restauration.
