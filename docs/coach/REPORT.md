# PARISFIT — Coach humain 3D : livraison partielle, non approuvée pour production

**Date : 27 novembre 2026. Statut : PR en brouillon, aucune fusion ni publication de ce chantier.**

Le personnage géométrique a réellement été remplacé par un maillage humain professionnel texturé et skinné. Cela ne suffit pas à valider la mission complète : les mouvements sont des animations originales expérimentales, pas de la motion capture ni des démonstrations approuvées par un professionnel. Le rendu reste celui d’un modèle temps réel de génération Rocketbox, pas un humain photoréaliste contemporain. Aucune promesse de qualité studio atteinte.

## 1. État initial et périmètre préservé

- Base : `83f89f8727c1de1c65dbe1278676f1daafd173fc`, fusion de la PR #10, identique au `main` distant lors de l’audit.
- Branche Arena imposée : `arena/a03f64da-parisfit` ; aucun changement direct de `main`.
- Lecture des exigences produit, architecture, README, Coach, app, HTML, styles, service worker et tests existants.
- PR #10 : accueil émeraude/corail, données locales, quatre cartes, navigation, séparation des démos, visuels et tests smoke. Ces parcours sont conservés.
- Ancien Coach : capsules/sphères, articulations `Group`, cycles procéduraux et dépendance Three.js sur jsDelivr. Aucun GLB, aucune peau skinnée, aucune texture anatomique, pas de contrôle de vitesse.
- Défaut identifié : `renderCoachStage()` remplaçait le contenu du conteneur et retirait le canvas lors d’un changement d’exercice. Corrigé : le renderer reste monté, les événements changent le clip.
- Baseline exécutée : `tests/smoke.cjs` PASS. Ce test ne validait pas le rendu WebGL ni la biomécanique de l’ancien modèle.

## 2. Modèle, provenance et droits

**Microsoft Rocketbox — Sports_Male_04**, avatar masculin en débardeur, short et chaussures, maillage humain continu, visage texturé, oreilles et doigts.

- Dépôt officiel : https://github.com/microsoft/Microsoft-Rocketbox
- Révision figée : `0943055db6ec570bcef9f2c8b41c9e5467c808f9`.
- Source : `Assets/Avatars/Professions/Sports_Male_04/Export/Sports_Male_04.fbx` et quatre textures `m026_*`.
- Licence MIT, copyright Microsoft 2020, copie dans `assets/coach/licenses/ROCKETBOX-MIT.txt`. Le README officiel confirme le passage à MIT en novembre 2020 ; l’ancienne annonce « academic use » n’est pas la licence actuelle retenue.
- La licence autorise usage commercial, modification et distribution avec conservation de la notice. Aucune ressource Mixamo ou issue d’un compte payant intégrée.
- Identifiants des blobs source, modifications et statut éditorial : `assets/coach/source.json`.
- Three.js 0.169.0 : MIT, code local et notice dans `vendor/three/`.
- Coût engagé : **0 €**, aucune consommation de crédits.

### Choix et alternatives

Rocketbox fournit une provenance vérifiable, un vrai rig humain, des textures et une redistribution MIT compatible avec un dépôt public. Les modèles cartoon de démonstration ne répondent pas à la demande. Mixamo reste une piste pour l’animation, mais aucun fichier provenant d’un compte tiers ou d’une provenance/licence non vérifiée n’a été repris. Les animations généralistes Rocketbox ne couvrent pas les huit exercices : elles n’ont pas été renommées abusivement en mouvements sportifs. Aucun générateur 3D payant n’a été utilisé.

## 3. Architecture réellement intégrée

