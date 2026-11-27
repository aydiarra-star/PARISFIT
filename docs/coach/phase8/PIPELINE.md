# Contrat de chaîne et état d'exécution

| Étape | Entrée / sortie à conserver | État phase8 |
|---|---|---|
| Consentement + captation | Registre privé / films natifs face-profil même prise | **Manquants** |
| Réception privée | Manifest, SHA256, originaux, vidéo calibration | Contrôle de refus exécuté, aucun film lu |
| Qualité + synchro | PTS natifs, repères début/fin, cadrage complet, rapport décode | Préflight implémenté, branche vidéo non qualifiée sur capture réelle |
| Calibration | Intrinsèques/extrinsèques, distorsion, sol, échelle, erreur reprojection, version solveur | À produire ; jamais inventer calibration.json |
| Extraction | Repères 2D + confiance par vue et horodatage, overlays sans recadrage caché | Non exécutée faute entrée autorisée |
| Reconstruction | Points 3D triangulés, résidus par caméra, trous/occlusions explicites | Non exécutée |
| Retarget RAW | Source préservée, repères anatomiques, offsets, proportions, rotations locales | Non exécuté sur nouvelle capture |
| Correction | RAW immuable, patches de contact relus, journal avant/après, impact spatial/angulaire | Non exécutée ; ne pas fixer un pied dont l'appui est inconnu |
| Export + Three.js | GLB, frames/temps, comparatifs source→extrait→Rocketbox→final | Aucun nouveau GLB ou comparatif disponible |
| Revues | Technique / fidélité / visuel / pédagogique, chacune liée au hash | Toutes en attente |

## Contrôle d'entrée local

`intake.py` ne téléverse rien et ne lance aucune IA. Vérifie les attestations explicites avant même de lire une vidéo. Les attestations sont celles de l'opérateur : **ce script ne valide pas juridiquement une signature**. Les originaux doivent être hors du dépôt. Refuse les chemins échappant à la racine privée (y compris symlinks).

Après vérification humaine des droits et calibration, sur la machine qui héberge les films :

```sh
.venv/bin/python tools/capture-pipeline/intake.py \
 --manifest /chemin/prive/PF-SQUAT-001/session.json \
 --private-root /chemin/prive/PF-SQUAT-001 \
 --report /chemin/prive/PF-SQUAT-001/preflight.json
```

Le manifeste de départ `session-template.json` n'accorde aucun droit. L'exécution avec ce manifeste doit retourner **2 / BLOCKED avant lecture**. C'est le résultat livré dans `intake-report.json`.

Pour un manifeste complété, le script vérifie les empreintes, décode toutes les frames localement, rapporte résolution/FPS nominal et cohérence des deux événements synchro. Il ne voit pas si les pieds sont cadrés et ne vérifie ni la vraie calibration ni les PTS variables : même sans anomalie mécanique, il retourne **PREFLIGHT_ONLY_NOT_RECONSTRUCTION_READY**. Les seuils 1080p, 29–121 FPS et ≤1/60 s de dérive sont des filtres d'acquisition du protocole, pas des seuils de naturel ou de précision biomécanique.

## Comparaison à réaliser après acquisition

Quatre colonnes, mêmes horodatages : film réel / repères extraits / RAW Rocketbox / CORRECTED final. Films réels face et profil uniquement ; la vue trois-quarts de la reconstruction doit être étiquetée **vue reconstruite**, jamais vidéo réelle. Si une vraie vue trois-quarts est souhaitée, enregistrer une troisième caméra simultanée. Vitesse native et ralenti ×0,5 sans interpolation de frames dissimulée. Cycle complet avec les plateaux initial/final ; marquer les trous plutôt que les combler silencieusement.

Conserver entrée et étapes, hash du modèle, versions, coordonnées/unité/axes, mapping anatomique et toutes les corrections (motif, intervalle, auteur, impact, refus). Pas de fichier final quand l'entrée manque.
