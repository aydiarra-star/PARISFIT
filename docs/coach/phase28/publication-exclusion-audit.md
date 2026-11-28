# Exclusion de publication — Phase28

## Branches et état de travail

Travail exclusivement sur `arena/a03f64da-parisfit`, branche dédiée existante avec PR ouverte. La session interdit la création/le changement de branche ; aucune branche supplémentaire créée. HEAD reste fc51383 et les modifications Phase24–28 sont locales/non poussées. Aucun commit/push, fusion ou déploiement pendant Phase28.

## Paquet Pages

Le workflow local `.github/workflows/deploy-pages.yml` construit puis publie uniquement `.cache/public`, par liste positive dans `tools/animation-lock/build_public.py`. L'artefact existant a été contrôlé **sans le reconstruire** : 28 noms, tailles/hashes conformes à Phase25. Les sources Phase26, le supplément, les CSV internes Phase28 et le futur dossier `archives-encrypted/` ne figurent pas dans cette liste.

Aucun volume n'existant encore, aucune preuve d'exclusion d'un *volume réel* n'est revendiquée. La frontière positive actuelle exclut les chemins proposés ; un test d'absence devra être répété une fois les volumes préparés. Les résultats restent locaux, pas une certification du site distant.

Trois motifs de secrets recherchés dans les octets du paquet actuel (clé privée age, token GitHub classique, en-tête de clé privée) : zéro correspondance. Aucun archive/capture/rapport interne dans le paquet. Ce contrôle limité n'est pas une preuve d'absence universelle de données sensibles ; les limites de la revue complète Phase26 demeurent.

## Autres workflows : réserve importante

`workflow-review.json` conserve les chemins d'upload et conditions observés :

- CI de validation : `.cache/coach-review/`, log navigateur, rapports Phase3–7.
- Workflow passif : `.cache/phase19/archive-probe.json`.
- Jobs d'authoring historiques : caches Phase9–14, exécutables seulement sur dispatch explicite `legacy_authoring`.

Aucun de ces chemins ne vise les sauvegardes `.cache/phase26-work/backups`, le futur espace `.cache/phase28-private-work` ou `archives-encrypted/`. **Mais des rapports historiques sont déjà téléversables par la CI** : ne pas dire que tous les diagnostics du projet sont privés. Ces workflows ne doivent jamais servir à chiffrer/déchiffrer les archives ni recevoir une clé, même dans les « secrets » Actions.

## Préparation retenue pour la reprise

- Garder tout travail en clair/déchiffré dans un chemin local dédié hors uploads et, pour la clé propriétaire, hors de tout dépôt.
- Placer les seuls volumes chiffrés destinés au dépôt dans `archives-encrypted/<snapshot>/…` **après** réussite de la restauration et accord de publication ; jamais dans assets, docs de rapports d'ancienne CI ou caches exportés.
- Maintenir la liste positive Pages et vérifier le contenu réel de l'artefact produit, pas seulement `.gitignore`.
- Avant un futur push, revoir tous les chemins d'upload/logs : aucune clé, plaintext de capture, archive non chiffrée ni restauration ne doit être collectée. Un garde-fou supplémentaire d'artefact pourra être intégré avec des fixtures fictives, sans déploiement.

Aucune modification des workflows n'est nécessaire pour prétendre débloquer une clé absente ; leurs limites sont documentées sans changer les preuves historiques. Les contrôles actuels ne révoquent pas les originaux déjà publics dans Git/PR/Actions.
