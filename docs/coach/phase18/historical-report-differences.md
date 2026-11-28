# Différences historiques — diagnostic logiciel, pas amélioration du geste

Comparaison exhaustive des JSON, des versions Git du laboratoire et des tests. Aucun rapport antérieur écrasé ; aucun clip, runtime ou avatar modifié. Cette phase ne régénère pas les mouvements historiques pour tenter de les «améliorer».

## Sources conservées

|Rapport|Ancienne sortie|Réexécution phase17|
|---|---|---|
|Mobile|[phase2/mobile-report.json](../phase2/mobile-report.json)|[phase17/legacy-mobile-rerun.json](../phase17/legacy-mobile-rerun.json)|
|Transitions|[phase3/transition-report.json](../phase3/transition-report.json)|[phase17/legacy-transition-rerun.json](../phase17/legacy-transition-rerun.json)|

Le [diff machine](historical-diff.json) conserve les chemins, valeurs exactes, deltas etSHA256 des quatre rapports. **Six valeurs diffèrent dans chaque paire**, douze au total ; les autres champs restent identiques. Les anciens résultatsHOLD et réserves restent valables comme preuves de leur contexte historique.

## 1. Rapport mobile : mesures dépendantes de l’environnement

|Largeur|Mesure|Ancien|Phase17|Delta|
|---:|---|---:|---:|---:|
|390px|Chargement local, ms|3308|3095|−213|
|390px|FPS logiciel|30,5|32,5|+2,0|
|390px|Heap JS, octets|9956016|9734836|−221180|
|412px|Chargement local, ms|494|455|−39|
|412px|FPS logiciel|20,6|22,9|+2,3|
|412px|Heap JS, octets|12094552|12885120|+790568|

**Code vérifié :** `tests/coach-mobile.cjs` mesure le temps avecDate.now, le débit sur une fenêtre d’environ3s et le heap viaCDP Runtime.getHeapUsage. Chromium headless, SwiftShader, viewport mobile, DPR demandé3/plafonné1,25 ; service workers bloqués dans ce test. Ce ne sont pas des mesures de téléphones physiques.

Le principe de mesure reste le même, mais les conditions logicielles ne sont **pas identiques** : le rapport mobile ancien a été introduit au commit `697523f7f11661eb385c9b8ada821b1edbf1aa3b` (phase2), dont le test importe `coach-3d.js?v=20261127-8`, contre `-10` lors de la réexécution ; la phase3 utilisait `-9`. Le module a aussi évolué avant phase17 (gestion de caméra et garde de transitions notamment). [Diff exact du test et du module](historical-mobile-code-evidence.txt). Charge CPU/GPU logicielle, cache, ordonnanceur, mémoire et versions du module sont donc des facteurs possibles, mais **leur contribution individuelle n’a pas été enregistrée**. Aucun benchmark apparié répété ni intervalle de confiance ; impossible d’attribuer le gain apparent à une amélioration du produit. Les vérifications fonctionnelles (pause, arrêt hors écran, restauration de contexte, absence d’erreurs) restent identiques.

## 2. Transitions : une cause historique concrète identifiée

Les six différences portent uniquement sur `clips[1]`, nommé`crouch-to-stand` :

|Mesure|Ancien|Phase17|
|---|---:|---:|
|minSurfaceY, m|0,0019998548502243424|0,0019998563609444375|
|maxJointSpeedMS|1,1857114255315657|1,8102095920264725|
|maxPlantedPivotStepM|0,011029770741593978|0,0121783863954599|
|maxFootGapM gauche|0,03857571490540938|0,05716914372922849|
|maxFootGapM droite|0,009726435257476379|0,013041431091695038|
|pelvisHeightDeltaM|−0,46405391693115244|+0,4640541076660157|

**Indice déterminant :** dans le rapport ancien, tous les champs du second clip sont strictement identiques à ceux du premier, sauf son nom. Le mouvement prétendu ascendant y a une variation de hauteur négative.

### Chaîne de preuve

1. Les deux clips dans`assets/coach/transitions/candidates.json` n’ont pas dechampUUID. Les hashes du fichier et du modèle sont identiques entre phase3, phase4 et le commit de référence.
2. DansThree.jsr169, `AnimationClip.parse` assigne`clip.uuid=json.uuid`, donc`undefined` pour les deux clips. `AnimationMixer.clipAction` indexe son cache par cetUUID, puis par la racine, et peut retourner l’action préexistante.
3. Enphase3, commit`c391ab8e7cd0a26c4a6a02b8b05fe39068407be8`, le laboratoire parse les clips sans garde. Le test vérifie seulement une variation absolue de hauteur supérieure à0,20m : il pouvait accepter deux descentes sous deux noms.
4. Enphase4, commit`52d903122a0e8179f5ecee6a7038565adac0a563`, le laboratoire assigne un identifiant distinct aux clips qui n’en ont pas. Le test exige alors le signe attendu de chaque transition. **Cette modification existait bien avant la réexécution de phase17.**
5. La [preuve Git](historical-code-evidence.txt) montre ces deux changements. Le [contrôle des clés](cache-identity.json) parse uniquement les clips existants et confirme la collision ancienne et les clés distinctes avec la garde déjà présente. Aucun mixer.play/update, aucun rendu, aucune nouvelle animation exécuté par ce contrôle.

**Conclusion technique :** la sélection du second clip était affectée par une collision d’identifiants dans l’ancien laboratoire ; le nouveau rapport ne mesure donc pas la même action sous la même étiquette. Cette cause explique le doublon et le changement de direction, bien mieux qu’un simple bruit numérique. Les petites différences résiduelles ne reçoivent pas pour autant une cause matérielle inventée.

**Conclusion biomécanique interdite :** «le mouvement est devenu meilleur». Le modèle et les pistes restent les mêmes. Les mesures d’appui demeurent préoccupantes et le statutHOLD n’est pas levé. Ne pas comparer les vitesses comme si le protocole de sélection était identique.

## Versions et conditions : connu / inconnu

[historical-diff.json](historical-diff.json) contient les hashesGit des tests, laboratoire, candidats, modèle, vendorThree, package.json etpackage-lock aux quatre commits (phase2, phase3, phase4 et référence). Le vendorThree est identique ; versionr169. Environnement du présent audit : Node22.22.3, Python3.11.2, Playwright1.65.1, paquetThree0.169.0 ; le contrôle utilise le vendor réellement livré.

Les JSON historiques ne consignent pas la version binaire exacte deChromium, les ressources du runner, les caches ni la charge machine. **On ne peut pas rétablir rétroactivement une expérience de performance parfaitement appariée.** Les scripts documentent les argumentsSwiftShader, mais cela ne prouve pas l’identité du matériel ou de la version du navigateur utilisée pour chaque ancien rapport.

## Prévention proposée, sans changer le runtime

Pour une future campagne de mesures : conserver hashes des entrées, versions exactes, commande, environnement, identité du clip sélectionné, ordre d’exécution et journaux ; tester la distinction des clips et la direction attendue ; séparer mesures déterministes et performance variable. Toute modification du laboratoire serait une tâche séparée autorisée : **aucune correction de runtime ou de trajectoire dans cette phase**.
