# PARISFIT

**MOVE. GROW. LIVE.**  
*Ton corps. Ton esprit. Ta progression.*

Compagnon numérique dédié au sport, au fitness, à la nutrition, au bien-être mental, aux habitudes et à l'équilibre personnel.

## Références officielles
- [Cahier des charges](CAHIER_DES_CHARGES.md)
- [Prompt maître](PROMPT_MAITRE.md)
- [Architecture initiale](ARCHITECTURE.md)
- [Modèle logique des données](DATA_MODEL.md)
- [Schéma PostgreSQL de conception](database/0001_core_schema.sql)
- [Contrat logique de l'API](API_CONTRACT.md)
- [Décision d'architecture backend](BACKEND_DECISION.md)
- [Authentification, sécurité et synchronisation](AUTH_SYNC_SECURITY.md)
- [Feuille de route](ROADMAP.md)

## Lancer
Ouvrir `index.html` pour voir l'interface. Pour tester l'installation PWA et le cache hors ligne, servir le dossier via HTTP(S) : les service workers ne fonctionnent pas en ouverture locale `file://`.

## Premier incrément
Interface responsive Aujourd'hui / Switch / Nutrition / Mental, navigation mobile et desktop, habitudes, hydratation, ressenti et journal enregistrés localement, parcours de respiration, manifeste installable et cache applicatif initial.

Backend, synchronisation, comptes, IA, bibliothèque sportive professionnelle, coach 3D, paiements et intégrations santé restent à construire.

L'interface PARISFIT validée reste la référence ; les fonctions nouvelles doivent s'y intégrer sans refonte arbitraire.

## État de la décision backend
Les options Supabase, Render + PostgreSQL et Firebase sont comparées dans BACKEND_DECISION.md. Supabase/PostgreSQL est l'option proposée pour un prototype technique isolé, mais aucun fournisseur n'est approuvé et aucun service cloud n'a été créé. Les exigences de sécurité et de synchronisation sont spécifiées dans AUTH_SYNC_SECURITY.md.

Le fichier database/0001_core_schema.sql est un premier brouillon PostgreSQL portable pour les comptes applicatifs, profils, consentements, objectifs, tâches, habitudes et synchronisation. Il n'a pas été exécuté sur une base et ne contient pas encore les politiques RLS propres au fournisseur retenu.