# Phase 7 — socle de pipeline, livraison partielle et bloquée

**Le critère final n'est pas atteint. Aucun nouvel exercice exceptionnel ni pipeline de production premium validé.** Ce dossier livre un audit, une sélection juridique, une architecture et un contrôle exécuté de bout en bout. Il ne faut pas assimiler ce contrôle à une nouvelle animation de mocap ou à un retargeting Blender réussi.

PR11 en brouillon ; aucune fusion, activation ou production. Les huit exercices et toutes les preuves des phases 1–6 sont inchangés. Aucun coût, achat, transmission de vidéo personnelle, validation professionnelle ou test de téléphone physique.

## État des livrables

| Livrable | État |
|---|---|
| Audit phases 1–6 | `AUDIT.md` |
| Comparaison universitaire/sport/multicam/pro/ouvert + droits | `DATASETS.md`, textes licence dans `licenses/` |
| Étude Blender et essai réel | `BLENDER.md`, erreur `blender-report.json` ; moteur indisponible, adaptateur non validé |
| Pipeline contrôle reproductible | `tools/animation-pipeline/run.py`, manifeste versionné, export/mesure/admission séparés |
| Deuxième mouvement | **Contrôle pompe existante** (procédurale), 5 s, départ haut → descente → remontée → retour haut ; pas une nouvelle capture |
| Prototype / GLB | `prototype.glb`, rééchantillonnage à 60 Hz, quaternions normalisés/hémisphère continu ; aucun bénéfice visuel prétendu |
| Comparaison | 8 vidéos complètes, 3 vues + ralenti, original/prototype ; galerie `index.html` |
| Mesures / tests | `measurements.json`, `decision.json`, `evidence-report.json`, tests admission et navigateur |
| Nouveau retarget de pompe optique / Blender / qualité premium | **NON LIVRÉ / NON VALIDÉ** |

## Pourquoi ce contrôle et pas une nouvelle correction

Le seul cycle pompe exploitable immédiatement avec provenance locale claire est celui déjà créé dans PARISFIT. Son isolation permet de tester conservation des poses, timing, appuis et export sans attribuer à une source externe un mouvement qu'elle n'a pas fourni. On ne transforme pas une séquence CMU d'acrobaties ou d'interaction en pompe standard. Le contrôle conserve les limites pédagogiques et la provenance procédurale des phases 1–2.

La version exportée n'ajoute aucun IK, aucun lissage, aucun changement manuel ni mouvement inventé. C'est volontaire : il faut d'abord savoir si le transport de données change la pose. La resampling/normalisation n'est pas une amélioration du naturel. Aucune troisième animation n'est commencée.

## Résultats exécutés

Validation locale : `npm test`, `npm run test:browser`, six tests d’admission Python, exécution intégrale du runner et décodage FFmpeg des huit vidéos : PASS. Journaux `regression.log` et `pipeline-run.log`. Le succès logiciel ne valide pas le naturel.

301 poses / 60 Hz sur 5 secondes. Écart maximal original→prototype des pivots articulaires : **0,000197 mm** (arrondi flottant). Appui minimum ~**1,984 mm** au-dessus du sol, gap max ~**2,000 mm**, dérive des points suivis ~**0,017 mm** ; vitesse articulaire max **0,217 m/s**, accélération **0,7425 m/s²**. GLB : **5 627 520 octets**, un clip ; runtime **5 789 744 octets**, huit clips, SHA inchangé.

Ces excellents nombres illustrent précisément le piège : une animation procédurale peut garder les effecteurs fixes et satisfaire ces tests **sans être un humain naturel**. Les points sont choisis parmi la peau associée aux mains/pieds, pas des patches anatomiques approuvés. Pas de contrôle exhaustif des collisions ni de validation des doigts ou de la déformation de peau. Source et résultat ne sont pas des performances humaines indépendantes.

## Seuils de triage — déclarés avant mesure, pas normes biomécaniques

Le manifeste a été écrit avant la mesure du prototype. Il cible seulement une **pompe lente à quatre supports supposés immobiles**, pas un saut ni une transition à appuis mobiles.

