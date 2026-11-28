# Décision Phase26 — préparation vérifiée, sauvegarde durable non acquise

## Ce qui est effectivement sauvegardé localement

- Historique Git récupérable : **158 commits, 29 entrées de références bundle, 1 779 objets Git dont 1 135 blobs**, avec restauration indépendante réussie.
- **972 fichiers du projet courant**, incluant les originaux suivis, workflows, licences, rapports jusqu'à Phase25 et modifications non committées.
- **811 fichiers de travail/cache**, incluant les captures, sources et modèle statique local.
- Manifestes SHA256, métadonnées Actions, résultats et procédure Phase26 dans le supplément de preuves scellé séparément.

Les trois archives de sources ont passé un **vrai test de restauration dans un répertoire isolé**, suivi des vérifications d'objets, de fichiers, `git fsck`, des régressions npm et du test de modèle statique. Le supplément de preuves dispose de son propre reçu de restauration. Aucune source ou preuve historique modifiée.

## Ce qui ne l'est pas

- **Aucune copie sur une destination privée durable vérifiée.** Toutes les archives et leurs restaurations sont dans `.cache`, éphémère et exclu des snapshots persistés.
- **216 artefacts Actions : métadonnées uniquement.** Trois tentatives ont échoué, aucune archive distante validée. Pas de conclusion sur la récupérabilité des 213 autres.
- Ensemble des logs/commentaires/issues/wiki/settings/packages GitHub, copies externes, références cachées/supprimées et credentials : non inclus, sauf métadonnées explicitement consignées. Les credentials sont volontairement exclus.

## Destination et sécurité

19 dépôts sont visibles par l'intégration, tous publics ; aucun stockage connecté privé n'est confirmé. Le plan du compte n'est pas exposé. L'existence théorique de dépôts privés gratuits n'est pas une destination disponible vérifiée. Les autorisations API ne donnent pas une vue exhaustive de tous les comptes/accès du propriétaire.

Aucun des six motifs de secrets recherchés ne correspond dans **3 802 unités** inspectées (fichiers, blobs, membres d'archives). Cela ne prouve pas l'absence absolue de secrets ou données personnelles. Les archives ne sont pas autorisées au partage, et aucun transfert externe n'a eu lieu.

## Décision

**Ne pas déclarer « sauvegarde complète et durable ». Ne pas changer la visibilité ni créer le dépôt public maintenant.**

La préparation et la restauration locales sont réussies. L'objectif de durabilité est **bloqué en attente d'une destination privée réelle et de votre autorisation de transfert**. La recommandation future reste : dépôt historique privé conservant les preuves, puis dépôt public neuf par liste positive, sans purge initiale et sans importer l'histoire interne.

## Autorisations nécessaires, séparées

1. Désigner une destination privée gratuite déjà possédée et autoriser la vérification de son accès, capacité et rétention. Aucun abonnement ni création de compte implicite.
2. Autoriser le transfert des archives précisément identifiées, manifestes et supplément ; décider chiffrement et gestion de clés par le propriétaire. Ne jamais communiquer de clé/jeton dans le chat.
3. Réussir les SHA256 **sur la destination**, un retour de copie et une restauration indépendante ; vérifier la récupération après fermeture du sandbox. Résoudre les artefacts Actions manquants ou accepter explicitement un périmètre partiel.
4. Autoriser ensuite, et seulement séparément, le changement de visibilité et la création éventuelle d'un dépôt public propre. Le nom, les accès et les fichiers de ce futur dépôt doivent être approuvés.
5. Publication, fusion, purge ou suppression éventuelles restent soumises à leurs propres accords, non couverts par cette phase.

## Interdictions respectées

Aucun changement de visibilité/permissions, aucune suppression/purge, aucun transfert sortant, aucune création de dépôt local ou distant, aucun changement/création de branche, aucune fusion, aucun push, aucun déploiement. Les appels GitHub sont des lectures de métadonnées et tentatives de téléchargement entrant ; aucune archive n'a été envoyée à un service externe.
