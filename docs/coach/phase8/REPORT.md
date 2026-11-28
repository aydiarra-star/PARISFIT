# Phase 8 — acquisition préparée, production bloquée

**Objectif premium non atteint.** Pas de nouvelle vidéo dédiée, pas de consentement signé, pas de reconstruction/retargeting nouveau, pas de GLB final ni de comparaison visuelle nouvelle. Aucune réussite n'est déduite des animations procédurales existantes. Ce dossier met en œuvre le cas explicitement prévu : préparer une capture concrète lorsqu'elle n'est pas disponible.

## Livraison utile maintenant

- `CAPTURE-PROTOCOL.md` : installation face/profil simultanés, corps/pieds visibles, calibration métrique, synchronisation et dérive, prise complète, règles de reprise/arrêt, dossier privé.
- `CONSENT.md` : modèle à adapter, choix séparés pour captation/traitement local/avatar commercial/partage pro/publication/cloud ; aucun accord obtenu.
- `SOLUTIONS.md` : options et coûts matériels/opérateur/licences, sans crédit payant ou tarif inventé.
- `BLENDER.md` : huit bibliothèques exactement identifiées, possibilités isolées, limites réseau et absence de moteur conteneur.
- `PIPELINE.md` : entrées/sorties à préserver, état de chaque étape, comparaison à construire.
- `PRO-REVIEW.md` : demande et grille de revue, non envoyées ; quatre niveaux de validation distincts.
- `tools/capture-pipeline/` : sonde Blender, recette Docker non construite, test BVH→rig de contrôle→GLB tenté mais bloqué, manifeste non signé, préflight privé et sept tests de refus.
- `index.html` : tableau de préparation sans image/vidéo fabriquée.

## Ce qui a été exécuté

1. Diagnostic `ldd` et import réel bpy : échec à `libXrender.so.1`, liste complète dans `environment-report.json`. Bibliothèques attendues : Xrender, Xxf86vm, Xfixes, Xi, xkbcommon, SM, ICE, GL.
2. Essai de récupération ciblée d'une bibliothèque GitHub : redirection d'asset inaccessible ; inspection d'archives compatibles potentielles, sans substitution système. L'obstacle n'est pas résolu. Aucun moteur Docker/Podman/Blender autonome disponible.
3. Appel réel du smoke Blender : échec avant import BVH, code 2 ; `blender-smoke-report.json`. Pas de GLB fabriqué pour masquer ce résultat.
4. Préflight avec manifeste vierge : code 2, **BLOCKED avant lecture de vidéo**. Rapport `intake-report.json`.
5. Sept tests unitaires du refus : consentement absent, source remplacée, vues incorrectes, booléen pris pour frame, hash incorrect, chemin privé, accord non booléen. Les fixtures sont des métadonnées sans personne, **pas de tests de qualité du mouvement**.

## Décision et preuves manquantes

| Niveau | État | Preuve nécessaire |
|---|---|---|
| Capture légitime | NON DISPONIBLE | Droits vérifiés, deux films du même squat, calibration et consentement privé |
| Technique pipeline complet | BLOQUÉ | Blender fonctionnel, extraction/reconstruction/retarget/export réellement exécutés |
| Fidélité à la nouvelle capture | NON ÉVALUABLE | Mesures et comparaison horodatée source/RAW/final |
| Qualité visuelle humaine | NON ÉVALUABLE | Cycle complet, plusieurs vues et ralenti examinés |
| Validation pédagogique/sportive | NON OBTENUE | Avis réellement obtenu, qualification et fichiers examinés identifiés |
| Admission | BLOQUÉE | Aucun mouvement candidat à admettre |

Les huit exercices et tous les dossiers antérieurs restent intacts. Aucun utilisateur filmé, aucune vidéo personnelle reçue/transmise, aucun professionnel fictif, aucun test de téléphone physique, aucune dépense, activation, fusion ou production.

## Ce qu'il faut fournir pour poursuivre

Une personne adulte volontaire et un opérateur pouvant réaliser la séance décrite, deux caméras simultanées fixes (ou trois), puis les originaux et la calibration avec les droits de traitement vérifiés. Garder les signatures privées. **Ne pas envoyer de vidéo dans Arena avant d'avoir autorisé ce canal de traitement ; le consentement local seul ne suffit pas.** Une attestation de portée des droits peut être communiquée sans exposer les pièces signées.

Il faut également une machine compatible pour exécuter la recette Blender préparée et un professionnel qualifié pour la revue. Ni la disponibilité de ce matériel ni celle de ce professionnel n'est présumée. À défaut, conserver le blocage plutôt que revenir à une ancienne animation.

## Reproduction du diagnostic et du refus

```sh
.venv/bin/python tools/capture-pipeline/probe-blender.py
python3 tools/capture-pipeline/test_intake.py
.venv/bin/python tools/capture-pipeline/intake.py \
 --manifest tools/capture-pipeline/session-template.json \
 --private-root /tmp/parisfit-private-not-provided \
 --report /tmp/parisfit-intake-report.json
# Sortie 2 attendue : aucune capture autorisée.
```

Environnement mesuré : Python 3.11.2, bpy 4.2.0, MediaPipe 0.10.21, OpenCV headless 4.11.0.86, imageio-ffmpeg **0.8.2** (constat actuel, différent de la version 0.6.0 proposée dans l'ancienne recette). Aucune extraction MediaPipe réalisée cette phase.

La recette Docker n'a pas été exécutée ; la branche vidéo du préflight n'a pas été qualifiée sur une nouvelle capture. Aucun environnement propre de production certifié. Les sources primaires et licences étudiées sont liées dans SOLUTIONS.md et les dossiers précédents.
