# Seconde source précise — WBDS, qualification documentaire partielle

**EN ATTENTE DE VALIDATION HUMAINE :** candidate pour vérifier une méthode sur la marche. **REFUSÉ :** l’admettre comme squat de remplacement ou preuve d’exactitude anatomique. **NON TESTÉ :** trajectoires brutes, reconstruction et retarget. Aucun nouveau pipeline de mouvement lancé.

## Identité et version

Fukuchi, Claudiane ; Fukuchi, Reginaldo ; Duarte, Marcos. *A public data set of overground and treadmill walking kinematics and kinetics of healthy individuals.* **DOI10.6084/m9.figshare.5722711.v6**, publié2026-09-13, APIofficielle https://api.figshare.com/v2/articles/5722711/versions/6 consultée27novembre2026.

L’articlePeerJ2018 DOI10.7717/peerj.4640 décrit42sujets et citev2 ; la noticev6 annonce51sujets. Le protocole de l’article et le supplément sont une référence, **pas une garantie que chaque ajoutv6 est identique**. Épingler et vérifier le couple essai/statique avant usage.

## Ce qui est effectivement documenté

- **Marqueurs/anatomie :** Fig1, Methods et supplément officiel DOI10.7717/peerj.4640/supp-1, Table1 effectivement lue.28labels statiques avec sites anatomiques ;22en dynamique après retrait bilatéral des marqueurs médiaux du genou, médiaux de cheville etMT2. Statique1s, pieds alignés avecX du laboratoire ; acquisition150Hz pour marqueurs et300Hz pour forces.
- **Modèle associé :** `WBDSmodel.mdh`, fichierVisual3D fourni dans le dataset. Partie consultée : pelvisCoda défini parASIS/PSIS, cuisse viaGTR/hip/knee/medial knee, jambe suivie parankle/HF/TT, pied parHEEL/MT1/MT5. C’est un modèleVisual3D, **pas un.osim prêt à utiliser**.
- **Mouvement :** marche pieds nus, sol/tapis à plusieurs vitesses, statiques et donnéesC3D/ASCII annoncés ; pas de squat chargé.
- **Unités/repères :** article : forcesN, COPmm, moment libre verticalTy enN·m ; pieds statiques selonX. ParamètresC3D, unitéPOINT et transformations/export signées de l’essai exact restent à contrôler avant conversion. Ne pas remplacer arbitrairementTy parMz. AucunCOP nouveau calculé.
- **Métadonnées :** description des champs taille/masse/longueur de jambe, choixStatic1/Static2, pied↔plate, mains sur rambardes et notes d’offset. Ces notes doivent faire partie de la sélection, pas être ignorées.

### Points à clarifier avant admission

Le supplément nommeR.Knee.Medial etL.Knee.Medial, mais les descriptions des lignes11/21 écrivent «most medial prominence of the ... lateral femoral epicondyle». **Ambiguïté textuelle conservée, pas corrigée silencieusement.** Vérifier auprès des auteurs/du protocole avant d’utiliser ces points comme référence anatomique.

Différence de labels/casse entre la table et les références du modèle (p.ex.R.Heel.Bottom etR.HEEL), évolutionv2→v6, coefficients et métriques par défaut duMDH : validation de correspondance encore nécessaire. Les valeursMass66/Height1.66 visibles dans le modèle ne sont pas automatiquement celles d’un essai choisi. Première partie duMDH seulement consultée, modèle non exécuté. L’usage manuelVisual3D peut nécessiter une licence distincte ; **aucun achat**. Une réimplémentation gratuite éventuelle exige une validation numérique indépendante, pas un renommage de fichiers.

## Licence du dataset précis et conditions commerciales

L’API de **v6 elle-même** indique **CC BY4.0** pour les fichiers du dépôt, dontMDH, pipeline, C3D/ASCII ; ce n’est pas seulement la licence de l’article. La licence permet partage et adaptation, y compris commerciaux, sous attribution, lien de licence et indication de modifications, sans suggérer un endorsement ni ajouter des restrictions incompatibles. [TexteCC BY4.0](https://creativecommons.org/licenses/by/4.0/legalcode.en). Les droits de personnalité, marques et licences des logiciels ne sont pas automatiquement accordés. Revue juridique finale EN ATTENTE DE VALIDATION HUMAINE, pas avis juridique.

Citation à conserver : auteurs, titre, DOIversionv6 et articlePeerJ6:e4640 ; mentionner les transformationsPARISFIT et les limites. Pas d’exception de licence signalée dans la notice pourMDH ; vérifier notices internes et fichiers réellement acquis avant redistribution. Aucun matérielWBDS redistribué ici, seulement références et constats d’audit.

### Fichiers épinglés — hashes publiés, pas recalculés

|Fichier de v6|IDFigshare|Taille|MD5 publié|
|---|---:|---:|---|
|WBDSmodel.mdh|11341412|28691octets|49e01170d916fff32f855d89794d7ee2|
|wbdsOvergroundDA.v3s|10058989|26214octets|780b97ca17f2117ba6507b0cde7347c6|
|WBDSc3d.zip|68193898|817730490octets|426a26bf3718cddd9f3bfe68437cb553|
|WBDSascii.zip|68194516|686716664octets|75d2be58331b3a0610b478572929651f|

Téléchargements stables : `https://ndownloader.figshare.com/files/ID`. Archives volumineuses **non acquises** dans cette phase de planification ; aucune identité de sujet/essai sélectionné inventée. La première qualification ultérieure doit choisir un seul essai et son statique lié, vérifier fichiers/hashes/labels/repères/notes et droits avant touteIK. Les courbes moyennes101points ne remplacent pas une capture chronologique complète.

## Comparaison et recommandation

|Voie|Avantage|Limite actuelle|Décision|
|---|---|---|---|
|MichaudS01/P001v1|Squat chargé et forces, données analysées|Mapping, placement, repères et scaling manquants|EN ATTENTE DE DOCUMENTATION ; demande bilingue prête|
|WBDSv6|Protocole/MarkerSet/supplément et modèle associé, licence précise|Marche, modèleVisual3D, ambiguïtés ci-dessus, essai non inspecté|Candidate méthodologique ; NON TESTÉ pour reconstruction, aucun retarget|
|AddBiomechanics générique|Plateforme avec modèles/données agrégés|Aucun nouvel essai précis/provenance qualifiéPhase15 ; ne pas déduire la qualité d’un upload de la plateforme|Non retenu comme source qualifiée ; étatPhase12 conservé|
|Nouvelle acquisition encadrée|Protocole et droits définissables avant capture|Professionnel, consentement, calibration et accès aux appareils nécessaires|EN ATTENTE DE VALIDATION HUMAINE ; pas de réservation/achat|

**Priorité :** obtenir les métadonnéesMichaud. Si impossibles à récupérer, qualifierWBDS pour la méthodologie seulement ; pour un squat coach crédible, privilégier une nouvelle acquisition documentée plutôt qu’une transposition de marche.
