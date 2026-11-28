# Reproduire les contrôles sans modifier les animations

Environnement utilisé : Node22, Playwright1.65.1, Chromium disponible via CHROMIUM_PATH=/tmp/chromium et bibliothèques via LD_LIBRARY_PATH=/tmp/al2023/lib ; Python de `.venv`. Ce sont les outils du sandbox, pas une matrice de téléphones physiques.

- Serveur statique du dépôt sur0.0.0.0:3000 ; tests smoke.cjs et coach-browser.cjs avec BASE_URL adapté. Aucun endpoint tiers nécessaire au runtime.
- Serveur isolé de cycleSW : `node tools/consolidation/cache-server.cjs` (3011). Garder ce processus actif uniquement pendant le test. Il expose une configuration de test locale et ne doit **pas être déployé**.
- `node tools/consolidation/browser-audit.cjs` : utilise3000 pour produit inchangé et3011 pour les scénarios artificiels d'update. Rapports/captures dans phase23 ; données locales synthétiques dans contextes navigateur isolés.
- `npm test`, `.venv/bin/python tools/preliminary-review/test_dossier.py`, `.venv/bin/python tools/expert-search/test_candidates.py`, `.venv/bin/python tools/consolidation/test_audit.py` : contrats passifs et techniques.
- `tests/coach-trajectories.cjs` écrit historiquement dans phase2 : **ne pas relancer sans préserver les octets de docs/coach/phase2/trajectory-report.json, copier le nouveau résultat sous phase23, puis restaurer l'original dans un finally**. La mesure23 est déjà disponible ; aucun besoin de rejouer pour consulter le dossier.

Le baseline/git-evidence correspond au HEAD audité5379624. Ne pas régénérer cette baseline sur un commit ultérieur et prétendre auditer le même état. Main a été récupéré et figé à83f89f8. Les trois runs CI sont listés par SHA exact, pas par dernier run de branche.

Aucune génération vidéo/animation, Blender, OpenSim, IK, scaling, correction ou retargeting. Les clips sont seulement lus, échantillonnés et joués pour la non-régression technique ; cela ne produit aucun avis professionnel.
