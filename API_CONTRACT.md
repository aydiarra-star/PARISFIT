# PARISFIT — Contrat logique de l'API

> Proposition de contrat pour préparer le futur backend. Ces routes ne sont pas encore implémentées ni accessibles en production. Le choix du framework et de l'hébergeur reste ouvert.

## 1. Conventions générales

- Préfixe versionné : /api/v1.
- Transport HTTPS uniquement.
- Corps JSON UTF-8 ; dates/horodatages au format ISO 8601 UTC.
- Les dates de journée sont transmises avec le fuseau horaire IANA du profil, par exemple Europe/Paris.
- Les identifiants sont des UUID.
- Les réponses personnelles sont toujours limitées au compte authentifié.
- Pagination par curseur pour les listes longues ; taille par défaut 20, maximum 100.
- Les champs inconnus ou non autorisés ne doivent pas être silencieusement acceptés.
- Les erreurs ne doivent jamais divulguer de secrets, de données d'un autre compte ou de détails internes.

## 2. Authentification et compte

| Méthode | Route | Usage |
|---|---|---|
| POST | /auth/register | Créer un compte |
| POST | /auth/login | Ouvrir une session |
| POST | /auth/refresh | Renouveler une session |
| POST | /auth/logout | Révoquer la session courante |
| GET | /me | Lire le profil courant |
| PATCH | /me | Modifier les préférences et le profil |
| POST | /me/export | Demander un export de ses données |
| DELETE | /me | Demander la suppression du compte |

Les jetons doivent être courts et renouvelables ; les mécanismes de stockage côté client seront définis selon la cible web/mobile. Ne jamais placer de secret serveur dans l'application cliente.

## 3. Consentements et confidentialité

| Méthode | Route | Usage |
|---|---|---|
| GET | /consents | Consulter les consentements |
| PUT | /consents/{purpose} | Accorder ou mettre à jour un consentement |
| DELETE | /consents/{purpose} | Retirer un consentement |

Les finalités sont indépendantes : données de santé, caméra/analyse de mouvement, personnalisation IA, notifications non essentielles et localisation facultative. Chaque changement conserve une trace minimale de la version et de la date. Le retrait doit bloquer immédiatement le traitement concerné.

## 4. Objectifs, tâches et habitudes

| Méthode | Route | Usage |
|---|---|---|
| GET / POST | /goals | Lister ou créer des objectifs |
| GET / PATCH / DELETE | /goals/{id} | Lire, modifier ou supprimer un objectif |
| GET / POST | /tasks | Lister ou créer des tâches |
| GET / PATCH / DELETE | /tasks/{id} | Modifier une tâche |
| GET / POST | /habits | Lister ou créer des habitudes |
| GET / PATCH / DELETE | /habits/{id} | Modifier une habitude |
| GET / POST | /habits/{id}/logs | Consulter ou enregistrer une réalisation |

Les tâches doivent prendre en charge les priorités, durées estimées, échéances facultatives, répétitions et reports. Une habitude peut être mise en pause ; une absence de réalisation n'est pas automatiquement transformée en échec.

## 5. Sport et programmes

| Méthode | Route | Usage |
|---|---|---|
| GET | /exercise-catalog | Consulter le catalogue publié |
| GET | /exercise-catalog/{id} | Lire un exercice et ses variantes |
| GET | /programs | Consulter les programmes disponibles |
| GET | /programs/{id} | Lire un programme |
| GET / POST | /workout-sessions | Consulter ou enregistrer des séances |
| GET / PATCH | /workout-sessions/{id} | Lire ou corriger une séance personnelle |

Les contenus publiés doivent avoir un statut de validation, une version et une provenance interne. Les variantes accessibles, les contre-indications, les consignes et les limites de chaque exercice sont des champs éditoriaux explicites. Une réponse de caméra incertaine ne doit pas produire de correction présentée comme fiable.

## 6. Nutrition et bien-être

| Méthode | Route | Usage |
|---|---|---|
| GET | /recipes | Consulter les recettes publiées |
| GET / POST | /meal-logs | Consulter ou enregistrer des repas déclarés |
| GET / POST | /hydration-logs | Consulter ou enregistrer l'hydratation |
| GET / POST | /wellbeing/checkins | Enregistrer un ressenti facultatif |
| GET / POST | /breathing-sessions | Enregistrer une séance de respiration |
| GET / POST | /journal-entries | Gérer les notes privées |
| GET / POST | /sleep-logs | Gérer les données de sommeil déclarées |

Les contenus nutritionnels doivent indiquer les allergènes et rester informatifs. Les ressentis, repas et données de sommeil ne sont pas des diagnostics. Les journaux sont privés et exclus du contexte IA par défaut.

## 7. Moment Intelligent et équilibre de vie

| Méthode | Route | Usage |
|---|---|---|
| GET / POST | /learning-items | Gérer les contenus d'apprentissage |
| GET / POST | /reading-sessions | Enregistrer la lecture |
| GET / POST | /games/sessions | Enregistrer les jeux et défis |
| GET / POST | /creative-projects | Gérer les idées et projets |
| GET / PATCH | /balance/preferences | Préférences de temps libre |
| GET / POST | /balance/sessions | Déclarer repos, loisirs, divertissement, social, travail ou apprentissage |
| GET | /balance/daily | Consulter le bilan personnel d'une journée |

