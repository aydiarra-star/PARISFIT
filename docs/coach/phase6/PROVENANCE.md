# Sources et droits — phase 6

Source primaire : CMU Graphics Lab Motion Capture Database, https://mocap.cs.cmu.edu/ et https://mocap.cs.cmu.edu/faqs.php (conditions vérifiées phase 5). Usage recherche et produits commerciaux permis ; copie/modification/redistribution permises ; **interdiction de revendre les données seules, même converties**. Ce dossier n'est pas une banque de données à revendre. Pas de garantie de qualité ni d'endossement.

Description primaire vérifiée le 27 novembre 2026 : https://mocap.cs.cmu.edu/search.php?subjectnumber=14&motion=%25 — sujet 14, essai 6 « jumping jacks, jog, squats, side twists, stretches », 120 Hz. Extrait choisi dans le BVH : 8,6–11,0 s, premier squat profond complet retenu. La première frame de calibration ajoutée par le convertisseur implique un possible décalage d'une frame avec l'AMC. Le fichier complet de 44,64 s est conservé, sans réécriture. L'absence d'accessoires gênants n'a **pas** été confirmée par vidéo : seule la hiérarchie articulaire a été examinée. Les appuis restent incertains.

Distribution BVH : Bruce Hahne / cgspeed 2010, miroir https://github.com/una-dinosauria/cmu-mocap à la révision `09a07f54f3bbb58797325f009282d0b2048a2871`, `data/014/14_06.bvh`. Identifiants Git blob et SHA256 dans `provenance.json`, vérifiés sur les octets originaux. `source-22_14.bvh` conserve aussi l'essai précédent ; son retargeting négatif est documenté séparément. Ce sont des données issues d'une capture optique instrumentée, **pas** une estimation vidéo. Les BVH sont des conversions de la capture ; ni les marqueurs bruts ni les forces au sol ne sont présents.

Modèle : Microsoft Rocketbox Sports_Male_04, MIT, copyright Microsoft 2020 ; licence conservée dans `assets/coach/licenses/ROCKETBOX-MIT.txt`. Pas de remplacement du modèle runtime. Three.js MIT ; aucun service payant, aucune vidéo personnelle envoyée.

Attribution demandée : “The data used in this project was obtained from mocap.cs.cmu.edu. The database was created with funding from NSF EIA-0196217.”

Ces permissions de données ne constituent ni une autorisation d'endossement, ni un avis professionnel, ni une validation médicale. Pour une nouvelle capture PARISFIT, utiliser l'autorisation explicite du participant avant tournage (modèle phase 5).
