# PARISFIT — Modèle logique des données

> Document de conception. Ce modèle n'est pas encore déployé dans une base de données et ne constitue pas une migration SQL.

## 1. Principes directeurs

- Chaque donnée personnelle appartient à un compte utilisateur et doit être isolée des autres comptes.
- Ne collecter que ce qui sert réellement à une fonction demandée par l'utilisateur.
- Distinguer les données déclarées, calculées et importées depuis un appareil connecté.
- Ne jamais transformer un ressenti en diagnostic ou en mesure médicale.
- Les fonctionnalités de santé, la caméra, les appareils connectés, la localisation et l'utilisation de données personnelles par l'IA sont facultatives et soumises à des consentements distincts.
- L'utilisateur doit pouvoir consulter, exporter et supprimer ses données.
- Le repos, les loisirs, le divertissement et les relations sociales ont une place légitime ; aucune donnée ne doit servir à imposer une limite ou à culpabiliser.

## 2. Domaines fonctionnels

| Domaine | Entités logiques | Données principales |
|---|---|---|
| Compte et profil | users, profiles, preferences | Identité minimale, langue, fuseau horaire, unités |
| Consentements | consents, consent_events | Finalité, version, statut, date d'accord et de retrait |
| Objectifs | goals, goal_steps | Objectif choisi, échéance facultative, étapes, état |
| Organisation | tasks, task_recurrences, task_events | Titre, priorité, durée estimée, échéance, statut |
| Habitudes | habits, habit_logs | Déclencheur, routine, fréquence choisie, réalisation, pause |
| Sport | exercise_catalog, exercise_media, programs, program_steps, workout_sessions | Niveau, équipement, variantes, consignes, durée |
| Nutrition | recipes, meal_logs, hydration_logs, food_preferences | Repas déclarés, ingrédients, allergènes, préférences |
| Bien-être | mood_checkins, breathing_sessions, journal_entries, sleep_logs | Ressenti facultatif, exercices, notes privées, sommeil déclaré |
| Apprentissage | learning_items, reading_sessions, games, creative_projects | Lectures, apprentissages, jeux, idées et projets |
| Équilibre de vie | leisure_preferences, leisure_sessions, daily_balance | Repos, loisirs, divertissement, social, travail et apprentissage |
| Motivation | quotes, favorites, achievements, challenges | Citations, favoris, récompenses et défis facultatifs |
| IA | ai_preferences, ai_conversations, ai_usage_events | Préférences, historique selon consentement, quotas |
| Notifications | notification_preferences, notifications, delivery_events | Canal, fréquence, consentement, livraison |
| Offre commerciale | plans, subscriptions, invoices, payment_events | Offre, statut, dates, références du prestataire |
| Appareils | connected_sources, sync_cursors | Fournisseur, autorisation, dernière synchronisation |
| Administration | content_versions, moderation_events, admin_audit | Versions de contenu et actions administratives tracées |

## 3. Relations et propriété

- Un utilisateur possède un profil, des préférences et plusieurs consentements.
- Un utilisateur peut créer plusieurs objectifs, tâches et habitudes.
- Une habitude possède plusieurs journaux de réalisation, sans supposer qu'une journée manquée est un échec.
- Un programme référence des exercices et variantes ; une séance conserve une copie des consignes essentielles utilisées afin que l'historique reste intelligible si le catalogue évolue.
- Les repas et ressentis sont des déclarations de l'utilisateur, pas des observations médicales.
- Les périodes de loisirs et de repos sont des catégories à valeur égale dans le bilan d'équilibre.
- Les données synchronisées depuis un appareil restent identifiées comme données externes, avec leur source et leur horodatage.

## 4. Champs transverses recommandés

Pour les entités personnelles synchronisées :

- id : UUID généré côté client pour permettre un usage hors ligne.
- user_id : propriétaire obligatoire.
- created_at et updated_at : horodatages UTC.
- deleted_at : suppression logique uniquement lorsqu'elle est nécessaire à la synchronisation.
- version : numéro de version pour détecter les modifications concurrentes.
- client_mutation_id : clé d'idempotence pour éviter les doublons lors des renvois réseau.

