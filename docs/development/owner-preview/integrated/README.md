# Coach animé dans la véritable interface PARISFIT — PR13, suite

## Réalisé
Un constructeur séparé (`tools/owner-preview/build_demo.py`) dérive le paquet de démonstration de l'interface réelle index/app/styles/coach-3d. Il réutilise le renderer, les consignes par exercice et par phase, la navigation et les commandes déjà présentes. Le formulaire de retour de PR13 est réutilisé dans Coach (même clé de stockage). Aucun iframe ni laboratoire externe dans ce parcours. Un sélecteur donne accès aux huit exercices.
Le module Coach dérivé charge le GLB original avec ses huit animations et autorise la lecture exclusivement dans cet artefact interne. Les sources publiques et leur registre restent identiques ; aucune animation améliorée, aucun avis professionnel inventé. Les replacements de sécurité critiques échouent si leur source attendue change.

## Accès
`python3 tools/owner-preview/build_demo.py`, puis `python3 tools/owner-preview/demo_server.py`.
Port 3013 par défaut. Formulaire de connexion HTML (pas de dialogue HTTP Basic). Mot de passe dans PARISFIT_DEMO_PASSWORD ou, en local, .cache/owner-preview-access.txt. Minimum 16 caractères. Cookie de session HttpOnly / Secure / SameSite=Strict ; serveur vérifie l'accès pour toutes les ressources, aucune clé dans le JS ou l'URL. Session invalidée au redémarrage. Réponses no-store, pas de service worker. Le site doit avoir une origine HTTPS dédiée, jamais celle de la production. Limitation 10 essais/minute par IP, garde Origin sur POST. Derrière un proxy partageant une IP cette limite peut affecter plusieurs utilisateurs ; ce service est pour revue privée, pas une plateforme multi-utilisateur.

Après connexion : accueil PARISFIT → carte Coach / « Voir le coach » → Lecture. Pas d'autoplay imposé. Le bouton Vue parcourt face/profil/trois-quarts. Sélectionner un autre exercice suspend la lecture pour éviter une transition corporelle trompeuse.

## Hébergement stable : pas encore déployé
L'utilisateur a autorisé la préparation d'une démo distincte, avec confirmation d'hébergement/coût avant déploiement. Aucun accès de déploiement disponible ici ; connector Render unsupported. Aucun lien permanent fourni ou revendiqué.
Dockerfile prêt pour un service distinct : contexte racine, Dockerfile tools/owner-preview/Dockerfile, branche arena/5aa3aaf8-parisfit, auto-deploy désactivé. L'image finale ne contient que le paquet de démo et le serveur, pas les archives ni le dépôt. Définir PARISFIT_DEMO_PASSWORD dans les secrets de l'hébergeur, pas dans Git, et COOKIE_SECURE=1. HTTPS obligatoire. Choisir/confirmer le plan et son coût avant création. Ne pas modifier le service Render public existant. Docker build et déploiement non exécutés ici.

## Tests réellement exécutés
- `tests/owner-demo.cjs` avec Chromium/SwiftShader et émulation tactile : huit clips chargés, articulations réellement différentes après lecture, pause stable, retour au début ; 320/375/390/430 sans débordement ; taps sur commandes, sélection des trois vitesses et contrôle de l'état interne, changement de vue ; retours persistants après rechargement, export téléchargé, effacement ; ressources animées refusées sans authentification, mauvais mot de passe refusé, service-worker et .git refusés. report.json PASS.
- Premier essai échoué : politique no-referrer provoquait Origin null au POST de connexion. Corrigée en same-origin ; essai complet ensuite réussi. browser.txt conservé.
- Captures coach-*.png : véritable interface et barre de navigation PARISFIT, personnage humain texturé.

## Limites importantes
Safari iOS et iPhone physique NON testés. Connexion cellulaire réelle, pincement multitouch, reprise après interruption réseau NON testés. Pas de promesse d'accès hors ligne à cette démo privée. Le paquet GLB reste téléchargé intégralement ; temps de chargement mobile à mesurer. Aucun test Docker ni hébergement stable exécuté. L'export conserve l'ancien format des observations ; elles restent dans le stockage du navigateur pour l'origine courante, sans synchronisation serveur. Changer d'origine n'importe pas automatiquement les observations de l'ancienne prévisualisation : exporter avant migration. Aucun nouvel exercice ni amélioration biomécanique.
