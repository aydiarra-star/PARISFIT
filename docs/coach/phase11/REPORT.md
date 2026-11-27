# Phase11 — aucune animation admissible

**Décision : A/B/C REFUSÉS. Aucun candidat de reconstruction du squat n'est créé.** Les GLB produits sont des diagnostics isolés, jamais des animations admises. PR11 reste brouillon ; ni activation, fusion, déploiement, achat ni remplacement de Rocketbox. Le fichier runtime et les huit exercices restent inchangés.

## Résultats sur le même intervalle CMU

| Mesure | A direct | B morphologie/directions | C B + cinématique/appuis estimés |
|---|---:|---:|---:|
| Pénétration peau |277,957mm|9,066mm|8,656mm|
| Gap pied maximum |56,969mm|62,231mm|64,681mm|
| Dérive sur fenêtres candidates |5,798mm|7,522mm|2,701mm|
| Pic accélération |34,031m/s²|33,549m/s²|186,292m/s²|
| Vitesse maximale |1,452m/s|1,478m/s|1,650m/s|
| Pas articulaire maximum |24,197mm|24,640mm|27,501mm|
| Variation quaternion maximum |5,717°/frame|5,717°/frame|6,082°/frame|
| Accélération bassin |11,163m/s²|11,163m/s²|11,163m/s²|
| RMS des pivots face à source normalisée |187,152mm|216,032mm|216,177mm|
| Inclinaison tronc |113,702–126,461°|7,178–24,376°|7,178–24,376°|

Les rapports JSON fournissent ROM détaillées, estimations, seuils, comptages de contacts, source dynamique et hashes. Les tableaux HTML sont générés depuis ces rapports, sans valeurs saisies pour faire passer les critères.

**Important :** la dérive est mesurée sur des fenêtres candidates différentes (A2/37frames gauche/droite, B32/26, C24/21), non sur une annotation de contact commune. La réduction de dérive de C ne prouve donc pas à elle seule une amélioration de l'appui. Les activations IK de C, elles, utilisent la vitesse source et sont consignées séparément dans `inferredContactFrames` ; ne pas confondre les deux détecteurs.

## Conclusions causales limitées

1. Les directions nulles et les conventions de rotation sont des défauts réels du retarget A. Le changement B réduit massivement l'anomalie du tronc et du sol sans modifier les longueurs Rocketbox. Mais B combine plusieurs interventions ; pas d'attribution unique sans ablation dédiée.
2. B ne satisfait pas le seuil de sol3mm ni le budget d'accélération20m/s². Ses torsions axiales ne sont pas reconstituées par une direction de segment. L'erreur RMS des pivots augmente malgré un tronc plus plausible : ce score doit rester un proxy, pas un classement de qualité humaine.
3. C résout les objectifs géométriques à environ0,000284mm de résidu maximum et sans cible hors portée dans cette exécution. **Cela n'empêche pas un pic de186,292m/s².** L'ancrage à partir d'un seuil de vitesse faible seul est insuffisant ; les nombreuses entrées/sorties de fenêtres sont une cause plausible des discontinuités, pas une mesure de contact réel. Aucun lissage ajouté pour cacher le pic.
4. Bassin et timing sont maintenus identiques pour isoler les autres différences ; stabilité physique et récupération ne sont pas validées.

## Cartographie et mesures

Voir [inventaire des111os](anatomy.html) et [analyse par région](ANATOMY.md). Parentés, distances entre pivots, directions, matrices relatives de repos, unités et échelles sont explicités. Les22associations incluent deux directions impossibles et des correspondances approximatives. Aucun ratio inventé pour une longueur nulle. Les58os cible non pilotés et9os source non associés sont listés.

Le facteur global0,946989 ne résout ni l'écart des avant-bras (≈76–85mm après normalisation), ni les pieds (≈51–52mm), ni les subdivisions colonne/cou. Les os d'affichage créés par l'importeur ne constituent pas des mesures humaines.

## Limites bloquantes non résolues

- Axes anatomiques cliniques de hanche/genou/cheville/épaule/poignet non qualifiés ; torsions NON TESTÉES.
- Contacts, sol de capture et patches plantaires non annotés ; aucune force mesurée.
- Collision exhaustive des surfaces NON TESTÉE ; zéro paire de sphères suspecte ne signifie pas absence de collision.
- COM estimé avec masses arbitraires fixes, pas centre de masse mesuré.
- Préparation debout, position basse, retour et stabilisation doivent être annotés dans la source : aucune pause ou phase de récupération artificielle ajoutée. Aucun raccord vers les huit exercices.
- Déformations visibles, pédagogie, sécurité selon variante : EN ATTENTE DE VALIDATION HUMAINE. Les vidéos produites ne sont pas une revue.
- Capture PARISFIT toujours absente ; protocole de consentement inchangé.

## Preuves et reproductibilité

-145poses60Hz pour chaque méthode ;1clip/80os dans les trois exports ; comparaison Blender/Three.js des pivots et minima de peau.
- Chaque export répété deux fois avec égalité SHA256 ; A reproduit le GLB phase9/10 `fac4d26f57590f99951058c2532d6a96c4195cd8d39fbb797b35b19e3fcb7e7e`.
-7tests unitaires de géométrie/IK ; contrats et tests des phases précédentes conservés. Tests supplémentaires des données générées : entrées identiques, dimensions du rig, hash A et résidu IK sans admission.
-21films :7vues par méthode, cycle complet. Décodage intégral avec durées, frames et SHA256. Overlay : source rouge, recalage global fixe ; source affichée au sample60Hz le plus proche (écart temporel≤8,33ms), pas une vidéo humaine superposée.
- Artifact `phase11-anatomical-diagnostics` : galerie `index.html`, trois GLB de diagnostic, géométrie brute, source échantillonnée, rapports complets, inventaires matrices, licences et21films. Rétention30jours ; gros binaires hors Git.
- Tentative de téléchargement des8films phase10 échouée EOF ; aucune revue visuelle déclarée. Les artifacts phase11 sont accessibles sur GitHub, pas présentés ici comme fichiers récupérés.

`evidence.json` lie les rapports publics au commit et au job exécuté, avec SHA256. Les erreurs initiales CLI et matrices IK sont conservées dans `rejected-executions/`. Une correction de transport des annotations ne modifie pas les résultats cinématiques.

## Suite utile, sans admission implicite

Faire annoter les phases et vrais contacts sur une capture autorisée synchronisée, qualifier les axes anatomiques et les subdivisions de colonne, puis tester une préservation de contacts effectivement mesurés avec les mêmes métriques et la revue professionnelle. Ne pas prolonger le contrôle CMU en « capture PARISFIT ». La [grille professionnelle](PROFESSIONAL-REVIEW.md) reste non remplie.

### Accélération source : ne pas tout attribuer au retarget

Le calcul indépendant sur les22pivots source normalisés au même pas60Hz donne **32,166m/s²** maximum (LeftLeg), et11,163m/s² à la racine. A/B≈34/33,5 ne créent donc pas tout le pic à partir d'une source sans accélération. Ce sont des dérivées discrètes après conversion/rééchantillonnage, pas une mesure de forces ni une analyse du bruit du système optique original. Le budget20m/s² est un filtre technique conservateur de ce contrôle lent, pas une limite clinique : son dépassement ne prouve pas que le sujet CMU effectue un geste dangereux. C amplifie en revanche fortement cette dynamique. Aucun filtre ajouté pour faire passer la source ou la cible sous le seuil.