- `coach-3d.js` : Three.js local, `GLTFLoader`, `AnimationMixer`, `OrbitControls`.
- `assets/coach/coach.glb` : géométrie, skin, 80 os, quatre images embarquées et huit clips nommés selon les IDs existants.
- Squelette : bassin, trois segments de colonne, cou/tête, clavicules, bras/avant-bras, mains, cinq chaînes de doigts par main, cuisses/mollets, pieds/orteils, os du visage.
- Hiérarchie Max corrigée à la conversion : cuisses rattachées au bassin, clavicules au thorax ; transforms mondiaux de repos préservés.
- Auteur des mouvements : `tools/coach-motion-authoring.js`, cinématique inverse à deux segments, cibles de pieds/mains et quaternions par os, échantillonnés à 30 Hz puis exportés dans le GLB. Il ne s’agit pas de faire tourner un personnage rigide pour simuler un exercice.
- Une scène, un modèle, pas de duplication par carte. Miniatures issues de captures du vrai rendu.
- Le reste de l’application reste HTML/CSS/JS natif, sans nouvelle compilation de production.

## 4. Animations : réalisé et limites par exercice

| Exercice | Réalisation examinée | Limites avant approbation |
|---|---|---|
| Squat | Flexion coordonnée bassin, hanches, genoux et bras, pieds ciblés | Amplitude, trajectoire des genoux et transfert d’appui à faire contrôler |
| Pompes | Position horizontale, flexion des coudes, déplacement coordonné torse/bassin, mains orientées vers le sol | Contact réel paume/sol, tension scapulaire et limites de poignet non validés |
| Gainage | Pose basse sur avant-bras, maintien et variation respiratoire discrète | Contacts précis et alignement à valider ; aucune mesure d’effort |
| Fentes | Fente statique avec descente et remontée, jambe arrière différenciée | Pas d’alternance gauche/droite dans ce clip ; appui arrière à vérifier |
| Jumping jacks | Ouverture des bras et jambes avec déplacement vertical | Timing de réception et réaction du sol non simulés physiquement |
| Mountain climbers | Appui des mains et avancée alternée des jambes | Trajectoires genou/hanche et stabilité scapulaire à contrôler |
| Étirement du dos | Inclinaison progressive du tronc et élévation des bras | Variante précise et consignes à harmoniser avec un professionnel |
| Mobilité épaules | Trajectoire circulaire des membres supérieurs | Animation plus large que les simples cercles d’épaules du texte actuel ; à harmoniser avant diffusion |

**Limites communes** : pas de mocap, pas de solveur de collisions corporelles/sol, pas de validation humaine spécialisée, pas de préhension dynamique ni de déformation des tissus, pas de variantes débutants animées. Les doigts sont réellement modélisés et riggés, mais leur préhension n’est pas animée indépendamment. Le mélange entre positions debout et au sol est un fondu squelettique, pas une transition naturelle capturée de mise au sol. Les étapes sont des points du cycle, pas des consignes sportives validées.

## 5. Commandes et robustesse

Fonctionnels et testés : choix des huit exercices sans rechargement, pause/reprise, vitesse ×0,25/×0,5/×1, retour à la première pose, avancement par quarts de cycle, curseur de position, face/profil/trois-quarts, rotation et zoom.

Chargement uniquement à l’ouverture visible du Coach, progression, erreurs explicites et bouton Réessayer. Absence WebGL : consignes disponibles et navigation préservée, **pas de mannequin géométrique de remplacement**. Le renderer s’arrête lorsque la scène est hors champ ou le document masqué. Pause = pas de boucle GPU continue. Ressources libérées à la fermeture hors bfcache. Préférence de réduction des mouvements respectée.

Cache v6 : moteur local et miniatures dans l’enveloppe ; GLB mis en cache après sa première ouverture réussie. **La première consultation 3D doit se faire en ligne.** Le cache ne dépend plus de jsDelivr. Chargement de la 3D hors ligne après consultation testé.

## 6. Tests techniques exécutés

