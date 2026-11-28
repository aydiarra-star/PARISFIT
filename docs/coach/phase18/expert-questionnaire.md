# Questionnaire et fiche de retour — vierges

**Aucun avis obtenu.** Merci de distinguer validation d’une définition documentaire, validation d’une méthode et validation d’un mouvement. Une réponse favorable n’autorise ni activation dansPARISFIT ni présentation comme coaching sûr.

## Identification et périmètre

Relecteur / qualification / organisme : **à renseigner**.
Date / conflits d’intérêts / indépendance vis-à-vis de l’étude : **à renseigner**.
Versions examinées : sourceWeRoLab`a26fe4852a78f30c5e8a437b158847031cb8dc3c` ; version du dossierPARISFIT et hashes : **à confirmer**.
Fichiers effectivement examinés / non accessibles : **à lister**.
Nature de l’avis : documentaire, biomécanique, acquisition ou autre : **à préciser**.

Pour chaque question, choisir exactement une réponse, ou laisser vierge si non examinée :

- **Validé** — préciser la proposition exacte et ses limites.
- **Validé sous conditions** — conditions vérifiables, pièces requises, responsable et échéance.
- **Non validé** — défaut, conséquence et preuve.
- **Impossible à déterminer** — information manquante et moyen éventuel de la recueillir.

Une case vierge n’est pas «validé». Une condition non levée n’est pas une admission. [Modèle JSON exportable](expert-feedback-template.json) : toutes les réponses et identités sont nulles, aucun envoi automatique.

## Q1 — Les repères anatomiques sont-ils correctement interprétés ?

Examiner [M01–M57](anatomical-uncertainties.md), en priorité IAS/IPS, TV2, HM2, USP/RSP etSK. Déterminer la latéralité et les signes du bassin ; ne pas corriger les alias par simple intuition ou symétrie. Pour chaque contestation, citer le label et la preuve individuelle, ou indiquer que celle-ci manque.

**Réponse :** à renseigner. **Labels acceptés / refusés / indéterminés :** à lister.
**Preuves, contradictions restantes et conséquences :** à renseigner.

## Q2 — Les marqueurs permettent-ils une estimation suffisamment fiable des articulations ?

Quelles méthodes de centre/axe sont justifiées pour la hanche, le genou, la cheville, l’épaule et le poignet ? Quels degrés de liberté sont observables ? Que change le retrait de huit marqueurs de calibration ? Quels effets des tissus mous et rattachementsFTC→pelvis, HGT→torso, USP→radius, DP1→calcn doivent être bornés ?

Ne pas confondre la définition du squeletteMotive avec les articulationsOpenSim. Aucun milieu de paire n’est calculé ici.

**Réponse :** à renseigner. **Articulations, méthode et incertitudes :** à renseigner.
**Preuves ou pièces manquantes :** à renseigner.

## Q3 — Le scaling est-il cohérent avec la morphologie d’AB01 ?

Examiner masse49,81kg, stature1,73m documentée séparément, neuf mesures actives, groupes bilatéraux et axesXYZ locaux. Les corps non explicitement ciblés, les six coordonnées verrouillées, la registration et les onze champsfixed absents sont-ils défendables ? Quels logs individuels sont nécessaires ?

Les4,21cm publiés sont une moyenne globale, pas l’erreur d’AB01. Aucun facteurS01 de Michaud ne doit être utilisé.

**Réponse :** à renseigner. **Mesures/segments concernés :** à renseigner.
**Tolérances proposées et justification scientifique ou professionnelle :** à renseigner, sans seuil universel présumé.

## Q4 — Les forces sont-elles exploitables pour analyser les appuis ?

La chaîne plateforme→C3D→OpenSim, les signes, origines des moments, COP et synchronisation sont-ils assez documentés ? Que permet réellement une magnitudeFz supérieure à20N ? Quels effets du filtrage et quelles preuves supplémentaires sont nécessaires pour distinguer charge, talon levé, glissement et contact complet ?

Lire [l’erratumC3D](c3d-integrity-and-timing.md) : en-tête brut cohérent, dépassement dû au lecteur inspecté ; aucune réparation effectuée.

**Réponse :** à renseigner. **Analyses permises / interdites :** à préciser.
**Preuves temporelles et métrologiques manquantes :** à renseigner.

## Q5 — Peut-on défendre une reconstruction biomécanique de ce squat ?

Au regard desQ1–Q4, quelle conclusion est soutenable pour cette prise seulement ? Quelles incertitudes sur les phases, amplitudes, résidus individuels et stratégie motrice empêchent une reconstruction défendable ? Quels résultats permettraient de falsifier l’hypothèse d’une reconstruction correcte ?

**Réponse :** à renseigner. **Usage admis : recherche / démonstration / aucun / autre à préciser.**
**Limites, critères préalables et contre-preuves recherchées :** à renseigner.

## Q6 — Quelles vérifications avant un transfert vers un personnage3D ?

Quels contrôles des pivots, proportions, repères de repos, degrés de liberté, temporalité et appuis seraient nécessaires pourRocketbox ? Comment séparer fidélité de la capture et naturalité visuelle ? Quelle revue continue sous trois vues, à vitesse normale et ralentie, serait nécessaire après une future phase autorisée ?

Aucun transfert, vidéo nouvelle ou animation générée dans cette phase. Les huit exercices existants ne sont pas validés par ce questionnaire.

**Réponse :** à renseigner. **Liste des contrôles et responsables :** à renseigner.
**Autorisation d’expérimentation :** décision distincte de l’utilisateur, absente à ce stade.

## Synthèse contradictoire à remplir

|Point|Avis parmi les quatre choix|Justification / preuve|Conditions précises|Vérification de levée|
|---|---|---|---|---|
|Q1 Repères|—|—|—|—|
|Q2 Articulations|—|—|—|—|
|Q3 Scaling|—|—|—|—|
|Q4 Appuis/forces|—|—|—|—|
|Q5 Reconstruction|—|—|—|—|
|Q6 Transfert futur|—|—|—|—|

Désaccords non résolus / besoin d’un deuxième avis : **à renseigner**.
Conclusion signée et datée : **NON OBTENUE**. Publication ou transmission de l’avis : seulement après autorisation appropriée. Aucun nom d’expert ni approbation prérempli.
