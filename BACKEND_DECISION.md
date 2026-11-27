# PARISFIT — Décision d’architecture backend (ADR-001)

**Statut : proposition documentée — aucun fournisseur sélectionné, aucun service créé.**  
**Date de revue : 27 novembre 2026**

## 1. Décision à prendre

PARISFIT doit évoluer d'une PWA locale vers une application multi-appareils avec comptes, synchronisation, données personnelles, contenus multimédias, coach IA et administration. Le backend doit rester remplaçable.

Contraintes prioritaires :
- démarrage sans dépense ni engagement automatique ;
- PostgreSQL et modèle relationnel exportable ;
- contrôle d'accès par utilisateur, vérifiable côté serveur ;
- hébergement dans une région précise de l'Union européenne si cette exigence est retenue ;
- sauvegardes, restauration et export testables ;
- synchronisation hors ligne avec résolution explicite des conflits ;
- séparation des données de bien-être, des contenus publics et des données de paiement ;
- coûts prévisibles, alertes et plafonds lorsque disponibles ;
- possibilité de migrer l'API et les données sans réécrire l'application.

## 2. Comparaison des options

| Critère | Supabase | Render + PostgreSQL | Firebase |
|---|---|---|---|
| Données | PostgreSQL relationnel | PostgreSQL relationnel | Principalement Firestore/NoSQL, avec options SQL selon produits |
| Authentification | Intégrée | À construire ou intégrer | Intégrée |
| Autorisations | PostgreSQL RLS, à concevoir et tester | API et règles applicatives à construire | Règles Firestore / IAM |
| API | API générée + fonctions | API entièrement maîtrisée | SDK et fonctions |
| Fichiers | Storage intégré | Stockage objet à ajouter | Cloud Storage |
| Temps réel | Realtime intégré | À construire | Temps réel natif |
| Portabilité | Bonne pour les données SQL ; dépendances Auth/Storage à isoler | Forte si l'application reste standard | Migration de modèle plus coûteuse si fortement liée à Firestore |
| Exploitation | Faible au démarrage | Plus élevée : API, auth, tâches, observabilité | Faible à moyenne, mais architecture orientée produits Google |
| Coût de départ | Offre gratuite limitée ; Pro affiché à partir de 25 USD/mois, compute et dépassements à surveiller | Services gratuits limités ; PostgreSQL et compute payants selon taille | Spark sans frais sous quotas ; Blaze à l'usage pour les dépassements |
| Risque principal | Dépendance aux services Supabase et quotas/pauses du plan gratuit | Plus de composants à sécuriser et maintenir | Verrouillage Firestore et coûts dépendants des opérations |

Les tarifs et quotas changent. Cette comparaison est un instantané documentaire, pas un devis ni une garantie de coût. Vérifier les pages officielles avant toute création ou bascule de plan.

## 3. Éléments vérifiés auprès des fournisseurs

### Supabase
- Le plan Free annonce notamment 500 MB de base par projet, 1 GB de stockage fichiers, 5 GB d'egress et jusqu'à 50 000 utilisateurs actifs mensuels inclus selon la page tarifaire consultée.
- Les projets gratuits peuvent être mis en pause après une semaine d'inactivité ; le plan Pro est affiché à partir de 25 USD/mois et inclut des sauvegardes quotidiennes conservées sept jours.
- Les projets sont déployés dans une région principale. Pour exiger l'Union européenne, il faut sélectionner une région AWS explicitement située dans l'UE ; le groupe générique « Europe » peut inclure Londres ou Zurich.
- La localisation de la base n'assure pas à elle seule la conformité RGPD : fonctions, journaux, sous-traitants, sauvegardes et transferts doivent aussi être examinés. Un DPA est disponible.

Sources officielles :
- https://supabase.com/pricing
- https://supabase.com/docs/guides/platform/regions
- https://supabase.com/docs/guides/security/gdpr-compliance

### Render + PostgreSQL
- Render propose des services applicatifs et PostgreSQL managé ; la tarification publiée distingue les plans gratuits limités et les instances payantes.
- La maîtrise de l'API et la portabilité sont intéressantes, mais il faut assembler et maintenir authentification, autorisations, stockage de fichiers, tâches asynchrones, sauvegardes et observabilité.
- Cette option devient pertinente si PARISFIT nécessite une logique serveur fortement personnalisée ou si l'équipe veut maîtriser chaque composant.

Source officielle :
- https://render.com/pricing

### Firebase
- Firebase propose Spark sans frais sous quotas et Blaze à l'usage.
- Auth, synchronisation et règles de sécurité sont pratiques pour un produit mobile, mais Firestore introduit un modèle NoSQL et une tarification influencée par les opérations. Cela demande une modélisation soigneuse pour les relations entre séances, exercices, habitudes, tâches et historiques.
- Pour PARISFIT, le choix doit être justifié par un besoin fort de fonctionnalités Firebase plutôt que par la seule rapidité du prototype.

