# Décision Phase28 — non prêt, arrêt avant chiffrement

**Le résultat demandé « archive réelle chiffrée, restaurée et vérifiée » n'est pas atteint.** Le blocage est explicite et requis par votre étape 2 : aucune identité age de production créée/conservée par le propriétaire dans un environnement sûr n'a été confirmée, et aucun destinataire public réel n'a été fourni.

## Effectué

- Revalidation des tailles/SHA256 des **quatre archives Phase26 exclusivement**.
- Identification et vérification des **1 783 fichiers**, par chemin/taille/hash dans `input-files.csv`.
- Identification/relecture des **1 779 objets Git** du magasin indépendant restauré Phase26, dans `input-git-objects.csv`.
- Relecture des **36 pièces de preuves supplémentaires** ; sources et anciens rapports inchangés.
- Contrôle du paquet local de **28 fichiers publics**, sans archive ni motif de secret recherché, et revue des chemins d'upload des workflows.
- Sept livrables demandés créés, avec statuts bloqués explicites. Le fichier de checksums contient un avis de non-production, aucun hash inventé.

## Non effectué

Aucun chiffrement réel, volume chiffré, réassemblage ou déchiffrement Phase28 ; **aucun test réel après chiffrement**. Ni le test fictif Phase27 ni la restauration Phase26 ne sont présentés comme un substitut. Aucune clé réelle générée, recherchée sur le disque, lue, copiée ou publiée.

Les **216 artefacts Actions restent absents en contenu**, selon la collecte Phase26. Les copies Phase26 restent en clair dans le cache éphémère du sandbox, pas dans une nouvelle sauvegarde durable.

## Pour débloquer sans exposer une clé

1. Créer/conserver l'identité age sur votre machine sûre, hors Git, avec copie de secours indépendante.
2. Confirmer cette conservation et fournir **seulement le destinataire public age**, jamais l'identité privée ou la phrase secrète.
3. Choisir le lieu sûr de la restauration réelle : avec la seule clé publique, l'agent peut chiffrer mais pas déchiffrer. Le test de déchiffrement doit donc se dérouler chez vous ou dans un environnement sûr explicitement autorisé, avec remontée de résultats sans secret.
4. Après création des volumes, réussir les contrôles réels puis obtenir votre **autorisation distincte de publication**. Aucun push/upload de volume n'est autorisé maintenant.

## Branche et garanties

Travail conservé sur la branche dédiée existante `arena/a03f64da-parisfit`. La session n'autorise pas une nouvelle branche ; aucune créée ou changée. Aucun original modifié, aucune ressource/ref supprimée, aucune purge, modification de visibilité, fusion, dépense ou déploiement. Aucun transfert sortant, commit ou push pendant Phase28.

Les rapports historiques déjà publics et ceux que certains workflows CI exportent restent une exposition distincte ; l'exclusion du paquet Pages ne les rend pas privés. Une future archive chiffrée ne protégera pas rétroactivement les copies publiques.
