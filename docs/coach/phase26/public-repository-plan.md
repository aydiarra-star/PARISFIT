# Préparation de la séparation — Phase26

## Deux périmètres, aucun changement réalisé

**Historique à conserver** : le dépôt actuel `aydiarra-star/PARISFIT`, ses branches/refs utiles, PR, preuves et originaux. Recommandation toujours soumise à accord : le rendre privé **sans réécrire l'historique**. Les captures ignorées par Git doivent être conservées dans une destination privée durable distincte ou une zone d'archives autorisée ; rendre le dépôt privé ne sauvegarde pas ces fichiers locaux.

**Futur dépôt public propre** : nom non décidé, non créé. Ne pas faire un fork ni importer le miroir/bundle historique. Exporter uniquement les fichiers autorisés et un historique nouveau, avec instructions/licences. Pas de token d'accès aux archives dans une CI publique. Une archive privée clonée puis « nettoyée » par un commit de suppression ne devient pas un historique public sûr.

## Liste positive initiale

Le point de départ est la liste exacte des **28 fichiers** du paquet Phase24, contrôlée Phase25 (`publication-verification.json`). La liste intégrale avec chemins/hashes est reproduite dans `public-allowlist.json` et `public-allowlist.md`.

Elle couvre : HTML/CSS/JS du shell et Coach verrouillé, registre sans approbation, manifeste PWA/icône, illustrations, huit aperçus fixes, Three/GLTFLoader/BufferGeometryUtils/OrbitControls, licence Rocketbox et **GLB statique uniquement**. Aucun `docs/coach`, GLB animé, vidéo scientifique, BVH/C3D/FBX/OSIM, rapport, cache, manifestes d'archive ou outil de lecture expérimentale n'entre dans cette liste.

Ces 28 fichiers constituent un minimum de **distribution**, pas une liste définitive de développement. Un README, notices des bibliothèques tierces et tests publics peuvent être ajoutés après revue explicite. Vérifier en particulier la présence de la notice MIT Three.js avant une nouvelle redistribution ; ne pas recopier aveuglément tout `vendor`, `tools` ou `docs`.

## Dépendances et workflows à adapter avant création/publication

- Conserver les dépendances runtime locales nécessaires au rendu statique, versions et licences ; `package.json`/lockfile pour développement ne seront ajoutés qu'après tri. Aucune dépendance payante.
- `build_public.py` actuel lit le GLB original interne : **ne pas le rendre dépendant d'un accès public à cet original**. Fabrication du dérivé en environnement privé/local, hash et inspection zéro animation, puis export du dérivé autorisé uniquement. La CI publique ne reçoit ni les archives ni leurs credentials.
- Tests historiques `npm test` et tests de migration ne sont pas directement portables : ils utilisent rapports internes, originaux et commit fc51383. Les conserver côté archive ; définir des tests publics autonomes sur le seul modèle statique, le verrou, les textes, la publication et le cache, sans republier les fixtures animées.
- Remplacer les jobs d'authoring, téléchargement de sources et upload de diagnostics par un workflow public limité : syntaxe, validation de liste positive, zéro animation, vérification liens/HTTP et création d'artefact strict. Interdire les logs base64 de données scientifiques et l'upload de la racine du dépôt.
- Archives privées : analyses locales par défaut ; ne pas activer une facturation Actions privée ou du stockage payant. Vérifier le plan/quota au lieu de supposer une gratuité illimitée.
- Publication future depuis le dépôt public avec Pages seulement après autorisation et vérification des conditions du compte, chemin du projet, cache et éventuel domaine/DNS. Pas de déploiement dans cette phase. Un dépôt privé n'implique pas un site Pages privé.

## Critères avant publication

Paquet réel conforme à la liste positive et aux hashes approuvés ; aucun accès URL direct aux anciens diagnostics/captures ; zéro animation dans le GLB ; pas de mixer de mouvement ; tests des textes, données utilisateur et migration PWA ; licences et attribution présentes ; secrets absents selon revue définie ; protections et autorisations propriétaire confirmées. Le passage privé et la séparation ne révoquent pas les clones/téléchargements déjà réalisés.
