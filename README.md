# PARISFIT

**MOVE. GROW. LIVE.**  
*Ton corps. Ton esprit. Ta progression.*

Compagnon numérique dédié au sport, au fitness, à la nutrition, au bien-être mental, aux habitudes et à l'équilibre personnel.

## Références officielles
- [Cahier des charges](CAHIER_DES_CHARGES.md)
- [Prompt maître](PROMPT_MAITRE.md)
- [Architecture initiale](ARCHITECTURE.md)
- [Feuille de route](ROADMAP.md)

## Lancer
Ouvrir `index.html` pour voir l'interface. Pour tester l'installation PWA et le cache hors ligne, servir le dossier via HTTP(S) : les service workers ne fonctionnent pas en ouverture locale `file://`.

## Premier incrément
Interface responsive Aujourd'hui / Switch / Nutrition / Mental, navigation mobile et desktop, habitudes, hydratation, ressenti et journal enregistrés localement, parcours de respiration, manifeste installable et cache applicatif initial.

Backend, synchronisation, comptes, IA, bibliothèque sportive professionnelle, coach 3D, paiements et intégrations santé restent à construire.

L'interface PARISFIT validée reste la référence ; les fonctions nouvelles doivent s'y intégrer sans refonte arbitraire.


## Coach sportif 3D — premier incrément
Le Coach IA charge un avatar humanoïde procédural articulé via Three.js/WebGL. Les huit exercices disponibles ont des cycles de mouvement dédiés, avec commandes pause/reprise et vues de face/profil. Three.js est chargé depuis jsDelivr ; une connexion est donc nécessaire pour ce rendu. En cas d'absence de WebGL ou d'échec du CDN, un affichage de secours est conservé. Ce modèle est une base stylisée en 3D, pas un avatar photoréaliste ni une animation de capture de mouvement professionnelle.
