# Phase19 — tests techniques, aucune validation biomécanique

- `npm test` : PASS (contrats existants, huit exercices et preuve documentaire).
- `.venv/bin/python tools/independent-review/test_review.py` : PASS,8 tests de contrat/fixtures ; pas de nouvel audit réel phase18.
- `LD_LIBRARY_PATH=/tmp/al2023/lib CHROMIUM_PATH=/tmp/chromium node tests/smoke.cjs` : PASS.
- Même environnement, `node tests/coach-browser.cjs` : PASS (huit exercices existants, contrôles, largeurs320–1200, hors ligne). Pas une validation de trajectoires nouvelles ; aucune animation modifiée.
- `.venv/bin/python tools/evidence-closure/test_closure.py` : contrôle livrables/liens/registre/logs/empreintes ; résultat dans [preservation-check.json](preservation-check.json).
- Probe officiel passif run46118632585 : PASS ;2 journaux récupérés,1876836 octets transférés par plages. Aucun contenu téléchargé exécuté.

Les logs locaux de tests sont archivés dans `test-output.txt`. Les téléphones physiques et l'avis professionnel ne sont pas couverts. La CI de validation générale peut être en cours au moment de rédaction ; son état observé est conservé séparément, sans inventer de PASS. Les4 jobs authoring doivent être **skipped**, non comptés comme tests réussis.
