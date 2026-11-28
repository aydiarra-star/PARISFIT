# Six facteurs : valeurs connues, recette non récupérée

**VALIDÉ :** valeurs et rôles généraux relus dans les fichiers épinglés. **EN ATTENTE DE DOCUMENTATION :** définition opérationnelle complète et application. **NON TESTÉ :** scaling, registration et IK. **REFUSÉ :** application par simple déduction du nom.

|Nom|S01|Unité|Rôle explicitement décrit dansREADME|Application exacte / certitude|
|---|---:|---|---|---|
|P1|1,07737|sans dimension|un des troisaxes du bassin|axeXML, référence et corps associés inconnus ; rôle général seulement|
|P2|1,08037|sans dimension|un des troisaxes du bassin|idem ; aucune assignationP2→Y|
|P3|1,08637|sans dimension|un des troisaxes du bassin|idem ; aucune assignationP3→Z|
|Fem|1,07018|sans dimension|fémur|isotropie, axe longitudinal, côtés et propagation auxjoints non établis|
|Tib|1,08885|sans dimension|tibia|corps affectés, couplages, translation desjoints et ordre non établis|
|Foot|1,14237|sans dimension|pied|répartitiontalus/calcn/toes, axes et règle d’application non établis|

Source commune : `../phase14/dataset-README.md` ; `participants.csv` SHA25664f61477376ef6ccea7d1ddb33f141a032e29566cae2122662e0e2fcda51049d dans archivev1 vérifiée. Valeurs machine dans `scaling-audit.json`. La noticeZenodo parle de facteurs du modèle scaled ; leREADME dit «surrogate scale factors». Conserver cette nuance plutôt que présumer unScaleSetOpenSim.

La documentation officielleOpenSim explique comment des facteurs manuels ou des distances entre marqueurs peuvent participer au scaling. Elle ne prouve pas quelle procédure les auteurs ont utilisée. En particulier, des valeurs positives plausibles ne déterminent ni les axes, ni le modèle de référence, ni la registration, ni les poids. Aucun calcul de longueur anatomique en multipliant les distances cutanées n’est autorisé.

## Suffisent-ils ? Non, dans l’état du dossier

Il manque le mapping officiel, le repère et le modèle/référentiel initial, leScaleSet ou algorithme d’application, les réglages des autres segments, la pose statique et la procédure de registration, le traitement des masses/inerties pour la dynamique. Demander aussi si ces six nombres paramètrent un surrogate musculaire plutôt qu’un redimensionnement complet et rejouable du squelette.

La masse64,9kg et la charge11,856kg sont documentées ; le brasMVC0,4317m n’est pas une longueur tibiale. La taille individuelle et les centres articulaires ne sont pas déduits des médianes de population. Masse et inerties ne sont pas indispensables au solveurIK purement cinématique ; elles le deviennent pour la dynamique. Une taille peut être remplacée par une procédure de scaling validée, pas par une supposition.

**EN ATTENTE DE VALIDATION HUMAINE :** un spécialiste doit examiner l’applicabilité et les incertitudes de toute procédure récupérée, même si le logiciel accepte ses paramètres.
