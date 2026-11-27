# Accéder réellement aux preuves

## Petits aperçus immédiatement disponibles

La page `index.html` inclut4MP4 diagnostiques locaux (environ520Ko au total) et des PNG : natif, filtre seul, rééchantillonnage seul et combinaison historique. Les données proviennent du BVH public épinglé et des scripts exécutés localement. Ce ne sont ni des vidéos du sujet ni une reconstruction candidate. Les grands artifacts, sources et matrices restent hors Git.

Ces petits aperçus de secours traitent l'échec récurrent du téléchargement, sans faire croire que les anciens films Rocketbox ont été visionnés. Une image centrale native et le PNG de marqueurs au point bas ont été ouverts pour vérifier sa lisibilité ; aucune revue intégrale des vidéos ni validation biomécanique/professionnelle revendiquée. Le PNG overlay conserve le même instant native/filtré, avec source verte et branche filtrée corail ; l'écart peut être subpixel à cette échelle.

## Depuis GitHub Actions

1. Ouvrir le run indiqué par `ci-evidence.json` ou le dernier run du commit livré.
2. En bas, section **Artifacts**, télécharger `phase12-source-benchmark`.
3. Extraire le ZIP, ouvrir `index.html` : MP4 H.264, PNG, métriques, fichiers d'origine s'ils ont été récupérés, attribution/licences.
4. `phase11-anatomical-diagnostics` du même workflow contient les diagnostics A/B/C Rocketbox, sans réutiliser la branche filtrée.

Dans un terminal où `gh` est déjà connecté :

```sh
bash tools/source-benchmark/recover.sh NUMERO_DU_RUN
# équivalent :
gh run download NUMERO_DU_RUN --repo aydiarra-star/PARISFIT \
  --name phase12-source-benchmark --dir .cache/phase12-recovered
```

Ne pas coller un jeton dans le chat. Si le navigateur télécharge mais que le proxy du terminal échoue EOF, utiliser le navigateur ; aucune URL d'artifact signée et expirante n'est stockée dans le dépôt.

## Reproduction si l'artifact expire

Rétention30jours. Checkout du commit indiqué dans la preuve, sans remplacer les hashes d'entrée : installer NumPy, Pillow, ffmpeg, c3d0.6.0 pour les originaux ; puis exécuter download.py, test_audit.py, audit.py, visuals.py, originals.py, analyze-originals.py et gallery.py dans `tools/source-benchmark/` (voir workflow pour commandes exactes). Les trois BVH de screening sont téléchargés par blobs GitHub épinglés. Un original indisponible est signalé NON TESTÉ, jamais remplacé silencieusement.

Aucune donnée privée autorisée par ce script : seuls les fichiers publics explicitement listés sont traités. Aucun achat, upload externe, déploiement ou activation.