Les loisirs, le divertissement et le repos sont des catégories de même dignité que le travail ou l'apprentissage. Le bilan ne doit pas classer moralement les activités, imposer des limites ou optimiser le temps passé dans PARISFIT.

## 8. Coach IA

| Méthode | Route | Usage |
|---|---|---|
| GET / POST | /ai/conversations | Consulter ou créer une conversation |
| GET / POST | /ai/conversations/{id}/messages | Lire ou envoyer un message |
| DELETE | /ai/conversations/{id} | Supprimer une conversation |
| GET | /ai/usage | Consulter les quotas et l'usage |

Avant chaque appel, le serveur vérifie les consentements et ne transmet que les données strictement nécessaires. Les données de santé, le journal et les images de caméra sont exclus par défaut. Les réponses doivent être contrôlées selon les règles de sécurité du domaine. Les quotas sont appliqués côté serveur.

## 9. Appareils et synchronisation

| Méthode | Route | Usage |
|---|---|---|
| GET | /devices/connections | Lister les connexions autorisées |
| POST | /devices/connections | Initier une connexion |
| DELETE | /devices/connections/{id} | Révoquer une connexion |
| POST | /sync/batch | Envoyer un lot de modifications hors ligne |
| GET | /sync/changes | Récupérer les changements depuis un curseur |

Chaque mutation hors ligne porte un identifiant idempotent et une version. Les conflits non fusionnables renvoient un statut 409 avec les métadonnées nécessaires à l'arbitrage. Aucune note ou saisie personnelle ne doit être écrasée silencieusement.

## 10. Abonnements et administration

- Les opérations de paiement sont initiées côté serveur via un prestataire ; aucune donnée de carte bancaire n'est stockée par PARISFIT.
- Les webhooks de paiement sont vérifiés cryptographiquement, dédupliqués et journalisés.
- Les routes /admin/* exigent un rôle explicite, une autorisation côté serveur et une journalisation des actions.
- Les administrateurs gèrent les exercices, programmes, recettes, citations, défis, notifications et versions de contenu.
- L'accès administratif au journal intime, aux messages privés ou aux données de santé est interdit par défaut.

## 11. Format de réponse et erreurs

Réponse réussie indicative :

    {
      "data": { },
      "meta": {
        "request_id": "uuid",
        "next_cursor": null
      }
    }

Erreur indicative :

    {
      "error": {
        "code": "VALIDATION_ERROR",
        "message": "Certains champs sont invalides.",
        "request_id": "uuid",
        "fields": {
          "title": "Ce champ est obligatoire."
        }
      }
    }

Codes HTTP attendus : 200/201 pour succès, 204 pour suppression sans corps, 400 pour requête invalide, 401 pour session absente ou invalide, 403 pour accès interdit, 404 pour ressource inconnue, 409 pour conflit de version, 422 pour validation métier, 429 pour limite atteinte et 500 pour erreur interne générique.

## 12. Sécurité et fiabilité obligatoires

- Vérifier l'identité et la propriété de chaque ressource côté serveur.
- Appliquer des limites de débit par compte et par adresse réseau, sans exposer de données personnelles.
- Utiliser des clés d'idempotence sur les créations susceptibles d'être rejouées.
- Valider les entrées, tailles de texte, fichiers, types MIME et formats.
- Ne jamais accepter un user_id fourni par le client comme preuve de propriété.
- Appliquer les politiques d'accès au niveau base de données lorsque la technologie le permet.
- Protéger les webhooks contre les répétitions et les signatures invalides.
- Tracer les opérations sensibles sans recopier le contenu privé.
- Prévoir sauvegardes, restauration testée, rotation des secrets et alertes d'incident.

## 13. Scénarios de test d'acceptation

1. Un utilisateur A ne peut ni lire ni modifier les données de l'utilisateur B, même en changeant un UUID dans l'URL.
2. Une mutation rejouée avec la même clé d'idempotence ne crée pas de doublon.
3. Un conflit de version renvoie 409 et ne perd aucune saisie.
4. Le retrait du consentement IA bloque l'envoi des données correspondantes.
5. Le retrait d'une connexion santé stoppe les synchronisations ultérieures.
6. La suppression d'un compte déclenche le processus prévu pour les données dérivées et les sauvegardes.
7. Un utilisateur sans abonnement ne peut pas appeler une fonction premium en contournant l'interface.
8. Une route d'administration est inaccessible à un compte standard.
9. Les réponses d'erreur ne révèlent aucune information sur les autres utilisateurs.
10. Les temps de repos et de loisir restent enregistrables sans objectif de productivité.

## 14. Décisions restant ouvertes

Ce contrat ne choisit pas le fournisseur d'authentification, la base de données, le framework API, le stockage média ou le prestataire de paiement. Ces choix doivent être comparés avant le développement du backend, puis les routes seront ajustées et versionnées avec les tests correspondants.