Les dates de calendrier doivent aussi tenir compte du fuseau horaire du profil. Une date locale de séance ne doit pas être déduite uniquement d'un horodatage UTC.

## 5. Confidentialité et sécurité

### Accès et isolation
- Authentification robuste et récupération de compte sécurisée.
- Autorisation côté serveur sur chaque lecture et écriture ; ne jamais faire confiance au seul filtrage de l'interface.
- Isolation par propriétaire au niveau de la base (par exemple politiques de lignes si PostgreSQL est retenu).
- Secrets et clés uniquement côté serveur ou dans un gestionnaire de secrets ; jamais dans le dépôt Git ou le code client.
- Chiffrement en transit et au repos. Les journaux intimes et données particulièrement sensibles nécessitent une protection renforcée et des règles d'accès strictes.

### Consentements séparés
Prévoir des consentements distincts et révocables pour :
1. l'import de données d'un appareil de santé ;
2. l'analyse de mouvement par caméra ;
3. l'utilisation de données personnelles par le coach IA ;
4. les notifications non essentielles ;
5. toute collecte de localisation facultative.

Le retrait d'un consentement doit arrêter les traitements concernés et déclencher la suppression ou la désactivation des données associées selon les obligations applicables.

### IA
- Envoyer au modèle uniquement le contexte nécessaire à la demande.
- Ne jamais transmettre le journal intime, les données de santé ou les images de caméra par défaut.
- Prévoir une autorisation explicite, granulaire et révocable avant l'utilisation de catégories sensibles.
- Séparer les contenus fournis par l'utilisateur des instructions système et des contenus externes.
- Conserver des traces techniques minimales : date, modèle, durée, consommation et statut, sans recopier inutilement le contenu privé.

### Caméra et mouvement
- Analyse sur l'appareil en priorité lorsque la technologie le permet.
- Pas d'enregistrement vidéo par défaut.
- Les images brutes sont traitées temporairement et supprimées ; seuls les résultats strictement nécessaires sont conservés avec consentement.
- Ne pas afficher de correction technique si la confiance de détection est insuffisante.

### Localisation
- Aucune géolocalisation continue par défaut.
- Préférer un contexte manuel ou une activation ponctuelle explicite.
- Ne pas conserver d'historique de déplacements pour personnaliser les routines.

## 6. Conservation, export et suppression

- Définir une durée de conservation par catégorie avant la mise en production.
- Permettre l'export des données personnelles dans un format exploitable.
- Prévoir la suppression du compte et la propagation de la suppression aux données dérivées, caches, index IA et systèmes connectés, sous réserve des obligations légales de conservation.
- Conserver séparément et de manière minimisée les preuves de consentement et les éléments comptables soumis à obligation légale.
- Ne pas utiliser les données supprimées pour entraîner ou améliorer des modèles.

## 7. Synchronisation hors ligne

- Utiliser des UUID générés localement et des mutations idempotentes.
- Mettre les opérations en attente dans une file locale ; réessayer avec temporisation en cas de réseau indisponible.
- Détecter les conflits avec version et updated_at, puis demander un arbitrage lorsqu'une fusion automatique risquerait de perdre une saisie.
- Ne jamais écraser silencieusement une note personnelle ou un journal.
- Afficher clairement l'état « sur cet appareil », « en attente de synchronisation » ou « synchronisé ».

## 8. Données à ne pas collecter par défaut

- Vidéos ou photos brutes de séance.
- Position GPS continue.
- Contacts du téléphone.
- Historique de navigation ou d'utilisation d'autres applications.
- Données médicales non nécessaires à une fonction explicitement activée.
- Contenu du journal intime dans le contexte IA.
- Données publicitaires sensibles ou inférées.

## 9. Décisions restant à prendre

Avant toute migration technique, comparer les solutions d'authentification, de base de données, de stockage média, de synchronisation et d'hébergement. La décision doit tenir compte du budget, du RGPD, de l'accès mobile, des sauvegardes, de la portabilité et du coût à mesure que le nombre d'utilisateurs augmente.

Aucune technologie backend ni structure SQL définitive n'est imposée par ce document.
