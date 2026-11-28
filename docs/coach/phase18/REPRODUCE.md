# Reproduction et périmètre des tests

BasePARISFIT : `f4d4146a372d08acca620b1a9facf54368c1fcda`. Branche de travail conservée, aucun changement de branche nécessaire.

```sh
.venv/bin/python tools/independent-review/audit.py
node tools/independent-review/cache-identity.cjs
python tools/independent-review/questions.py
python tools/independent-review/build.py
python tools/independent-review/test_review.py
npm test
```

`audit.py` lit les deuxC3D en cache dephase17. S’ils manquent, utiliser uniquement l’acquisition limitée `tools/passive-qualification/acquire.py`, qui n’exécute pas de code auteur. **Ne pas lancer les scripts MATLAB, scaling ou IK.** SHA256 comparés au manifestphase17 avant toute conclusion.

L’en-tête et le bloc de paramètres sont décodés par Python standard, indépendamment de python-c3d. Le contrôle est limité au formatIntel flottant de ces fichiers et ne certifie pas toutes les variantesC3D. Le modulec3d0.6.0 déjà installé sert ensuite à comparer les propriétés et citer son code. Aucune dépendance ajoutée àPARISFIT.

`cache-identity.cjs` utilise le vendorThree local pour parser les métadonnées des clips existants et inspecter la fonction de cache. Il n’appelle aucun mixer.play/update et ne crée aucune nouvelle piste, vidéo ou animation. Un avertissementNode concernant la détectionESM est possible ; pas de modification du package/runtime pour le masquer.

`questions.py` reprend les57labels et statuts antérieurs sans les promouvoir. Les réponses du questionnaire et du registre restentnulles. LesMarkdown d’interprétation et les sourcesC3D consultées sont éditoriaux, pas des résultats de solveur.

`build.py` réutilise seulement le formateur documentaire dephase17, sans exécuter son programmeprincipal ni réécrire ses sorties. La pagephase18 et son manifest sont nouveaux. Les752fichiers protégés à la référence sont vérifiés parSHA256 ; seuls les points d’entrée des tests/package etCI peuvent être étendus.

## Navigateur

Servir le dépôt sur0.0.0.0:3000, puis :

```sh
node tests/coach-independent-review-browser.cjs
python tools/independent-review/build.py
node tests/coach-independent-review.cjs
```

Dans ce sandbox : `CHROMIUM_PATH=/tmp/chromium`, `LD_LIBRARY_PATH=/tmp/al2023/lib`. Sept documents dépliés,57questions et lienslocaux vérifiés à320/390/768/1200px. L’émulation n’est pas un test physique de téléphone ni une revue professionnelle.

La CI exécute aussi les tests historiques dans son environnement éphémère. Leurs réécritures de rapports ne sont pas importées dans les preuves antérieures de cette branche. Le diff exactphase17 conservé est la base de l’enquêtehistorique, pas une série fraîche choisie pour améliorer les valeurs. UnPASS de régression ne valide pas la biomécanique.
