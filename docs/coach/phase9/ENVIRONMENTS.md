# Environnements évalués

| Voie | Observation / statut |
|---|---|
| Arena local + bpy 4.2.0 | Huit bibliothèques absentes ; erreur phase8 préservée. Toujours non opérationnel localement |
| Python isolé en CI Ubuntu24 + bpy4.2.0 | Dépendances installées mais processus termine code139, run46046334582. Ne pas considérer cet essai comme réussi ; cause du crash non isolée |
| Blender natif Ubuntu24 en background | Blender4.0.2 démarre réellement ; premier import échoue faute NumPy visible par Python embarqué. Rapport négatif conservé. Installation python3-numpy/requests + chemin dist-packages ajoutés ; résultats suivants dans REPORT.md |
| Conteneur Docker | Recette phase8 conservée non testée ; pas nécessaire pour le runner CI natif. Aucun Docker/Podman dans Arena |
| Blender autonome officiel téléchargé | Non installé ici ; les téléchargements d'assets de releases redirigent vers des hôtes inaccessibles. La distribution Ubuntu est l'alternative réellement essayée |

## Huit dépendances à résoudre

`libXrender.so.1`→`libxrender1`, `libXxf86vm.so.1`→`libxxf86vm1`, `libXfixes.so.3`→`libxfixes3`, `libXi.so.6`→`libxi6`, `libxkbcommon.so.0`→`libxkbcommon0`, `libSM.so.6`→`libsm6`, `libICE.so.6`→`libice6`, `libGL.so.1`→`libgl1`.

Dépendances supplémentaires explicites : `libegl1`, `libx11-6`, `libxext6`, `libgomp1`, Blender natif et NumPy/requests de la distribution. Background n'élimine pas la résolution dynamique de ces bibliothèques. Les Python du runner et de Blender peuvent différer : lire les versions réellement rapportées, pas seulement `python --version` du shell.

## Installation et relance sur machine autorisée

```sh
sh tools/blender-pipeline/install-ubuntu.sh
npm ci
npx playwright install --with-deps chromium
# Démarrer séparément le serveur HTTP racine dépôt sur 3000.
sh tools/blender-pipeline/run-control.sh
```

La CI réalise ces opérations dans le job `blender-control` avec source/target hashés, sortie isolée `.cache/phase9`, logs et artefacts même en échec, timeout15min et permissions GitHub lecture seule. Aucun secret ni donnée personnelle. Les fichiers GLB/rapports/images de contrôle sont en artefact `phase9-blender-control` (rétention30 jours) ; les rapports copiés dans docs persistent.

`ubuntu-24.04` et apt sont des versions de distribution, pas un build bit-à-bit hermétique. `dpkg-query -W` et `pip freeze` sont archivés dans chaque artefact. La version Blender, Python, NumPy, système, hashes et temps d'étapes sont dans le rapport. Aucun achat, nouvelle souscription, service payant ou runner premium configuré ; utilisation de la CI standard déjà active du dépôt.
