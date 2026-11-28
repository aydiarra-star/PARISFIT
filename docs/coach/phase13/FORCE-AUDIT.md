# Plates-formes — mesures disponibles, interprétations conditionnelles

**VALIDÉ :** lecture des12composantes et alignement des timestamps publiés. **EN ATTENTE DE VALIDATION HUMAINE :** calibration physique, repères et association pied/plate. **NON TESTÉ :** centre de pression, forces articulaires, moments articulaires et dynamique inverse.

## Acquisition et intégrité

Deux AMTI AccuGait selon le déposant ; CSV100Hz, Fx/Fy/Fz enN, Mx/My/Mz enN·m. `forces-report.json` contient plages de toutes les composantes, seconde différence RMS, seuils et dérive de pieds. Les valeurs finies et le même time que les marqueurs vérifient le fichier, pas le capteur, son zéro ou son trigger.

Pas d'essai de plate déchargée dans le sous-ensemble, matrice de calibration, incertitude métrologique ou log de compensation de latence. Les variations rapides du signal chargé ne sont **pas** un bruit de capteur mesuré.

## Détection d'appui sans correction de mouvement

Sensibilité à10/20/50/100N sur Fz, seuils de triage seulement. Les deux plates restent chargées pendant la répétition, à tous ces seuils. Cette constatation ne distingue pas à elle seule descente, bas et remontée. Ces phases sont reliées à l'annotation du déposant et à la trajectoire verticale du proxy pelvien.

Les centres de platesX/Y sont connus :1=(−0,698;0),2=(0;0). La proximité géométrique du milieu talon/métatarsien à ces centres est comptée pour chaque pied. Cela rend l'association droite→1/gauche→2 plausible, mais ne certifie pas la surface de semelle, une éventuelle contribution croisée ou les dimensions/orientations exactes des plates.

La fraction Fz1/(Fz1+Fz2) varie d'environ45,67% à57,06%, moyenne50,74%. C'est une **répartition entre plates**, pas une validation de symétrie biomécanique. Pas de normalisation par poids corporel : masse et charge ne sont pas extraites pour cette analyse, aucun bilan COM/forces supposé.

Les talons sont des marqueurs cutanés : leur déplacement horizontal de21,8/25,0mm depuis le début n'est pas un glissement de semelle mesuré. Leur hauteur au-dessus deZ=0 n'est pas un gap de contact ; le marqueur n'est pas placé sous le pied.

## Synchronisation

Égalité numérique des3350timestamps marqueurs/forces. Analyse exploratoire de corrélation entre accélération verticale du **proxy de bassin** et Fz total sur±10samples : maximum au paramètre−2samples, corrélation≈0,9974. Dans le code, k<0 associe a(t) àF(t−k·dt). **Ne pas interpréter cela comme une latence instrumentale de20ms** : bassin≠COM, répartition segmentaire mobile, signaux courts et relation dynamique non identifiée. Aucun signal n'est décalé.

## Pourquoi aucun COP

Les moments sont présents, mais les informations nécessaires à une transformation certifiée vers la surface de contact ne sont pas établies : origine/sens des moments, repère de plate, hauteur de surface et calibration. Les seuls centresX/Y ne suffisent pas. Aucune division deM parFz présentée comme mesure de COP ; aucune force appliquée à un point de contact inventé.

Les forces ne sont pas des entrées de `reconstruct()` et ne peuvent donc pas déplacer un pied, un bassin ou un genou pour améliorer artificiellement la géométrie.
