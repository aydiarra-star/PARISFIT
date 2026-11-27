# PARISFIT — Authentification, autorisations et synchronisation

**Statut : spécification fournisseur-neutre — non implémentée.**

## 1. Cycle de vie du compte

### Inscription
- Adresse e-mail et mot de passe, avec validation serveur et messages d'erreur non révélateurs.
- Vérification obligatoire de l'adresse avant synchronisation de données personnelles.
- Mot de passe haché par le fournisseur d'authentification avec un algorithme moderne adapté ; aucun mot de passe en clair ou réversible.
- Limitation de débit sur inscription, connexion, vérification et récupération.
- CAPTCHA ou protection anti-robot adaptative si les abus le justifient.
- Consentements distincts : conditions d'utilisation, confidentialité, communications marketing facultatives, traitement IA facultatif, caméra facultative, connexions santé facultatives.

### Connexion et sessions
- Cookies de session HttpOnly, Secure, SameSite lorsque l'architecture le permet ; éviter de stocker les jetons longue durée dans localStorage.
- Jetons d'accès courts et renouvellement sécurisé si architecture mobile/API l'exige.
- Rotation et révocation des sessions lors d'un changement de mot de passe, d'une suspicion de compromission ou d'une déconnexion globale.
- Afficher les sessions/appareils actifs et permettre leur révocation.
- Ne jamais journaliser les mots de passe, jetons, codes de récupération ou secrets.

### Récupération
- Lien ou code à durée courte, usage unique, envoyé à l'adresse vérifiée.
- Réponse identique que le compte existe ou non.
- Invalidation des sessions après réinitialisation.
- Aucun support humain ne demande le mot de passe ou un code à usage unique.

### MFA et rôles
- MFA activable pour les utilisateurs ; obligatoire pour administrateurs et opérateurs privilégiés.
- Rôles minimaux : user, coach_editor, support_readonly, admin.
- Principe du moindre privilège : le support ne lit pas les journaux intimes, données de santé ou conversations IA par défaut.
- Actions administratives sensibles avec journal d'audit non modifiable par l'opérateur concerné.

## 2. Autorisation et isolation des données

- Chaque ressource privée porte un propriétaire serveur owner_id dérivé de la session authentifiée ; le client ne peut pas choisir librement cet identifiant.
- Toute lecture, modification, suppression et export vérifie propriétaire, rôle et consentement.
- Défense en profondeur : vérification dans l'API ET politique RLS au niveau de la base lorsque disponible.
- Refuser par défaut toute opération non explicitement autorisée.
- Les contenus publics (exercices éditoriaux, recettes publiées, citations) sont séparés des données privées.
- Les administrateurs ne peuvent pas accéder aux données personnelles en masse sans justification, autorisation et trace d'audit.

## 3. Données à traiter avec précaution

Catégories sensibles ou à risque :
- humeur, journal, sommeil, stress et bien-être mental ;
- poids, mensurations, activité et données de santé connectées ;
- blessures, limitations, allergies et préférences alimentaires ;
- images/vidéos ou données biométriques dérivées de l'analyse du mouvement ;
- conversations avec le coach IA.

Règles :
- collecter le minimum nécessaire et expliquer l'usage avant collecte ;
- séparer les consentements facultatifs et permettre leur retrait ;
- ne pas utiliser les données sensibles pour la publicité ou la revente ;
- ne pas envoyer de journal intime, santé ou vidéo à un fournisseur IA sans base légale, information et consentement appropriés ;
- privilégier le traitement caméra sur l'appareil ; ne pas conserver la vidéo brute par défaut ;
- distinguer donnée déclarée, donnée mesurée et estimation algorithmique ;
- ne jamais présenter l'application comme un service médical ou un outil de diagnostic.

## 4. Synchronisation hors ligne

### Modèle
- IndexedDB pour le cache structuré local ; cache PWA réservé aux ressources statiques publiques.
- Chaque mutation reçoit un UUID d'événement et une clé d'idempotence.
- La file locale conserve l'ordre, les tentatives et l'état de synchronisation.
- Le serveur valide schéma, propriétaire, droits et version avant d'appliquer une mutation.
- Les réponses serveur contiennent version, date de mise à jour et état final.

### Conflits
- Préférences simples : fusion champ par champ avec règle documentée.
- Journal, séances, consommations et événements : append-only autant que possible.
- Deux modifications incompatibles d'un même objectif ou d'une tâche : présenter un conflit ou appliquer une règle explicite ; ne pas écraser silencieusement.
- Suppression : tombstone synchronisée, puis purge selon la politique de conservation.
- Horloge du client non fiable ; le serveur attribue l'heure canonique.

### Résilience
- Reprise avec backoff exponentiel et jitter.
- Déduplication côté serveur par clé d'idempotence.
- Une erreur de synchronisation ne bloque pas la consultation des données déjà disponibles hors ligne.
- Indiquer clairement à l'utilisateur ce qui est enregistré localement, synchronisé ou en attente.

## 5. Export, suppression et conservation

- Export utilisateur structuré et compréhensible (JSON/CSV selon catégorie), avec médias associés lorsque possible.
- Suppression de compte avec confirmation renforcée et délai de sécurité clairement annoncé.
- Suppression des données actives et propagation aux sous-traitants selon leurs mécanismes contractuels ; documenter les délais résiduels des sauvegardes.
- Les obligations légales de conservation éventuelles sont séparées des données supprimables et expliquées.
- Les données agrégées/anonymisées ne sont conservées que si la ré-identification est raisonnablement empêchée.
- Pas de conservation illimitée « au cas où ».

## 6. Audit et sécurité opérationnelle

Événements à tracer : connexion administrateur, changement de rôle, export, suppression, modification de consentement, accès exceptionnel au support, changement de configuration de sécurité.

Ne jamais tracer le contenu des journaux, messages IA, mots de passe, jetons ou données médicales détaillées.

Avant lancement :
- tests automatisés d'accès croisé entre utilisateurs ;
- tests d'élévation de privilèges et d'accès direct aux objets ;
- vérification des en-têtes, CORS, CSRF, XSS, injections et limites de débit ;
- revue des dépendances et secrets ;
- sauvegarde et restauration éprouvées ;
- procédure de violation de données et de notification ;
- test complet d'export et d'effacement ;
- revue des traitements, bases légales, durées et sous-traitants.

## 7. Conditions de livraison

Cette spécification n'est considérée comme implémentée qu'après réalisation d'une API, de tests automatisés d'autorisation, d'un parcours de suppression/export, d'une synchronisation testée sur plusieurs appareils et d'une revue de sécurité. La présence de ce document ne prouve aucune de ces capacités.
