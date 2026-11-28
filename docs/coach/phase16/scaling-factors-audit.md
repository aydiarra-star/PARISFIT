# Audit des six facteurs — application NON TESTÉE

Consultation du 27 novembre 2026. **VALIDÉ :** valeurs relues dans la preuve originale S01. **EN ATTENTE DE DOCUMENTATION :** application exacte. Aucune valeur n’a été appliquée.

Source : [README original](../phase14/dataset-README.md), [inspection originale](../phase14/original-audit.json), `participants.csv` SHA256 `64f61477376ef6ccea7d1ddb33f141a032e29566cae2122662e0e2fcda51049d`, archive SHA256 `901112330ed234ad97ce24cb866bd5e7e33bef766861d21264953b3ac1875782`. Réexamen des preuves acquises en phase14, pas nouveau téléchargement annoncé.

|Facteur|Valeur S01|Unité|Ce que le README établit|Axe/corps et procédure officielle|
|---|---:|---|---|---|
|P1|1.07737|sans dimension|facteur d’un axe du bassin|ordre des axes non spécifié ; ne pas assigner X|
|P2|1.08037|sans dimension|facteur d’un axe du bassin|ordre non spécifié ; ne pas assigner Y|
|P3|1.08637|sans dimension|facteur d’un axe du bassin|ordre non spécifié ; ne pas assigner Z|
|Fem|1.07018|sans dimension|fémur|corps/côtés, anisotropie/isotropie, géométrie de référence et propagation aux joints non établis|
|Tib|1.08885|sans dimension|tibia|corps/côtés, axes, règle de scaling et ordre non établis|
|Foot|1.14237|sans dimension|pied|répartition talus/calcn/toes, axes et règle de scaling non établis|

Le README parle de «six surrogate scale factors», tandis que la notice parle de facteurs du modèle scaled. Cette nuance motive la question3, pas une interprétation automatique. Les identifiants de corps existent dans le XML, mais leur existence ne confirme pas les correspondances aux colonnes. P1–P3 ne sont pas une largeur absolue du bassin ; Fem/Tib ne sont pas des longueurs mesurées.

## Recherche de la procédure

L’endpoint officiel [latest](https://zenodo.org/api/records/23979972/versions/latest), relu dans cette phase, retourne toujours record23979972, revision4, modification2026-11-05T12:57:28.048468. Pas de nouvelle procédure trouvée dans cette réponse. Le manifeste épinglé de290fichiers ne contient pas de setupScaleTool/IK. La documentation officielle [OpenSim Scaling](https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/pages/53089123/Getting+Started+with+Scaling), consultée en phase15, décrit les mécanismes généraux mais n’autorise pas une interprétation des colonnes Michaud.

**Non récupérés :** référence du scaling, affectation axes/corps, ordre d’opérations, traitement des autres segments, règle des masses/inerties, registration et éventuels ajustements manuels. La masse64,9kg et l’haltère11,856kg sont connus ; le brasMVC0,4317m n’est pas la longueur du tibia. Masse/inerties ne sont pas indispensables à l’IK pure, mais le deviennent pour une dynamique inverse.

**Conclusion B :** valeurs et rôles généraux vérifiés, méthode insuffisamment documentée. Les questions2–4 de la demande finale ciblent ces pièces. Les fichiers de scaling d’une autre étude ne peuvent pas calibrer S01.
