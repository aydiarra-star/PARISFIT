# Politique de verrouillage — Phase24

Date : 2026-11-27. Base : fc51383. Fonctionnalité technique ≠ validation biomécanique.

## Défaut fermé

`animation-validation.js` est le point de décision. Registre absent, JSON illisible, clip inconnu/dupliqué, statut autre que `validée`, absence de preuve, hash différent : refus. Aucun paramètre URL, localStorage, cookie ou rôle « admin » ne donne d'accès. Le registre chargé est gelé récursivement. Son édition relève d'une revue de code, pas d'un écran utilisateur.

Le runtime vérifie l'admission avant sélection/lecture/recherche temporelle, changement de vitesse et boucle d'animation. Le verrou arrête les actions éventuelles, désalloue le mixer et annule la boucle de mouvement. Aucun mixer n'est créé pour ces huit clips. Les événements forcés sur des contrôles réactivés dans le DOM ne déverrouillent rien.

## Défense par absence de données

Le site publie seulement un GLB **statique dérivé**, construit à partir de Rocketbox. Les huit clips originaux restent inchangés dans le dépôt. Le dérivé retire animations, accessors, bufferViews et échantillons binaires propres aux animations ; il ne s'agit pas de masquer simplement le champ `animations`. Géométrie, poids, squelette au repos, matériaux et quatre textures sont conservés ; test octet par octet.

Le runtime rejette même un GLB animé livré frauduleusement à l'URL statique. Dans cette livraison, une simple modification de statut ne suffit donc pas à activer une animation : il faudrait une nouvelle intégration/version de publication examinée séparément. Ce choix volontairement plus restrictif évite un déverrouillage administratif accidentel.

## Publication et diagnostics

`python3 tools/animation-lock/build_public.py` construit `.cache/public` par **liste positive**. Le workflow Pages n'envoie plus la racine du dépôt. `tools`, `docs`, `tests`, `.git`, GLB original et transitions sont exclus. Ne jamais héberger la racine comme site public. La prévisualisation de cette phase sert uniquement ce paquet.

Pour un audit interne local : `python3 tools/animation-lock/serve_internal.py --acknowledge-unvalidated`, puis `http://127.0.0.1:3012/tools/coach-lab.html`. Le serveur écoute seulement l'interface locale ; il n'est pas un système d'authentification ni un service privé distant. Les essais scientifiques ne deviennent pas une expérience utilisateur.

**Limite réelle : le dépôt GitHub est public** (`repository-visibility.json`). Ces outils et originaux restent donc récupérables hors du paquet web, y compris par l'historique. Ne pas prétendre à leur confidentialité. Une décision du propriétaire concernant l'accès au dépôt/archives serait nécessaire pour une restriction de distribution plus large ; aucune modification de visibilité n'a été effectuée. Des copies déjà téléchargées ne peuvent pas être révoquées.

## Cache et hors ligne

Cache `parisfit-shell-v24`, versions de shell renouvelées, modèle statique précaché. Activation : purge des anciens caches Parisfit, conservation des caches étrangers et du localStorage, rechargement des fenêtres existantes lors d'une migration. Les navigations ne sont pas attendues dans `activate` pour éviter une attente circulaire avec les fetchs. Le worker bloque aussi les anciennes URL d'animation et diagnostics, y compris hors ligne, URL encodée et requête Range testées.

Un client resté hors ligne avec l'ancienne version continue à posséder ses anciens fichiers jusqu'à réception du nouveau worker. Une installation échouée ne peut pas garantir cette migration. Aucune révocation distante universelle n'est possible. Aucun déploiement effectué.
