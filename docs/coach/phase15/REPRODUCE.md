# Reproduction et traçabilité

**VALIDÉ uniquement pour calculs/tests techniques.** La recherche documentaire ne peut être reproduite comme une garantie d’absence de documents : son périmètre et ses dates sont dansINVENTORY.md.

Depuis la racine, Python3+NumPy :

```
python3 tools/metadata-plan/analyze.py
python3 tools/metadata-plan/test_plan.py
python3 tools/metadata-plan/build.py
npm test
```

Les facteurs sont lus depuis la preuve originalePhase14, sans transformation ni application. L’observabilité utilise les données d’affichagePhase13 arrondies à6décimales, statique médian et150framesrep1. Le script enregistre leurSHA256. Il calculeJ=[I,−skew(p−centre)] avec tolérance de rang1e−10 ; pas d’optimisation, scaling ouIK. Ce rang local, dépendant de la géométrie et de la tolérance, ne mesure ni l’incertitude du capteur ni la précision anatomique. Les groupes et hypothèses sont explicites dans le code. Tests synthétiques : point/ligne/triangle, invariance à la translation, absence d’admission.

`build.py` construit la page et le manifesteSHA256 des livrables. Les testsNode contrôlent le manifeste, valeurs inchangées, statuts, non-envoi, non-admission et hash du runtimeRocketbox. Les preuvesPhase14 restent intactes ; pas de nouvelle acquisition duZIPMichaud annoncée.

Test navigateur (serveur statique sur port3000, Chromium disponible) :

```
node tests/coach-metadata-plan-browser.cjs
python3 tools/metadata-plan/build.py
```

`CHROMIUM_PATH` optionnel ; vérifie les deux messages développés, liens locaux, absence de débordement à320/390/768/1200px. Produitbrowser-report.json, puis le manifeste est rafraîchi. Ce test n’est pas une revue professionnelle ni un essai sur téléphone physique.

Les fichiersWBDS sont identifiés par leurversion/ID et MD5 **publié** ; aucune vérification binaire locale ou lecture des archives de mouvement revendiquée. Les URLs et les sections consultées permettent de renouveler cette qualification documentaire avant acquisition d’un essai. Aucun script de cette phase n’envoie de message, n’effectue de paiement, n’exécute d’IK ni ne modifie le coach.
