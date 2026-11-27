# Provenance, droits et modifications — phase 5

## Vidéo humaine C et dérivés

**FitnessScape — « Squat - exercise demonstration video »**, publié sur Wikimedia Commons le 19 mars 2025, extrait de « Half Rack Workout ». Licence **Creative Commons Attribution 3.0 Unported**.

- Source primaire et déclaration de licence : https://commons.wikimedia.org/wiki/File:Squat_-_exercise_demonstration_video.webm
- Licence : https://creativecommons.org/licenses/by/3.0/
- Auteur : https://www.youtube.com/@FitnessScapeFitness
- Vidéo originale citée par Commons : https://www.youtube.com/watch?v=0I6q9NqK9tM
- Miroir de transport GitHub utilisé (hôte autorisé du sandbox) : `HUSNAIN-MUNAWAR/motionforge-3d`, commit `970715decf7160f7d051236dcb59e49bbdde7ffe`, fichier `data/sample/wikimedia-squat/squat-exercise-demonstration.webm` ; blob `f9f7551ecc00c41ac1779c7d4a2c02272f35a139`.
- SHA256 des octets téléchargés : `2440985661c3533a4ce78472b0f4577dbdf023aff3f8f9a225bbb5ff8071b1e9`, identique à celui de la notice du miroir. Le fichier n’a pas été téléchargé directement depuis upload.wikimedia.org ; la provenance primaire et la notice du miroir ont toutes deux été consultées. Le SHA Git du blob est vérifié au téléchargement.

`source.webm` est conservé sans modification. `pose-overlay.mp4` ajoute les articulations estimées, un redimensionnement et une attribution visible, sans audio. `pose-estimates.json` contient les estimations brutes/filtrées locales ; `video-prototype.glb` et les vidéos C sont des adaptations expérimentales de l’extrait 0,8–2,5 s, avec estimation 3D, lissage, adaptation d’échelle/orientation et recalage vertical. Ces dérivés de mouvement sont proposés sous CC BY 3.0 avec crédit FitnessScape ; le modèle Rocketbox conserve sa licence MIT distincte. Aucun endossement de PARISFIT par FitnessScape, Wikimedia, Google ou CMU n’est suggéré.

CC BY 3.0 autorise partage/adaptation, y compris commerciale, sous attribution ; elle ne garantit pas les droits de personnalité, de marques ou un consentement publicitaire du sujet. **Aucune autorisation spécifique de la personne filmée pour PARISFIT n’a été obtenue.** Ce média public licencié sert à l’analyse technique dans le dossier de recherche ; il n’est ni une publicité ni une démonstration active de l’application. Toute exploitation promotionnelle/production nécessite une revue de droits distincte. Aucune vidéo personnelle ou client n’a été envoyée à un tiers.

## Mocap instrumentée D

**CMU Graphics Lab Motion Capture Database, sujet 22, essai 14 : alternating squats (2 subjects — subject A).** Capture optique, différente d’une estimation depuis vidéo.

- Catalogue primaire : https://mocap.cs.cmu.edu/search.php?subjectnumber=22&motion=14
- Conditions primaires consultées : https://mocap.cs.cmu.edu/ — données utilisables dans des produits commerciaux, **pas de revente des données seules, même converties**. Ce n’est pas du CC0 ou du domaine public.
- Conversion BVH par **Bruce Hahne (cgspeed), release 2010** : notice entière conservée dans `licenses/CMU-BVH-READMEFIRST.txt` ; première pose de calibration ajoutée par le convertisseur, explicitement exclue de l’extrait.
- Miroir : `una-dinosauria/cmu-mocap`, commit `09a07f54f3bbb58797325f009282d0b2048a2871`, `data/022/22_14.bvh`, blob `fd551a6b3e25d3a801f2de37ebb89aa2c8698083`.
- Modifications : extrait 0,7–1,7 s, échantillonnage 60 Hz, adaptation des directions osseuses au modèle Rocketbox, échelle déduite des longueurs de jambe, recalage au sol. Fichier BVH brut dans le cache, script de téléchargement reproductible ; GLB dérivé dans le dossier de recherche, non vendu comme animation autonome.

Acknowledgment: **The data used in this project was obtained from mocap.cs.cmu.edu. The database was created with funding from NSF EIA-0196217.** La source avertit que les orteils/mains peuvent être bruités et que doigts/pouces ne sont pas réellement capturés. Aucun geste de doigt mesuré n’est revendiqué.

## Outils et modèle

- Modèle Microsoft Rocketbox Sports_Male_04 : copyright Microsoft 2020, MIT, notice `../../../assets/coach/licenses/ROCKETBOX-MIT.txt`. Aucun remplacement ni modification de l’asset runtime.
- MediaPipe 0.10.21 : Apache 2.0, notice `licenses/MEDIAPIPE-APACHE-2.txt`. Modèle Pose Full embarqué dans cette distribution, empreinte dans `pose-estimates.json`. Ni poids ni modèle d’apprentissage redistribués séparément ici ; la licence de la distribution ne dispense pas d’une revue des composants avant une autre intégration.
- OpenCV headless, NumPy, FFmpeg via imageio, Pillow et Three.js : outils locaux de traitement/export ; versions exécutées dans `python-environment.txt`, Three 0.169.0 déjà présent et licencié dans le dépôt. Aucun code des projets de démonstration GitHub n’a été repris.
- Frais externes engagés : **0 €** ; aucun crédit ou abonnement consommé.
