# Reconstruction : trois hypothèses exposées, aucune vérité anatomique fabriquée

## Types de points

1. **Marqueur cutané mesuré/reconstruit par le système optique** :37trajectoires publiées. Mesure de surface, affectée notamment par tissus mous et placement.
2. **Centre articulaire estimé** : requiert modèle, calibration, régression ou essai fonctionnel ; **NON TESTÉ ici**. Aucun marqueur n'est renommé centre de hanche/genou/cheville.
3. **Segment reconstruit dans ce diagnostic** : ligne entre landmarks de surface ou points virtuels soumis à des contraintes de longueur. Il n'est pas l'os anatomique validé.
4. **Articulation cible Rocketbox** : pivot et axes de rig ; inchangés, aucune association exécutée tant que le point2 n'est pas qualifié.

## H0 — chaîne de landmarks cutanés

Bassin = moyenne deRight/Left ASIC etRight/Left sacral crest ; tronc = milieu des deuxacromioclavicular_joint ; tête =Skull_vertex. Pour chaque côté, chaîne greater_trochanter→lateral_epicondyle→lateral_malleolus→1st_metatarsal_head ; membre supérieur acromioclavicular_joint→olecranon→ulna_head. Ce sont des **proxies**. Le résidu nul face à ces mêmes marqueurs est tautologique, pas preuve anatomique.

## H1 — mêmes directions, longueurs issues du statique

Distances trochanter/épicondyle et épicondyle/malléole calculées entre positions médianes du statique. Hanche virtuelle ancrée au trochanter cutané dynamique ; genou et cheville virtuels reconstruits avec directions observées et longueurs fixes. Aucun centrage médial ajouté. Les positions s'écartent des marqueurs ; le résidu est publié. Une variation de longueur nulle est **imposée**, pas une validation.

Les directions de cuisse/jambe étant conservées, l'angle3points du genou est identique à H0 à l'arrondi près par construction. Cela ne constitue pas une confirmation indépendante. La direction tronc/cuisse peut changer selon les points utilisés.

## H2 — constellation pelvienne rigide + longueurs statiques

Fit rigide aux moindres carrés (Procrustes/Kabsch, SVD, déterminant+1) entre les quatrelandmarks pelviens statiques et dynamiques. Le trochanter statique est transporté avec cette constellation pour définir un **landmark virtuel**, jamais un centre de hanche. Puis même reconstruction des membres inférieurs que H1. RMS de rigidité pelvienne, résidus de markers et dynamique sont exposés.

L'hypothèse «trochanter solidaire du bassin» peut être fausse lors de la flexion, puisqu'il appartient au fémur. H2 sert précisément à quantifier l'effet d'une hypothèse de rigidité abusive possible. **Ne pas retenir le plus petit score comme choix de modèle.** Les membres supérieurs restent des chaînes de surface dans les trois variantes ; aucune torsion anatomique obtenue.

## Voie reconnue étudiée, non exécutée

Le dépôt fournit un modèle générique **LaiUhlrich2022_symmetric.osim**, décrit comme OpenSim4.6, avec37marqueurs annoncés et modifications de wrapping symétrique de certains muscles. `model-inspection.json` conserve corps, joints, coordonnées et attachements des marqueurs lus dans le XML, ainsi que les crédits disponibles. Le chargement/initSystem du template est VALIDÉ séparément dans `model-probe.json` (22corps,39coordonnées,66marqueurs, gravitéY−). Aucun ScaleTool, InverseKinematicsTool ou modèle individualisé n'est exécuté ici : l'inspection d'un template n'est pas une reconstruction biomécanique validée.

La méthode OpenSim de moindres carrés pondérés exige scaling et registration des marqueurs. Un faible résidu n'est pas suffisant : Dunne etal. montrent que l'erreur de registration peut modifier les angles malgré de faibles erreurs marqueurs [1]. L'étude clinique de localisation des hanches consultée décrit l'utilisation de mesures ASIS/PSIS pour certaines régressions [2] ; **ASIC et sacral crest ne sont pas automatiquement les points palpés requis**. Pas de régression de hanche appliquée à des repères non certifiés, ni de médian de genou inventé à partir du seul épicondyle latéral.

[1] https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0252425 — *A marker registration method to improve joint angles computed by constrained inverse kinematics* (2021).

[2] https://pmc.ncbi.nlm.nih.gov/articles/PMC12614639/ — *Can Predictive and Functional Methods Locate the Dysplastic Hip Joint Center?* ; source méthodologique, pas extrapolation clinique à S01.

## Dérivées, filtrage et incertitude

Dérivées discrètes non filtrées au pas mesuré≈0,01s ; accélération par seconde différence. Seconde différence RMS = proxy de haute fréquence, pas bruit optique. SD statique inclut oscillation réelle et tissus mous. Aucun filtre correcteur ni retiming ; aucun ajustement de géométrie par forces.

Sensibilité : décaler un seul endpoint de genou droit à la fois (hanche/genou/cheville proxies) de±10mm ou±20mm selon chacun des troisaxes du laboratoire ;18scénarios par amplitude. Le maximum publié est celui de ces scénarios, **ni erreur de mesure estimée, ni borne générale, ni intervalle de confiance95%**. On n'a pas de distribution d'erreur de centres articulaires.

Pour les angles : genou =180°−angle3points ; hanche =180°−angle(tronc,hip_proxy,knee_proxy), donc pas flexion anatomique dans un repère de bassin ; inclinaison tronc =angle(milieu épaules−proxy bassin, verticaleZ), pas décomposition sagittale/axiale.

## Porte Rocketbox

**NON TESTÉ**. H0/H1/H2 ne fournissent pas des centres/axes qualifiés. Pas de retarget, comparaison de qualité, ratio morphologique anatomique ou GLB supplémentaire. Comparaison sémantique seulement : trochanter cutané≠pivotThigh ; épicondyle latéral≠centreCalf ; malléole latérale≠pivotFoot ; moyenneASIC/sacrum≠Bip01_Pelvis. L'incompatibilité de définition précède toute recherche d'un bon score.

### Sensibilité indépendante au filtrage

`filter-sensitivity.json`, reproduit par `tools/michaud/filter_sensitivity.py` : moyenne glissante centrée1/5/9samples (10/50/90ms) sur les données d'affichage arrondies ; padding réfléchi, comparaison sur les140frames intérieures communes pour exclure les bords. Changements de position, angle de genou proxy et dérivées publiés. Aucun choix de filtre optimal, aucun résultat filtré injecté dansH0/H1/H2 ni retarget. Ce test mesure une dépendance numérique, pas un gain d'exactitude anatomique.
