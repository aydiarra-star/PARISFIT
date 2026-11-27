# PARISFIT — Feuille de route

| Lot | Périmètre | État vérifié |
|---|---|---|
| 0 | Cahier des charges et prompt maître | Présents sur main |
| 1 | Socle web mobile-first et identité PARISFIT | Fusionné dans main |
| 2 | Navigation Aujourd'hui / Switch / Nutrition / Mental | Prototype interactif présent |
| 3 | Persistance locale et préférences | Prototype local présent, sans synchronisation |
| 4 | Tests structurels, tests automatisés et CI | En cours : validation Node.js et tests sans dépendance |
| 5 | Accessibilité clavier et annonces dynamiques | Première couche ajoutée ; audit mobile et lecteur d'écran à réaliser |
| 6 | Modèle logique de données et confidentialité | Documenté dans DATA_MODEL.md ; non déployé |
| 7 | Contrat logique de l'API | Documenté dans API_CONTRACT.md ; non implémenté |
| 8 | Authentification, API et base de données | À concevoir après décision d'architecture |
| 9 | Bibliothèque d'exercices et programmes validés | À réaliser |
| 10 | Coach 3D et animations | À réaliser |
| 11 | Nutrition enrichie et contenus vérifiés | À réaliser |
| 12 | Moment Intelligent, tâches et équilibre de vie | À réaliser |
| 13 | Coach IA sécurisé | À réaliser |
| 14 | Abonnements et administration | À réaliser |
| 15 | HealthKit / Health Connect | À réaliser |
| 16 | Publication mobile et conformité finale | À réaliser |

## État réel actuel

Le dépôt contient une première interface web/PWA en HTML, CSS et JavaScript natifs. Les habitudes, le ressenti, l'hydratation, le journal et quelques interactions sont stockés localement dans le navigateur.

Ce socle n'est pas encore un produit complet : aucun backend, compte utilisateur, synchronisation multi-appareils, service IA, paiement, bibliothèque sportive professionnelle, animation 3D ou intégration santé n'est connecté.

Les statuts évoluent uniquement après vérification du code et exécution des contrôles correspondants.
