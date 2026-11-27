# Essais matériels — procédure prête, aucun appareil physique testé

**Statut : NON EFFECTUÉ sur iPhone Safari et Android Chrome.** Les rapports Chromium du dossier sont des émulations WebGL logiciel, pas des mesures de ces appareils. Aucun résultat de température/batterie/GPU matériel disponible.

## Fiche de mesure (une par appareil)

Date / testeur : ____ ; modèle : ____ ; RAM : ____ ; OS : ____ ; navigateur/version : ____ ; batterie initiale : ____ ; économie d’énergie : ____ ; réseau/latence : ____ ; température ambiante : ____ ; commit/URL de prévisualisation : ____.

Tester un iPhone Safari et un Android Chrome réels, idéalement un appareil moyen de gamme et un ancien appareil encore supporté. Utiliser une URL HTTPS de recette approuvée, jamais localhost du téléphone. Aucun déploiement en production pour ce test.

## Scénarios et relevés

| Scénario | Procédure | Mesure / critère provisoire |
|---|---|---|
| Chargement froid | Effacer le stockage du site puis ouvrir le Coach, 5 fois sur Wi-Fi et réseau mobile | Chronométrer ouverture→modèle utilisable ; médiane/p95, taille transférée, réseau. Cible indicative ≤5 s sur bon Wi-Fi, pas une garantie |
| Chargement chaud | Réouvrir sans effacer, 5 fois | Distinguer cache, téléchargement et compilation GPU |
| Cadence longue | Lire les 8 exercices pendant 15 min, changer les vues et niveaux de zoom | FPS médiane/p5 via outils développeur, interruptions >200 ms, début/5/10/15 min ; cible indicative ≥24 FPS et absence de baisse persistante >20 % |
| Mémoire | 30 changements d’exercice puis 10 pertes/retours de visibilité | Relever heap/mémoire accessibles avec méthode exacte ; rechercher croissance continue après collecte. Ne pas présenter heap JS comme VRAM |
| Chaleur / batterie | Même luminosité/réseau, 15 min puis relever | Batterie départ/fin, avertissement thermique, baisse de cadence, chaleur ressentie. Si thermomètre absent écrire « non mesurée » |
| Commandes | Pause, 0,25×, 0,5×, reset, phases, timeline, 3 vues, zoom et orbite | Animation immobile en pause ; caméra seule bouge au changement de vue ; texte de phase correspondant ; boutons tactiles accessibles |
| Cadrage | Portrait/paysage, petite/grande police, zoom navigateur | Aucun texte coupé ; modèle entier à zoom par défaut ; navigation accessible |
| Interruption | Verrouiller 30 s, changer d’application, recevoir appel/notification | Pas de course de chargement, double canvas, avance incontrôlée ou écran noir persistant |
| Hors-ligne | Visiter chaque exercice en ligne, recharger en mode avion ; tester aussi cache vide | Cache chaud utilisable ; cache vide : erreur honnête et consignes accessibles si shell disponible, pas promesse hors-ligne sans première visite |
| WebGL | Pression mémoire réelle si possible, restauration, navigateur sans WebGL | Pas de crash bloquant ; message/retry ; contenu texte préservé. Extension artificielle ≠ pression mémoire réelle |
| Accessibilité | VoiceOver/TalkBack, réduction des animations | Contrôles nommés, focus visible, phase intelligible, caméra sans tween si mouvement réduit |

## Résultats à remettre

Une ligne par scénario : PASS/FAIL/NON TESTÉ, valeur brute, unité, méthode, capture/vidéo, erreur console, conditions. Un seuil manqué n’est pas masqué par une moyenne globale. Joindre l’avis du testeur et les limitations de mesure. Toute température, mémoire ou consommation non accessible reste « non mesurée ».

Les candidates de transition ne sont pas activées dans le parcours ; leurs vidéos se consultent séparément dans la galerie. Ne pas affirmer avoir mesuré le coût runtime de transitions qui ne sont pas chargées par l’application.