- Pénétration ≤3 mm, gap/dérive ≤5 mm : budget visuel millimétrique proche des appuis ; **ce n'est pas une tolérance physique à pénétrer le sol**. Tout contact négatif visible est à revoir, même sous ce budget. Pression et patch palmaire restent requis.
- Erreur longueur ≤0,1 mm : tolérance numérique conservatrice pour rig rigide, pas autorisation de déformation anatomique.
- Pas quaternion ≤10°/frame à 60 Hz : alarme de discontinuité grossière, pas limite articulaire ni validation d'une vitesse naturelle. Mesurer aussi vitesse angulaire continue avant qualification réelle.
- Vitesse ≤2 m/s et accélération ≤20 m/s² : plafonds de triage pour ce contrôle lent, non issus d'une population clinique. Doivent être comparés aux données autorisées et revus, sans les relever après un échec pour accepter le clip.
- Écart boucle ≤2 mm : contrôle géométrique uniquement. Une pompe cyclique peut boucler mais ne fournit pas un raccord debout→sol ou une récupération sûre.
- Visuel/pédagogie/anatomie/collision/appareils/récupération : **preuves indépendantes obligatoires**, non remplacées par ces seuils.

Le moteur d'admission ne peut actuellement jamais activer un asset : preuves de revue signées et liées au hash non implémentées. Cette limitation est explicite, pas un système de certification prétendu complet. Les booléens dans le manifeste ne peuvent pas ouvrir l'admission. Le type optique testé dans le code est une politique de ce pilote, pas une assertion que seule la mocap optique peut devenir valable.

## Reproduction réellement exécutée et limites d'environnement

Dépendances existantes : Node 22, npm ci (Three 0.169.0 / Playwright 1.65.1), Python 3.11, Pillow 12.0.0 et imageio-ffmpeg 0.6.0. Serveur local racine dépôt sur 3000 ; exports uniquement `docs/coach/phase7/`. Chromium et bibliothèques spécifiques au sandbox peuvent nécessiter :

```sh
export LD_LIBRARY_PATH=/tmp/al2023/lib
export CHROMIUM_PATH=/tmp/chromium
.venv/bin/python tools/animation-pipeline/run.py
python tools/animation-pipeline/test_gate.py
FFMPEG_PATH=$(.venv/bin/python -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())') node tools/animation-pipeline/capture.cjs
.venv/bin/python tools/animation-pipeline/verify.py
node tests/coach-production-pipeline.cjs
```

Le manifeste représente une seule fixture qualifiée ; ce n'est pas encore un import universel de rigs. Le runner refuse un autre intervalle ou dossier runtime. Les composants ont été exécutés ; le runner est également vérifié lors de la livraison. Les hash des entrées et des sorties figurent dans les rapports. Un environnement vierge complet n'est pas certifié.

Blender séparé : `.venv/bin/python tools/animation-pipeline/blender-stage.py` → échec attendu code 2 ici. Le script préparé n'implémente pas la calibration BVH/IK ; voir l'étude. Ne pas fabriquer un `blender-roundtrip.glb` de substitution.

## Conditions de reprise pour une vraie production

1. Obtenir **une seule** pompe correctement filmée/capturée avec droits et repères fiables, ou un extrait professionnel autorisé pour ce dépôt. Conserver origine, calibrations, FPS, confiance, sol, annotations des appuis et mouvement complet.
2. Installer Blender complet et faire passer l'aller-retour GLB avant un solveur. Implémenter calibration multi-axes et retarget RAW ; mesurer résidus, puis seulement contacts CORRECTED distincts.
3. Annoter paumes/semelles anatomiquement ; mesurer contact/rotation/charge transférée avec la source plutôt que supposer des effecteurs fixes.
4. Comparer source/RAW/CORRECTED/export aux mêmes temps. Faire examiner la pédagogie et le naturel par un professionnel réellement identifié, puis les appareils physiques et les raccords/récupération.
5. Ne qualifier la méthode que si elle produit ce mouvement sans corrections ponctuelles opaques. Aujourd'hui : **BLOCKED**, pas « pipeline fiable de production terminé ».
