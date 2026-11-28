# Audit des accès runtime — Phase24

| Entrée | Contrôle / résultat observé |
|---|---|
| Huit sélections via `renderCoachStage` | texte conservé, verrou visible, zéro mixer/action/temps |
| Cartes bibliothèque, précédent/suivant | mêmes gardes |
| Commencer exercice / séance complète | parcours conservé, aucune lecture |
| Lecture, reset, pas, vitesse, timeline | désactivés dans HTML et runtime ; événements synthétiques refusés |
| Espace, Entrée, flèche droite sur canvas | aucun mouvement de squelette |
| `experimental`, `admin`, `autoplay`, `unlock`, `debug` en URL | aucune voie d'autorisation |
| Faux admin / validation en localStorage | aucun effet |
| Rechargement, historique retour/avance | état verrouillé |
| Changement de vue de l'application | mixer absent, aucun mouvement en fond |
| Caméra, rotation, zoom | conservés ; bouger la caméra ne fait pas jouer un clip |
| GLB original, diagnostics, transitions, docs | HTTP 404 dans le paquet public |
| Registre public | lisible, aucune donnée privée de professionnel ; ne fournit aucune animation |
| GLB statique | zéro animation ; samples retirés ; squelette/textures conservés |
| Registre absent/malformé | modèle statique et texte disponibles, aucune lecture |
| GLB animé à l'URL statique | chargement rejeté, pas de mixer |
| Hors ligne après installation v24 | instructions/modèle statique et données utilisateur accessibles |
| Anciennes URL sous worker v24, Range, `%63oach.glb` | 404 même hors ligne |
| Migration v10 → v24 | anciens caches supprimés, fenêtre rechargée, données préservées |

Preuves : `browser-report.json`, `migration-report.json`, `public-build.json`. Le test d'événements DOM force volontairement des contrôles au-delà du comportement utilisateur normal. Cela ne constitue pas un sandbox contre quelqu'un qui réécrit intégralement le JavaScript de son navigateur.

La liste positive ferme aussi les anciens lecteurs non nommés individuellement : aucun fichier `tools/` ou `docs/` n'est publié. Les originaux ne sont pas servis par la prévisualisation sur le port 3000. Le serveur de diagnostic local est distinct et n'a pas été lancé.

## Limites d'accès non résolues

Le GitHub public reste une autre source des originaux et lecteurs ; sa confidentialité n'est pas résolue par un 404 dans Pages. Anciennes copies téléchargées et anciennes PWA non mises à jour non révocables. Production distante non modifiée et non certifiée. Pas de garantie de verrouillage de tous les exemplaires distribués, ni de promesse de sécurité clinique.
