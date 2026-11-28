# Diagnostic des conventions squelettiques

## Lire les données sans inventer l'anatomie

`anatomy.html` et `anatomy-summary.json` donnent tous les31os CMU et80os Rocketbox : nom, parent/enfants, position de repos mondiale, distance parent/enfant, axes mondiaux, matrice de repos relative au parent, matrice/échelle objet. Le fichier intégral `A/anatomy.json` de l'artifact ajoute la matrice de repos absolue de chaque os et la pose artificielle source0 (positions et quaternions).

Le BVH ne déclare pas une unité SI fiable : l'import applique le facteur historique explicite0,056444 vers le mètre, axes−Z/Y ; aucune calibration physique nouvelle revendiquée. Source et cible sont évaluées en Blender Z-up ; les rapports indépendants sont convertis en Y-up par `(x,z,−y)`. Échelles objet importées `[1,1,1]` ; ce résultat ne signifie pas que les proportions des deux corps sont égales.

Les axes présentés sont **axes de rig**. Une longueur graphique Blender ou une queue artificielle créée à l'import ne remplace jamais une distance exploitable entre deux pivots. Un ratio absent reste `null`, pas0 ni une longueur estimée.

## Correspondances problématiques

- **Bassin Hips→Pelvis** : Hips→LowerBack est nul, contre120,27mm Pelvis→Spine. Aucun vecteur normalisé anatomique valide à transférer. Les branches source LHipJoint/RHipJoint sont aussi coïncidentes avec Hips ; elles ne mesurent pas une largeur de bassin. La vraie largeur entre pivots UpLeg est distincte.
- **Colonne** : LowerBack→Spine et Spine→Spine1 mesurent environ117,6/117,7mm avant normalisation, contre153,2mm pour chacun des segments cible. Spine1→Neck source est nul, contre199,75mm Spine2→Neck cible. Il n'existe pas une bijection de vertèbres anatomiques. Les os auxiliaires et les58os cible non pilotés ne doivent pas servir à inventer un rachis capturé.
- **Cou/tête** : le mapping Neck→Head saute la subdivision Neck1 source. Son segment agrégé187,38mm ne correspond pas au segment cible69,27mm. Head est un label de pivot ; aucune longueur humaine supplémentaire n'est inférée.
- **Hanches/cuisses/genoux** : UpLeg→Leg→Foot a une topologie exploitable. Mais les longueurs source sont asymétriques ; le facteur0,946989 calculé seulement sur la jambe gauche n'ajuste pas exactement la droite. Les directions ne calibrent ni valgus ni axes de flexion/rotation.
- **Chevilles/pieds** : Foot→ToeBase source≈125mm contre Foot→Toe0 cible170mm ; après normalisation, déficit d'environ51–52mm. Le pivot de cheville et l'extrémité d'orteil ne sont pas une surface de semelle. Les groupes de peau sont des proxies, pas des contacts mesurés.
- **Épaules/clavicules** : LeftShoulder/RightShoulder sont coïncidents avec Spine1 ; la branche vers Arm est exploitable comme direction mais représente une convention différente de la clavicule cible. Après normalisation, résidus≈−53,5/−48,4mm. Pas de reproduction attestée du mouvement scapulaire.
- **Coudes/avant-bras** : Arm→ForeArm ressemble en longueur à la cible après normalisation ; ForeArm→Hand beaucoup moins (résidus≈+84,7mm gauche,+76,3mm droite). Une même trajectoire de poignet et une même rotation de coude ne peuvent être imposées indépendamment avec ces longueurs sans compensation.
- **Poignets/mains/doigts** : le pivot Hand existe, mais FingerBase et Thumb sont coïncidents avec lui. Blender signale des os d'affichage sans longueur lors de l'import des mains. Aucune longueur ni torsion anatomique de main ne peut être déduite de ces branches nulles. Les doigts Rocketbox non mappés héritent de leurs parents et restent en rotation locale de repos : ils ne sont pas capturés.

La table des22associations classe `direct-topology` (8segments de membres), `approximate` et `impossible-direction` (2). « Direct » signifie topologie de chaîne, pas validation anatomique. Les58os cible non pilotés et9os source non utilisés sont listés explicitement dans l'inventaire. Ni os auxiliaire ni subdivision ne sont silencieusement renommés en articulation humaine.

## Pourquoi A échoue et ce que B isole

Dans A, la formule est `H × Q(t) × inverse(Q(0)) × offset × cibleRepos`. Même au temps de référence, l'offset statique et le heading subsistent ; l'offset de direction est indéfini pour les segments nuls. Ce n'est pas un transport de delta qui garantit l'invariance de repos. L'inclinaison du tronc mesurée114–126° est compatible avec une erreur de conventions, pas une preuve de mouvement humain fidèle.

B évite les offsets nuls et utilise une conjugaison du delta pour le tronc, puis des directions de segments pour les membres en conservant leurs longueurs natives. Le tronc devient≈7–24° et la pénétration descend à≈9mm. Cela apporte une preuve expérimentale que les conventions d'orientation comptent fortement. **Pas une preuve que B est anatomiquement correct**, ni une attribution causale unique : B modifie plusieurs aspects, perd la torsion des directions de membres et reste sans calibration anatomique.

## Pourquoi C ne suffit pas

Une chaîne géométrique à deux segments peut atteindre sa cible à faible résidu tout en étant dynamiquement mauvaise. Le changement discontinu entre objectif libre et cheville ancrée sur un contact seulement supposé peut créer un pic d'accélération. Les contacts doivent être annotés/mesurés avant d'être préservés, pas déduits d'une vitesse faible seule puis « validés » par l'immobilité produite. La version testée de C est donc une expérience négative, pas un contrôle d'appuis prêt pour PARISFIT.
