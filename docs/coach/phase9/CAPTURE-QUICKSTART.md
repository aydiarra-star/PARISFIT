# Capture du premier squat — fiche pratique

**Pas de capture réalisée.** Obtenir les autorisations phase8 avant d'enregistrer. Un adulte volontaire, opérateur identifié, variante choisie avec un professionnel si disponible. Aucun achat nécessaire sans accord préalable ; faire d'abord l'inventaire des téléphones/supports existants.

## Installation (avant l'arrivée du participant)

1. Sol plat, non glissant, espace dégagé, pas de miroir/personne secondaire. Lumière diffuse, pas de fenêtre lumineuse derrière le sujet. Tenue confortable contrastée permettant de voir genoux/hanches ; mains et chaussures entièrement visibles.
2. Deux caméras fixes en paysage : A de face, B de profil à environ 90°. Commencer vers 3–4 m du sujet, hauteur proche du bassin, puis ajuster pour garder tête, mains et pieds dans le cadre pendant toute la flexion. **Distance/hauteur indicatives, pas paramètres de calibration.** Mesurer et noter la hauteur des objectifs et les distances au repère au sol.
3. Même résolution/FPS si possible : 1080p, 60 Hz ; 30 Hz documenté si nécessaire. Pas de zoom numérique, filtre, stabilisation qui recadre automatiquement ou mode cinéma. Verrouiller mise au point/exposition. Un essai de cadrage sans enregistrement identifiable peut précéder l'accord ; aucun film personnel avant accord.
4. Mire ChArUco rigide mesurée et repère métrique : enregistrer selon le solveur, couvrant le volume du corps. Noter taille des cases, dictionnaire, sol, hauteur/distance. Ne plus déplacer les caméras. Archiver les originaux de calibration et les résultats, pas seulement une photo de la mire.

## Répétitions : un exercice, plusieurs prises séparées

- Deux à trois prises maximum envisagées pour sélectionner **un seul squat**, pas un catalogue. Nombre adapté par la personne/professionnel, jamais imposé.
- Par prise : 3 s debout naturel → une descente confortable → passage bas → remontée → 3 s debout après retour. Pas de cadence/profondeur imposée pour faire correspondre un modèle.
- Repos indicatif 30–60 s entre prises, davantage à la demande ; arrêter en cas de douleur, gêne, fatigue ou demande. Ne pas donner d'avis médical ni pousser à une reprise.
- Identifier TAKE01, TAKE02, TAKE03 dans les notes privées. Ne jamais assembler une descente d'une prise et une remontée d'une autre. Les deux caméras tournent **en même temps** sur la même prise.

## Vérifier la synchronisation (avant reconstruction)

1. Après démarrage des deux caméras, produire un clap **visuel** visible dans les deux champs, hors de la phase d'exercice. Refaire un événement net après la dernière pose. Audio facultatif uniquement s'il est autorisé ; ne pas se fier au seul son et à sa distance.
2. Dans un lecteur image par image, relever la frame du contact du clap au début et à la fin pour A et B ; noter l'incertitude si le contact est flou. Pour un flux à cadence constante, offset initial = temps événement B − temps événement A.
3. Comparer les durées entre événements : `(finA−débutA)/fpsA` et `(finB−débutB)/fpsB`. Leur différence estime la dérive. Le contrôle existant bloque au-delà d'une frame à 60 Hz ; ce n'est pas une preuve de précision 3D.
4. En cadence variable, utiliser les PTS de chaque frame, pas son index divisé par le FPS nominal. Vérifier pertes/doublons de frames. Si la dérive est notable, corriger l'alignement temporel de manière documentée, **pas la vitesse du corps** pour rendre le squat plus joli. Revoir les repères intermédiaires/visuels.
5. Revoir les deux films complets côte à côte : mêmes instants de descente/bas/remontée, pieds jamais coupés, pas de caméra déplacée. Si cette preuve manque, garder le statut « synchro incertaine » et ne pas trianguler comme si les vues étaient simultanées.

## Alternative si une seule caméra est disponible

Filmer une prise complète de profil ou trois-quarts fixe, corps/sol visibles, consentement identique. Une deuxième prise de face peut aider à apprécier la gestuelle mais **ne constitue jamais la seconde caméra du même mouvement**. Estimation monoculaire locale possible seulement après accord : profondeur, échelle, torsions et occultations incertaines ; pas de triangulation métrique fiable ni de garantie des appuis. Cette voie reste séparée et n'est pas acceptée par le manifeste stéréo actuel. Ne pas acheter une deuxième caméra automatiquement.

## À remettre, en privé

Originaux face/profil par prise, originaux calibration, paramètres/métrique/PTS/événements, manifeste, notes de variante et de sélection. Consentements/signatures/coordonnées séparés, jamais PR/chat public. L'autorisation locale n'autorise ni Arena, ni GitHub Actions, ni un autre cloud. Pour le dépôt public : uniquement données explicitement publiables et rapports sans données sensibles.
