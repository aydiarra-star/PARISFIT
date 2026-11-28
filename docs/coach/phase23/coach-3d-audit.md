> Phase23 — audit de consolidation, date de session2026-11-27. État audité : `5379624ffab37417a43546d6cdb6e454956c530d`. Aucun merge, déploiement, contact, devis, dépense ou changement d’animation.

# Coach3D — préservation technique, pas validation biomécanique

Modèle : Microsoft Rocketbox Sports_Male_04, source/attribution MIT dans assets/coach/source.json et licences. GLB **5789744octets**, SHA256 **1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb**, identique à5379624. Huit clips : squat, pompes, gainage, fentes, jumpingjacks, mountainclimber, etirementdos, mobiliteepaules. Tous les fichiers runtime/assets antérieurs sont préservés.

## Tests effectués

- [coach-browser.log](coach-browser.log) : huit exercices, squelette/meshes/textures, timeline, pause/reprise, retour début, phases, ralenti0.25, zoom et trois vues ; transition coupée explicitement et pause ; mêmes canvas ; responsive320–1200 ; offline après cache, retry d'un média échoué, reduced-motion.
- [trajectory-regression.json](trajectory-regression.json) : totalité de chaque clip échantillonnée60Hz, toutes les gardes historiques PASS, aucun seuil modifié. Contact/continuité et trajectoires sont des régressions d'ingénierie, **pas des critères médicaux**. Aucun nouveau clip ni correction.
- npm : garde de transitions, assets, admission documentaire et preuves précédentes. Les vidéos comparatives3vues et ralenti historiques phase2 restent disponibles et intactes ; elles n'ont pas été remplacées par les captures d'accueil. Aucune nouvelle revue visuelle professionnelle complète revendiquée.

## Blocage : distinction impérative

`coach-transition-gate.js` conserve ses routes enabled=false et joinStatus=BLOCKED. Aucun clip AB01 ou source des phases14–22 n'est dans le GLB ou branché au runtime. Aucune transition non admise activée.

**En revanche, le blocage universel demandé n'est pas satisfait par l'existant.** Les8 démonstrations ont `validation:"experimental"` dans coach-content.js, et index.html les annonce « non validées par un professionnel ». Elles restent jouables ; il n'existe pas de gate biomécanique par clip sur ces8 démonstrations. Un test technique PASS ne peut servir à les déclarer validées.

Afin de ne pas modifier les animations ni dissimuler un changement de comportement sous couvert d'audit, les8 exercices sont conservés tels quels. L'utilisateur doit arbitrer explicitement l'usage limité de ces démonstrations expérimentales ou demander un verrouillage de lecture séparé (sans supprimer les assets). **Aucune admission biomécanique, lancement de nouvelle animation ou autorisation de production ne résulte de cette phase.** Téléphones physiques et avis professionnel restent manquants.
