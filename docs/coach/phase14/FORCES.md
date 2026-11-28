# Forces — analyse indépendante de toute IK

**VALIDÉ :** audit numérique des12composantes sur les3350samples deP001 et, séparément, les fenêtres de répétitions annotées. **EN ATTENTE DE VALIDATION HUMAINE :** repère des composantes, calibration, attribution aux pieds. **NON TESTÉ :** COP, contact anatomique, dynamique inverse, forces articulaires.

## Synchronisation et continuité

Temps marqueurs/forces égaux échantillon par échantillon ; cadence≈100Hz. Les12colonnes de force/moment sont finies. Cette cohérence des fichiers ne démontre ni le trigger matériel, ni l’absence de resampling ou retard physique. Aucun alignement optimisé, filtrage ou retiming appliqué.

L’analysePhase13 de corrélation entre accélération du proxy de bassin etFz total est conservée comme diagnostic, **pas mesure d’un délai instrumental** : bassin≠centre de masse complet avec haltère. Aucun décalage de20ms appliqué.

## P001 complet — pas seulement le cycle sélectionné

|Mesure|Plate1|Plate2|
|---|---:|---:|
|Fz min|237,8965N|206,5068N|
|Fz max|554,7300N|528,6187N|
|max√(Fx²+Fy²)|112,7635N|114,2088N|
|FramesFz≤10/20/50/100N|0 à chaque seuil|0 à chaque seuil|
|Transitions de chargement aux mêmes seuils|0|0|

P001 couvre10,45–43,94s et15répétitions annotées. La partFz1 sur toutP001 va de44,036% à60,572%, moyenne51,803% : ne pas généraliser la seule moyenne rep1 à toute la série.

Aucune perte de chargement détectée à ces seuils fixes dansP001. Ce n’est pas une preuve que la semelle entière reste au sol : un talon peut se lever tout en conservant la charge sur l’avant-pied. Les seuils sont des diagnostics de sensibilité, pas des normes cliniques. Le mot«horizontal» supposeZvertical ; orientation et calibration restent à confirmer.

## Répétition1 — cohérence avecPhase13

Fenêtre10,45–11,94s,150samples. Fz1=237,8965–554,4614N ; Fz2=230,5191–528,6187N. Plate1 représente45,674–57,060% deFz total, moyenne50,742%. Valeurs identiques aux calculsPhase13.

Fx1=36,1502–90,0457N ; Fx2=−85,8013 à−24,8385N. Fy1=−18,3994 à11,7122N ; Fy2=−14,7685 à14,5383N. DesFx de signes opposés peuvent être compatibles avec une stratégie d’appui, **mais ne prouvent pas une opposition physique tant que les deux repères ne sont pas qualifiés**. Ne pas sommer leurs composantes horizontales comme bilan mécanique certifié.

La partFz est une répartition **entre plates** ; droite→1/gauche→2 reste une hypothèse étayée par proximité des marqueurs aux centres documentés et par le protocole«une plate sous chaque pied», pas une identification par la force seule. Aucune position articulaire n’est déduite.

Les phases descente/bas/remontée sont établies par les annotations et les trajectoires de surfacePhase13, pas par un seuil de force ; chargement continu n’implique ni immobilité, ni stabilisation. Toutes les fenêtresP001 annotées ont leur audit séparé dans `force-audit.json`.

## Moments et COP

Mx/My/Mz sont audités numériquement, sans interprétation de moments articulaires. Absence de dimensions/altitude de surface et convention des repères/origines/signes : **COP NON TESTÉ**. Aucun point d’application n’est fabriqué et aucune force ne sert à améliorer la géométrie ou à faire passer une IK.
