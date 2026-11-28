# Registre des validations — Phase24

Source exécutable : `animation-validation-registry.json` à la racine, consommée par le runtime. Ce document n'est pas un second registre d'autorisation.

Version : `5379624-source-unchanged` (identifiant de livraison historique, sans prétention de version fournisseur).
Fichier interne : `assets/coach/coach.glb` — 5 789 744 octets.
SHA256 : `1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb`.

| ID clip / exercice | Statut | Professionnel / date / rapport |
|---|---|---|
| squat | non évaluée | non renseignés |
| pompes | non évaluée | non renseignés |
| gainage | non évaluée | non renseignés |
| fentes | non évaluée | non renseignés |
| jumpingjacks | non évaluée | non renseignés |
| mountainclimber | non évaluée | non renseignés |
| etirementdos | non évaluée | non renseignés |
| mobiliteepaules | non évaluée | non renseignés |

Chaque entrée contient ID, exercice, version, hash du fichier complet, statut, identité/qualification du relecteur, date, référence et hash du rapport, périmètre exact, conditions et limites. Champs inconnus : `null` ou liste vide, jamais une approbation implicite.

Statuts admis : `non évaluée`, `en cours d’évaluation`, `refusée`, `validée`. Seul le dernier peut franchir le contrôle documentaire, avec toutes les informations requises. Le hash lie la validation au fichier exact : tout changement de clip ou autre octet du fichier invalide l'ancienne correspondance. Le fichier complet est un périmètre volontairement conservateur : modifier une texture invalide également la correspondance.

Le moteur vérifie la structure, pas l'authenticité scientifique d'un rapport : une revue humaine doit vérifier preuve, qualifications, portée, conditions et limites avant modification du registre. Les champs synthétiques utilisés uniquement en mémoire dans le test ne sont pas une validation. Il n'existe ici aucun rapport réel d'approbation. L'intégration publique reste statique même si quelqu'un change le statut seul.
