# Autorisations et frontière entre CI et capture privée

Les formulaires phase8 restent valables comme modèles non signés. Ne pas filmer avant accord. Ne pas confondre :

- **Filmer** : usage `record`, accord de captation.
- **Analyser localement** : `local-analysis`, captation + analyse locale + droits de l'opérateur.
- **Exploiter commercialement l'avatar** : `commercial-animation`, accord supplémentaire explicite.
- **Publier la source** : `publish-source`, distinct de `publish-motion` pour redistribution des coordonnées/GLB.
- **Transmettre à un service externe** : `external-upload`, accord explicite et périmètre nommé (service et finalité), jamais déduit du traitement local.

`tools/capture-pipeline/permissions.py` contrôle ces permissions par opération ; cinq tests de séparation. Il n'effectue aucun upload et ne vérifie pas juridiquement une signature. Le préflight `intake.py` reste bloquant avec le manifeste non signé, et n'ouvre pas l'admission sportive. Une attestation de l'opérateur ne remplace pas le contrôle des documents réels en privé.

**La CI publique n'accepte que le BVH CMU déjà publié et Rocketbox, identifiés par SHA256 dans le script.** Pas de paramètre vidéo, pas de secret, pas de formulaire d'upload de capture personnelle. Les artefacts de CI sont des données de contrôle publiques autorisées. Une capture dédiée doit être traitée localement, ou dans un environnement privé dont le service a été expressément autorisé ; ne pas placer ses originaux, signatures, pièces d'identité ou données sensibles dans Git/PR/artefacts publics.

## Entrée future du retargeting

Le segment testé commence au BVH, **pas au film**. La vidéo devra d'abord passer droits → préflight → calibration/synchro → extraction 2D → reconstruction 3D → résolution des rotations, avec leurs rapports d'incertitude. Le passage automatique d'une vidéo inconnue à un BVH de qualité n'est pas implémenté ni validé dans cette phase.

Le BVH de contrôle utilise la hiérarchie CMU, une T-pose de calibration ajoutée au début et les axes/unités documentés. Pour une nouvelle reconstruction : fournir un mapping explicite, une pose et un référentiel de calibration, unités mètres, timing natif, rotations complètes, origine/sol et preuves de droits ; **ne pas renommer aveuglément les os d'un autre rig ni copier ce facteur d'échelle**. L'actuel exécuteur refuse un autre hash en CI. L'adaptateur d'une nouvelle hiérarchie devra être qualifié localement avant admission.

Les corrections sont désactivées pour le contrôle de fonctionnement : aucun IK, lissage ou projection au sol. Un modèle exporté ne prouve pas des appuis corrects. L'étape de correction future exige fenêtres de contact relues et journal RAW/CORRECTED.
