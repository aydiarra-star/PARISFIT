# Critères proposés pour une future expérimentation

**Aucune admission dans cette phase.** Les critères ci-dessous distinguent contrôles exacts de traçabilité, métriques à mesurer ultérieurement et tolérances professionnelles encore à définir. Un dossier prêt pour expertise ne signifie pas un mouvement qualifié.

## Principes de décision

1. Pas de seuil universel de «bonne biomécanique».
2. Fixer les critères, leur domaine d’application et les motifs d’exclusion **avant** les futurs calculs. Ne pas les ajuster pour accepter le résultat.
3. Une moyenne globale ne remplace pas un contrôle par marqueur, région, degré de liberté et phase.
4. Séparer seuil de détection et seuil d’admission ; une charge détectée ne valide pas un contact plantaire complet.
5. Si une information essentielle est inconnue ou une condition non levée, ne pas admettre automatiquement l’essai.

## Six dimensions séparées

|Dimension|Contrôle mesurable proposé|Référence / justification|Valeur d’admission actuelle|
|---|---|---|---|
|Qualité des données sources|SHA256, nombre de frames, labels, unités, fréquences, lacunes et historique d’interpolation|Manifest officiel épinglé, paramètresC3D et spécificationC3D ; contrôles d’intégrité, pas preuve anatomique|Égalité des hashes et comptes de référence ; historique des lacunes encore requis|
|Cohérence anatomique|Statut de chaque site et centre, offsets, axes, résidus statiques individuels, sensibilité aux choix de registration|Protocole publié, XML et revueQ1–Q3 ; modèle de peau différent de l’os|**Aucun seuil métrique fixé** ; tolérances par région à justifier par l’expert|
|Stabilité des appuis|Continuité des forces, affectation pied/plateforme, déplacements dans les phases réellement en appui, COP et incertitudes|Article NotreDame et revueQ4 ; distinguer appui chargé et contact complet|20N seulement comme seuil de segmentation rapporté par les auteurs, **pas seuil d’admission** ; tolérances de glissement/hauteur non définies|
|Qualité cinématique|Erreurs par marqueur et phase, contraintes, amplitudes, vitesses, accélérations, observabilité, départ/retour|RevueQ2/Q5, comparaison pertinente pour le mouvement et le sujet ; pas seulement résidu global|Aucune bande normative chiffrée retenue pourAB01 ; méthode et tolérances à faire approuver|
|Fidélité du transfertRocketbox|Différences de temporalité, orientation, proportions, appuis et amplitudes entre source qualifiée et avatar|RevueQ6 et définition explicite des invariants de transfert ; rig de personnage non assimilé à une anatomie|**NON TESTÉ**, aucun mapping admis, aucune tolérance inventée|
|Qualité visuelle et naturelle|Revue continue du cycle, trois vues, vitesse normale/ralentie, entrées/sorties et collisions visibles|Évaluation humaine indépendante avec grille explicite ; preuve perceptive distincte de la validité anatomique|Aucun score ou note arbitraire ; aucune nouvelle vidéo produite ici|

## Nombres utilisables — périmètre précis

- **200Hz /1000Hz, ratio5:1** : paramètres du fichier et fréquences publiées. Ce sont des spécifications de lecture à vérifier, pas une garantie de synchronisation matérielle.
- **2948/1565 frames** : comptes physiques etPOINT:FRAMES ; égalité déterministe, pas seuil biomécanique. La propriété calculée du lecteur ne doit pas être substituée à l’en-tête brut.
- **20N** : seuil de contacts rapporté dans la méthode des auteurs ; le diagnostic phase17 a utilisé la magnitude duFzlocal brut. Ce n’est pas une reproduction du traitement après import/filtrage, ni la preuve d’une sole entièrement posée.
- **4,21±0,34cm et9,82±0,74cm** : erreurs de marqueurs des modèles statiques rapportées. **Ni seuils d’acceptation ni valeurs d’AB01**.
- **accuracy=1e-5** : tolérance numérique déclarée du solveur dans le setup, pas une précision anatomique prouvée.
- **46fixed=false /11absents** : paramètres documentés/inconnus, pas une autorisation de déplacer les marqueurs.

Aucune valeur de seuil supplémentaire (degrés, centimètres, vitesse ou score visuel) n’est proposée faute de justification spécifique. L’expert devra renseigner : métrique, valeur, unités, population/mouvement, référence ou raisonnement professionnel, fenêtre de mesure, incertitude, exceptions et procédure de contestation.

## Conditions cumulatives avant préparation d’une expérience

- Droits des données et composants nécessaires établis ; versions et hashes figés.
- Q1–Q5 examinées, contradictions essentielles résolues ou limites acceptées **explicitement** ; aucun avis implicite déduit d’un silence.
- Fonctions modifiées, configurations effectives, timing et registration suffisamment traçables ; résidu statique individuel examiné selon une méthode connue.
- Critères et analyse de sensibilité écrits avant calcul, protocole de conservation des résultats négatifs défini.
- Revue indépendante obtenue et autorisation explicite de l’utilisateur pour une phase ultérieure strictement bornée.

Ces conditions n’autorisent pas l’intégration ou l’activation. Transfert, rendu du cycle complet, revue visuelle, tests physiques sur appareils et validation professionnelle du coach sont des étapes ultérieures séparées.

## Sources

[Article NotreDame, Methods/Data Processing/Technical Validation](https://pmc.ncbi.nlm.nih.gov/articles/PMC12717423/), [C3D POINT:FRAMES](https://www.c3d.org/HTML/Documents/pointframes1.htm), [C3D Synchronization](https://www.c3d.org/HTML/Documents/datasynchronization.htm), [configurations inspectées](../phase17/configuration-inspection.json), [analyse du RMS](../phase17/rms-scaling-error-analysis.md). L’article ne fournit pas de seuil numérique d’acceptation du squatAB01 ; aucune norme générique n’est présentée comme son critère.
