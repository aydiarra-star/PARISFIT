# Décision Phase25 — recommandation soumise à autorisation

## Décision

**Recommander B, avec A préalable : conserver le dépôt actuel et tout son historique en privé, puis créer une application publique propre sans cet historique. Ne pas purger maintenant.**

Cette solution préserve les SHA et les preuves, sépare clairement l'application des données biomécaniques et peut fonctionner sans achat : dépôts gratuits, construction locale, éventuel Pages depuis le dépôt public uniquement. La gratuité n'autorise pas une consommation Actions privée illimitée ; désactiver les exécutions d'archive ou rester en local. Aucun plan payant du propriétaire n'est supposé.

**Audit local terminé dans le périmètre décrit ; confidentialité globale non acquise, aucune opération de sécurisation distante exécutée.**

## Faits qui motivent ce choix

- 12 branches distantes, 13 refs PR, 158 commits et 1 135 blobs inspectés ; sept versions GLB animées, deux BVH et 141 versions de vidéos dans Git. Dépôt toujours public.
- Le paquet local Phase24 ne contient que 28 fichiers autorisés : zéro animation dans le GLB statique, 866 chemins internes testés en 404. Cela ne protège pas le dépôt GitHub.
- Phase24 n'est pas encore commitée/poussée ; HEAD distant reste fc51383. Pas de résultat production revendiqué.
- API : `has_pages: false`, huit déploiements listés tous échoués, aucune URL de production autoritative obtenue. Le risque Pages d'une bascule privée doit néanmoins être vérifié avec le propriétaire.
- 216 artefacts Actions totalisent ~1,64 Go selon métadonnées ; leurs contenus et l'ensemble des logs distants ne sont pas intégralement audités/sauvegardés.
- Aucun motif de secret détecté par le scan borné ; contacts professionnels, métadonnées d'auteur, données pseudonymes et droits particuliers identifiés. Aucun certificat d'anonymisation ou autorisation commerciale générale.
- Copie locale vérifiée de 1 739 fichiers + bundle Git, mais **cache éphémère, pas sauvegarde durable suffisante** pour supprimer/purger.

## Autorisations à demander, dans cet ordre

1. **Sauvegarde durable** : choisir une destination privée déjà possédée et les personnes autorisées ; permettre son transfert et les contrôles de restauration. Sans cela, aucune suppression/purge.
2. **Contrôles propriétaire** : confirmer hébergement/domaine/DNS, plan, collaborateurs, deploy keys, invitations et Apps. Les deux endpoints deploy keys/invitations étaient interdits à l'audit (403), donc pas déclarés vides.
3. **A — visibilité** : autoriser explicitement le passage du dépôt historique en privé, en acceptant les conséquences Pages/forks/métriques. Ni transfert de propriété ni retrait de collaborateurs implicite.
4. **B — séparation** : autoriser le nom/propriétaire d'un nouveau dépôt public propre et le périmètre exact à exporter. Aucun fork ni copie de l'ancien historique dans ce public. Dossier privé/local pour les captures ignorées par Git, vérifié séparément.
5. **Publication éventuelle** : nouvel accord de déploiement après audit de l'artefact réel, tests de droits et de cache. Garder les animations verrouillées ; publication technique ≠ validation biomécanique.

**C — purge** n'est pas autorisée par ces étapes. Si la conservation de l'URL actuelle du dépôt public est impérative, revenir avec une procédure B+C distincte, liste complète des refs et risques, sauvegardes durables testées, plan de coordination et accord explicite. Aucun résultat ne pourra promettre de révoquer les copies déjà distribuées.

## Livrables et limites

Les six rapports demandés sont dans ce dossier, accompagnés des inventaires SHA, refs, métadonnées d'accès, résultats HTTP et sauvegarde. `sources.md` donne la documentation officielle utilisée. Inventaire exhaustif pour les fichiers locaux sélectionnés et les objets des refs récupérées ; **pas d'exhaustivité affirmée sur les contenus Actions distants, refs cachées, caches, clones externes ou droits de chaque vidéo**. Ces limites sont des points à lever avant une opération irréversible, pas des ressources présumées absentes.

## Interdictions respectées

Aucun changement de visibilité, aucune purge, aucune suppression de ressource, aucun nouveau dépôt/service, aucun achat, aucun déploiement, aucune fusion/fermeture de PR, aucun contact de tiers. Aucun original ou rapport antérieur modifié. Aucune archive envoyée hors du sandbox. Aucun push effectué pendant Phase25.
