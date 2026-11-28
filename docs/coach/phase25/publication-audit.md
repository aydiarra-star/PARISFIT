# Audit de publication — Phase25

## Résultat local : PASS, périmètre strictement défini

Audit **sans régénérer ni supprimer** le paquet `.cache/public` produit en Phase24. Contrôle de liste exacte, hash SHA256 de chacun des fichiers et comparaison aux sources actuelles. Le dérivé est recalculé en mémoire uniquement pour vérifier son identité.

- **28 fichiers**, **6 271 964 octets**.
- GLB statique : **0 animation**, 14 accessors, 18 bufferViews, tous référencés par géométrie/skin/images ; identité exacte au dérivé reproductible sans échantillons d'animation.
- Test indépendant Phase24 : géométrie, poids, matrices, squelette, matériaux et quatre textures conservés.
- **866 chemins internes historiques distincts** (rapports, diagnostics, tests, vidéos, captures et modèles non publics) demandés directement au serveur HTTP du paquet : **866 réponses 404**.
- **28 chemins autorisés : 28 réponses 200**.
- Aucun `docs/`, `tools/`, `tests/`, `.git`, BVH, C3D, vidéo ni GLB animé dans le paquet. Les données JSON de trajectoire et dépendances spécifiques des lecteurs ne sont pas copiées. Three et OrbitControls restent publics car nécessaires au modèle statique.

Résultats détaillés : `publication-verification.json` (tous les chemins, tailles, hashes et statuts). Script : `tools/confidentiality-audit/publication.py`. Il démarre un serveur local temporaire sur un port libre puis l'arrête ; aucune publication distante. Le premier passage fermait les réponses sans lire tout leur corps et produisait des BrokenPipe côté serveur ; le test lit désormais les corps avant fermeture, sans changer les assertions. Les résultats finaux sont ceux archivés.

## Paquet futur ≠ site de production ≠ GitHub

| Surface | Constat | Conclusion permise |
|---|---|---|
| `.cache/public` Phase24 | liste positive et tests HTTP complets ci-dessus | ressources internes absentes de ce paquet |
| workflow Pages dans l'arbre local | upload `.cache/public` | configuration prévue, **non déployée** |
| branche distante actuelle / main | modifications Phase24 pas encore poussées ; ancien workflow à examiner lors de toute mise en service | ne pas attribuer la correction locale au serveur |
| API GitHub repository | `has_pages: false` | aucun Pages actif déclaré par cette API |
| endpoint Pages | HTTP 404 | configuration Pages non obtenue |
| 8 déploiements listés | dernier état `failure`, URL d'environnement vide pour chacun | aucun déploiement réussi identifié dans cette liste |
| autres hébergeurs / domaine propriétaire | aucun URL de production autoritatif fourni | **non vérifié**, pas de certification production |
| dépôt GitHub public | originaux présents dans branche/histoire/PR | accès indépendant du paquet, non corrigé par les 404 locaux |

L'environnement n'autorise pas librement des connexions à un domaine d'hébergement externe ; aucune URL de production n'a été inventée. Les 404 locaux ne sont donc **pas** présentés comme des 404 de production.

## Réserves et suite

Après autorisation séparée d'une éventuelle publication : auditer le **paquet réellement déployé**, son hash, les URL directes (y compris variantes encodées/Range), les anciennes URL et caches/CDN, et les anciens service workers. Les tests Phase24 de cache/navigation sont conservés, non réécrits. Les PWA qui restent hors ligne avec les anciennes ressources ne peuvent pas être révoquées immédiatement.

L'audit valide la frontière de publication locale, pas l'innocuité biomécanique d'une animation ni la confidentialité de toutes les copies distribuées.
