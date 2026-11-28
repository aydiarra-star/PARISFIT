# Test fictif de chiffrement — Phase27

**PASS : un seul fichier texte fictif, aucune ressource originale lue/chiffrée/déplacée par le test.**

Implémentation : pyrage 1.4.0, format age, destinataire X25519. Clé jetable créée en mémoire, jamais convertie en texte, écrite sur disque, imprimée ou envoyée. Ce n'est pas la clé du propriétaire. À la fin du processus elle n'est plus disponible pour une nouvelle restauration ; aucun effacement sécurisé de toute mémoire/swap n'est prétendu.

## Mesures

| Objet | Octets | SHA256 |
|---|---:|---|
| Texte fictif | 141 | `0f66a01b6e329f43d43020147bc163262e9f7813253dfc60b5cf508b397fff07` |
| Tar contenant le texte | 10240 | `12e7bada56ecfd836ee1b433b37a3633da5d3703feb9df1dce30c691d47ca892` |
| Chiffré age | 10479 | `a71ad0ab11bcfe7c2459d61d794b9941dd1c949d9816a3bbe47eb618e5730a52` |

Le chiffré a été découpé en **trois volumes** de 4 096 octets maximum pour exercer le scénario multi-volumes sur un petit fichier. Les hashes de chaque volume sont dans `poc-results.json`. Le réassemblage retrouve le SHA256 chiffré ; le déchiffrement retrouve le SHA256 du tar ; le texte restauré sur disque est identique octet par octet à l'original.

## Contrôles positifs et négatifs

- Marqueur explicite du texte, nom de fichier et texte complet absents du chiffré.
- En-tête `age-encryption.org/v1` **lisible**, volontairement ; « aucune donnée lisible » ne signifie pas que le format/métadonnées sont entièrement cachés.
- Deux chiffrements du même tar vers le même destinataire produisent des résultats différents.
- Mauvaise clé : refus ; octet modifié : refus ; fichier tronqué : refus.
- Volume manquant ou ordre inversé : refus avant restauration.
- Aucun réseau utilisé pendant le test cryptographique ; téléchargement de la dépendance effectué auparavant.
- Outil générique `volumes.py` : découpage/réassemblage du même chiffré fictif vérifié séparément. Il refuse une entrée non marquée age, ne traite aucune clé et n'effectue aucun upload.

L'absence de chaînes connues est un contrôle de non-présence du texte en clair, pas une preuve mathématique de sécurité. SHA256 ne remplace pas l'authentification cryptographique ni une source de manifeste de confiance.

## Reproduction locale

```sh
# Installation d'outillage dans le cache seulement, version épinglée :
python -m pip install --no-deps --target .cache/phase27/lib pyrage==1.4.0
PYTHONPATH=.cache/phase27/lib python tools/encrypted-backup/poc.py
```

Le script exige un dossier `.cache/phase27/poc` neuf et refuse d'écraser le test existant. Pour une autre campagne, choisir un nouveau dossier de sortie dans une copie du script, sans supprimer l'ancienne preuve. Les hashes chiffrés changeront normalement, la clé étant aléatoire. La restauration est vérifiée dans la même exécution ; conserver cette clé jetable n'est pas l'objectif.

## Limites

Binaire officiel age non installé (téléchargement échoué), GPG absent. Pas de test CLI croisé, de débit mémoire/disque sur les grandes archives, d'upload/download GitHub, de conservation réelle d'une clé propriétaire ou de chiffrement des originaux. Les quatre archives Phase26 restent en clair dans leur cache local original, inchangées. Le test ne les sécurise pas.

Les sorties détaillées sont dans `poc-output.txt`, `poc-results.json`, `volume-tool-output.txt` et `pyrage-provenance.json`. Horloge observée du test : 2026-11-28T12:17:33.322024+00:00 ; date de session de référence 2026-11-27, divergence explicitée.
