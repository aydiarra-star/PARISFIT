# Préparation Render — démonstration distincte (NON DÉPLOYÉE)

## État vérifié
Commit de départ local/distant : 8b1bd4b36ba424c0353fa7126ece80a85b7cec53.
PR13 OPEN / DRAFT, branche arena/5aa3aaf8-parisfit. CI à ce SHA : validate SUCCESS (57 s), passive-contracts SUCCESS (18 s), quatre jobs de qualification SKIPPED. Ces résultats ne préjugent pas de la CI du nouveau commit.
Aucun accès Render disponible : connecteur unsupported, aucun secret API configuré. Aucun service créé, aucune URL réservée ou inventée. Docker absent dans cet environnement : image NON construite/testée ici.

## Configuration préparée
Blueprint dédié `render-coach-demo.yaml` (pas le blueprint public par défaut).
- Nom proposé : parisfit-coach-review (disponibilité non vérifiée).
- Service Web Docker, plan free, branche arena/5aa3aaf8-parisfit.
- Dockerfile : tools/owner-preview/Dockerfile ; contexte racine.
- Auto-deploy désactivé ; aucun disque ni base de données.
- PARISFIT_DEMO_PASSWORD : generateValue, à consulter uniquement dans les variables secrètes Render. Jamais copier dans Git, chat, JS ou logs.
- COOKIE_SECURE=1 ; PORT fourni par Render ; écoute 0.0.0.0.
- Health check / : page de connexion, pas de ressource animée.
- Le serveur refuse de démarrer sur Render sans secret explicite. Le Dockerfile exige aussi ce secret.
- Image finale : serveur et paquet démonstration seulement ; contexte Docker filtré, aucun accès file-server au dépôt ; aucune clé locale Arena requise.

## Procédure propriétaire — après contrôle zéro dépense
1. Consulter Billing / Monthly Included Usage : heures Free partagées, bande passante et minutes de build restantes, moyen de paiement et limites de dépenses. Ne pas créer le service tant qu'un dépassement facturable reste possible. Ne pas modifier la facturation ou les services existants sans accord.
2. Créer un NOUVEAU Web Service dans Render, dépôt aydiarra-star/PARISFIT, branche indiquée ci-dessus. Ne sélectionner ni parisfit ni parisfit-preview.
3. Choisir Docker, chemin du Dockerfile ci-dessus, contexte racine, instance Free, auto-deploy désactivé. Aucune option payante ni disque.
4. Générer un secret aléatoire fort (au moins 32 caractères recommandé) dans le gestionnaire de mots de passe/variables Render ; définir PARISFIT_DEMO_PASSWORD et COOKIE_SECURE=1. Alternative Blueprint : choisir explicitement render-coach-demo.yaml, qui génère le secret côté Render.
5. Avant confirmation, vérifier que la création ne modifie que le nouveau service et que le coût affiché est zéro. En cas de Free indisponible : arrêter, ne pas choisir une offre payante.
6. Après déploiement réussi, copier l'URL HTTPS réellement attribuée par Render. Ne pas déduire l'URL du nom souhaité.
7. Safari, onglet normal : connexion, ouvrir Coach, sélectionner chaque exercice puis Lecture. Exporter les retours avant de fermer/effacer les données Safari. Vérifier accès refusé au GLB dans une session sans cookie.
8. Transmettre uniquement URL, état et éventuelles erreurs expurgées — pas le secret. Aucun merge PR13 requis.

## Compatibilité Free et risques zéro dépense
Documentation officielle consultée : https://render.com/docs/free
Web services Free et TLS disponibles. Mise en veille après 15 minutes sans trafic ; réveil annoncé autour d'une minute ; fichiers locaux éphémères. 750 heures Free mensuelles partagées par workspace. Épuisement des heures : suspension des services Free du workspace (donc impact potentiel sur les services existants). Bande passante et builds peuvent être facturés au dépassement si un moyen de paiement est présent ; le seul champ plan: free NE garantit PAS zéro dépense. Vérifier les conditions du compte et les contrôles de consommation avant déploiement. Aucun contournement de quotas ni mécanisme de maintien éveillé ajouté.
La démonstration est sans base serveur persistante : retours dans Safari, export nécessaire. Redémarrage/sommeil invalide le cookie de session, nouvelle connexion nécessaire. Une adresse stable n'implique pas disponibilité permanente ni réveil instantané.

## Vérifications exécutées dans ce lot
- Construction du paquet démonstration : PASS (build.txt).
- tests/owner-demo-isolated.py : PASS (isolated-runtime.json). Exécution dans un répertoire temporaire contenant uniquement serveur et paquet runtime, PORT arbitraire, secret d'environnement jetable, aucun fichier secret Arena. Contrôle 401/303/200, cookie sécurisé, requête cross-origin 403, huit clips GLB, chemins internes 404, aucun secret dans ressources/logs, échec sans secret Render.
- npm test : PASS (unit.txt).
- tests/owner-demo.cjs rejoué : PASS (browser-report.json), huit clips avec changements d'articulations, commandes tactiles simulées, quatre largeurs, conservation/export/effacement. Nouvelles captures conservées dans ce dossier, anciennes captures préservées.

Non exécutés : déploiement Render, test Docker, Safari iOS physique, réseau cellulaire réel, vérification des quotas du compte. Tests Chromium locaux ne valent pas validation iPhone ni validation biomécanique.