- `npm test` : syntaxe JS, structure GLB, buffers/images intégrés, squelette, doigts, huit clips, valeurs finies et rotations de plusieurs articulations : PASS.
- `tests/smoke.cjs` : six largeurs 320–1440 px, accueil, eau persistée, ressenti, lecture, habitudes, Coach et shell hors ligne : PASS.
- `tests/coach-browser.cjs` : chargement réel WebGL, textures/skin, huit clips, poses distinctes, trois caméras, maintien du même canvas, pause, vitesse, reset, étapes, zoom, cinq largeurs, perte réseau + retry, préférence mouvement réduit, rechargement 3D hors ligne : PASS.
- Aucun `pageerror`, HTTP 4xx/5xx ou appel à un domaine tiers pendant le test nominal final. Les requêtes de l’échec réseau volontaire sont testées séparément.
- WebGL désactivé : message de secours et accès à Nutrition vérifiés.
- Un essai intermédiaire a révélé que les miniatures lazy-load manquaient hors ligne ; elles ont été ajoutées au précache et le test final contrôle les requêtes échouées.
- CI améliorée avec installation Chromium, tests navigateur et archivage des captures. Le résultat local n’est pas présenté comme une CI distante déjà réussie.

Rapports : [asset-report.json](asset-report.json), [browser-report.json](browser-report.json), [mobile-report.json](mobile-report.json).

## 7. Examen visuel réel

Captures prises dans Chromium avec WebGL logiciel, pas des rendus générés par IA :

- [Les huit exercices, face](evidence/eight-exercises-0.jpg)
- [Les huit exercices, profil](evidence/eight-exercises-1.jpg)
- [Les huit exercices, trois-quarts](evidence/eight-exercises-2.jpg)
- [Interface mobile 390 px](evidence/mobile-390.jpg)

Les huit exercices ont été ouverts et échantillonnés ; visage, proportions, mains, pieds, dos et genoux examinés sur les vues de face/profil. Corrections effectuées : cadrage des mouvements au sol, orientation des poignets, alignement global des pompes/gainage, ombres, conservation du canvas. Cela démontre un vrai maillage humain et une animation squelettique, **pas une certification biomécanique ni l’absence exhaustive de collisions sur chaque frame**.

## 8. Mobile et performances

GLB final : environ **3,19 Mo** (contre 7,99 Mo avant repacking des textures). Textures 1024 px, une seule instance de modèle. DPR plafonné à 1,25 en mode mobile/modeste, ombres 512 px, antialias réduit. Mesure du rendu : environ 7 522 triangles dessinés et 8 draw calls (environnement et ombres inclus) dans l’émulation testée.

Émulations tactiles Chromium 390 et 412 px, DPR demandé 3 : modèle visible et interface utilisable. Le rapport contient les temps locaux observés, affectés par l’amorçage du GPU logiciel et les caches. **Ce ne sont pas des benchmarks de téléphones.** Aucun iPhone/Safari physique, Android physique, FPS matériel, mémoire GPU réelle, chauffe ou autonomie mesuré. Cette validation demeure obligatoire avant production.

## 9. GitHub, déploiement et critères de sortie

Ce chantier doit rester en PR brouillon jusqu’à :
1. Validation par un animateur/riggeur des appuis, poignets, doigts et transitions debout/sol.
2. Validation sportive des huit mouvements et harmonisation des consignes.
3. Acquisition ou création traçable de motions de qualité suffisante si ces clips ne passent pas cette revue.
4. Essais sur Safari iOS et Chrome Android réels, y compris faible mémoire et perte de contexte WebGL.
5. Approbation du rendu facial/vestimentaire au niveau premium attendu.

Aucun commit de fusion pour ce chantier. Aucun déploiement Render lancé ou déclaré LIVE. Le connecteur Render n’est pas pris en charge dans cet environnement ; aucune URL Render publique confirmée n’a été fournie. Les données GitHub consultées montrent seulement un précédent déploiement `github-pages` du commit de base, marqué `failure` le 27 novembre 2026 à 11:55:44 UTC. Cela ne renseigne pas le statut Render. Aucune URL de production fonctionnelle confirmée ; utiliser l’aperçu Arena pour cette branche.
