# Prévisualisation interne du Coach humain

## Audit de reprise
- main distant vérifié via GitHub : 644508d1568bccfb737e1fd0ccd0a821b2caf1c9, identique au HEAD initial.
- PR12 ouverte et en brouillon, a3b21cb333962d17e014a0da92bc2f491b663232, récupéré via refs/pull/12/head et comparé : 20 fichiers de ressentis datés et preuves. Lot laissé intact dans sa PR, non réappliqué et non intégré ici.
- GLB existant : un skin, huit clips avec 82 canaux chacun. Aucun fichier original modifié.
- SHA256 original : 1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb.

## Accès propriétaire
Lancer `python3 tools/owner-preview/serve.py`. Port 3012, utilisateur HTTP Basic `owner`. Mot de passe aléatoire dans `.cache/owner-preview-access.txt` (ignoré par Git, permissions 0600). Ouvrir le lien d'aperçu Arena, de préférence dans un onglet séparé. Consulter le fichier d'accès dans le visualiseur privé de la session. Ne pas publier ce fichier. Ce mot de passe est une capacité de session, pas une authentification d'identité propriétaire.

Le proxy externe doit être HTTPS. Ne pas exposer directement le port HTTP sur un réseau non fiable. Arrêter le serveur révoque l'accès ; supprimer le fichier d'accès puis redémarrer permet de renouveler le code. L'authentification protège chaque ressource, y compris le GLB. Liste blanche de sept routes uniquement. Aucun serveur de fichiers du dépôt, aucun paramètre URL de déverrouillage. Aucun service worker, réponses no-store. Un utilisateur autorisé peut toujours copier les ressources : ce n'est pas un DRM.

## Fonctionnalités
Personnage humain Rocketbox, huit clips originaux effectivement joués par AnimationMixer. Lecture/pause, retour au début, timeline, ×0,25/×0,5/×1, face/profil/trois-quarts, rotation OrbitControls et zoom. Arrêt de la lecture quand la page devient cachée.
Retours visuels datés et liés à l'exercice, texte libre guidé, stockage local séparé de l'application, export et effacement avec confirmation. Une erreur de stockage conserve le texte saisi ; des données illisibles ne sont pas écrasées. Aucun retour transmis au serveur.

## Preuves réellement exécutées
- npm ci --ignore-scripts : succès, audit npm 0 vulnérabilité signalée.
- npm test : succès (unit.txt).
- npm run build:public : succès (public-build.txt), outils internes et GLB animé absents de la liste publique.
- tests/owner-preview.cjs : succès sous Chromium headless/SwiftShader ; huit clips avec mouvement d'os mesuré, pause stable et reset ; largeurs 320/375/390/430 sans débordement ; vues, zoom, vitesse ×0,25 ; retours enregistrés/rechargés/exportés/effacés ; 401 sans authentification et 404 hors liste blanche. browser-report.json et captures motion-* / preview-*.
- tests/coach-animation-lock-browser.cjs : succès, huit exercices publics verrouillés, pas de mixer/action, tests hors ligne et tentatives de contournement (public-lock-report.json).
- Diff des ressources/app/Coach public : aucun changement. Archives historiques non modifiées.

Les échecs initiaux restent dans browser-log.txt (libnspr4 absent) et browser-retry.txt (échantillon à 650 ms dans la pose initiale). Bibliothèques Chromium extraites, échantillon porté à 1,8 s ; suite rejouée avec succès. Dépendance navigateur uniquement dans le cache, aucun changement de package-lock.

## Limites
Tests Chromium aux dimensions mobiles, pas Safari ni iPhone physique. Rotation tactile et pincement non vérifiés sur matériel réel. Les trois vitesses existent, mais seul le contrôle ×0,25 est exercé dans cette suite. Aucun nouveau test injectant des erreurs de stockage pour ce formulaire. Pas de promesse de fonctionnement hors ligne pour cette prévisualisation authentifiée.
La capture 390 px montre le personnage humain texturé et les contrôles accessibles. Aucun jugement global sur la qualité anatomique : huit clips observables, pas huit mouvements professionnellement validés. Aucune modification/amélioration des mouvements, aucune nouvelle motion capture, aucune instruction biomécanique synchronisée ajoutée. Les captures fixes ne prouvent pas à elles seules la fluidité.
Aucune fusion ni déploiement Render. Le paquet public reste verrouillé. La PR12 reste séparée.