Sources officielles :
- https://firebase.google.com/pricing
- https://firebase.google.com/docs/projects/billing/firebase-pricing-plans

## 4. Orientation recommandée — non approuvée

**Option à étudier en premier : Supabase avec PostgreSQL**, derrière une couche d'accès propre à PARISFIT.

Pourquoi :
1. le modèle du produit est fortement relationnel ;
2. PostgreSQL favorise les requêtes analytiques et l'export ;
3. Auth, Storage et RLS peuvent accélérer le premier backend ;
4. la couche d'accès de l'application peut masquer les SDK spécifiques et faciliter une migration future ;
5. une région UE précise est disponible, sous réserve d'auditer tous les flux et sous-traitants.

Réserves :
- ne pas considérer le plan gratuit comme une infrastructure de production garantie ;
- la mise en pause et l'absence de sauvegardes automatiques du plan gratuit sont incompatibles avec une promesse de disponibilité et de récupération ;
- les politiques RLS doivent être testées par rôle et par propriétaire ;
- les traitements IA et les données envoyées à des tiers nécessitent une analyse distincte ;
- aucune donnée sensible réelle ne doit être migrée avant validation de la sécurité et du RGPD.

**Alternative : Render + PostgreSQL** si le besoin de maîtrise serveur dépasse le gain de simplicité de Supabase.  
**Firebase** reste possible si les besoins temps réel/mobile priment et si la modélisation NoSQL est assumée.

## 5. Architecture cible indépendante du fournisseur

    PWA / application mobile
            |
            v
    Client PARISFIT (interface + cache local + file de synchronisation)
            |
            v
    Couche API versionnée /api/v1
            |
            +--> Authentification et autorisation
            +--> Services métier (habitudes, tâches, séances, nutrition, équilibre)
            +--> Service de synchronisation et conflits
            +--> Service de contenus et médias
            +--> Passerelle IA (quotas, consentement, filtrage, minimisation)
            |
            v
    PostgreSQL + stockage objet privé + journaux techniques minimisés

Le navigateur ne doit jamais recevoir une clé administrative ou un secret serveur. Les opérations sensibles passent par l'API ou des fonctions serveur protégées.

## 6. Principes de migration et de synchronisation

- Conserver localStorage uniquement pour les préférences non sensibles et le prototype ; ne pas y stocker de jetons longue durée ni de données sensibles.
- Prévoir IndexedDB pour les données structurées hors ligne, avec une file d'événements idempotents.
- Chaque enregistrement synchronisable possède un identifiant UUID, owner_id, created_at, updated_at, version et éventuellement deleted_at.
- Les mutations transmettent un idempotency_key ; les répétitions réseau ne créent pas de doublons.
- Les conflits sont détectés par version/ETag. Les données de journal ou de séance ne sont pas écrasées silencieusement.
- Pour les préférences simples, une politique documentée « dernière modification confirmée » peut être admise ; pour les historiques, préférer des événements append-only.
- Les suppressions synchronisées utilisent des tombstones jusqu'à confirmation des appareils concernés.
- Le serveur est l'autorité pour les droits, abonnements, rôles, quotas et consentements.

## 7. Garde-fous avant mise en production

- DPA et liste des sous-traitants examinés.
- Région UE précise choisie et flux hors région documentés.
- RLS / autorisations testées avec comptes distincts et rôles distincts.
- Secrets uniquement côté serveur et rotation prévue.
- MFA obligatoire pour les comptes administrateurs.
- Sauvegarde automatique, restauration et exercice de reprise testés.
- Export et suppression de compte vérifiés de bout en bout.
- Journaux sans mots de passe, jetons, contenu de journal intime ou données de santé en clair.
- Politique de conservation définie par catégorie.
- Analyse d'impact RGPD à évaluer avant les traitements à risque élevé ; avis juridique si nécessaire.
- Tests de charge, quotas, alertes de coûts et procédure d'incident.

## 8. Critères d'acceptation de la décision

Le fournisseur ne sera retenu que si un prototype isolé démontre :
1. création, vérification et récupération de compte ;
2. séparation stricte des données de deux utilisateurs ;
3. révocation de session et suppression de compte ;
4. synchronisation hors ligne sans doublons ni perte silencieuse ;
5. export lisible des données utilisateur ;
6. sauvegarde et restauration documentées ;
7. coûts estimés à 100, 1 000 et 10 000 utilisateurs actifs selon des hypothèses explicites ;
8. absence de secret privilégié dans le bundle frontend.

## 9. Hors périmètre de cette décision

Aucun compte fournisseur, projet cloud, base de données, service, abonnement, paiement, migration ou collecte de données réelles n'est créé par ce document. La sélection définitive nécessite une approbation explicite du propriétaire du projet.
