# Hébergement GitHub dans le même dépôt

Sources officielles S1–S4 dans `sources.md`. Les seuils ne constituent pas un contrat de sauvegarde ou un quota réservé.

| Mode | Limites documentées / contraintes | Pertinence |
|---|---|---|
| Git ordinaire | >50 MiB : avertissement ; >100 MiB : blocage ; navigateur : 25 MiB max ; push : 2 Go | Volumes de **20 MiB** compatibles, bien sous les limites ; aucun LFS requis |
| Taille globale Git | S1 recommande idéalement <1 Go, fortement <5 Go ; S2 recommande un maximum sur disque de 10 Go | Ne pas interpréter 10 Go comme autorisation d'y empiler des backups ; viser petit et contrôler la croissance |
| Releases du même dépôt | S3 : jusqu'à 1 000 pièces, chacune <2 GiB ; pas de plafond total/bande passante annoncé sur cette page | Alternative pour éviter la croissance Git ; actifs non inclus dans `git clone`/bundle, suppression possible, téléchargement à vérifier |
| Git LFS | Quotas inclus, consommation stockage et bande passante ; dépassement bloqué ou facturé selon budget | **Non retenu** ici pour ne dépendre ni d'un quota inconnu ni d'une facturation possible |
| Artefacts Actions | Rétention/expiration et accès distincts ; échecs constatés Phase26 | Pas un stockage durable garanti, pas requis pour restaurer |

## Estimation du périmètre actuel

`capacity-estimate.json` utilise les tailles réelles Phase26 ; aucune archive originale chiffrée pour le calcul. L'estimation ajoute une marge d'en-tête et de tags par blocs, pas une mesure d'exécution.

| Archive | Taille avant chiffrement | Volumes estimés de 20 MiB |
|---|---:|---:|
| Projet courant | 47,018 MiB | 3 |
| Données/cache | 293,490 MiB | 15 |
| Bundle historique | 29,518 MiB | 2 |
| Preuves Phase26 | 0,258 MiB | 1 |
| Total | environ **370,28 MiB** | **21** |

Le découpage est fait par archive, non sur une concaténation globale. Ce volume ponctuel est raisonnablement compatible avec les plafonds techniques Git, mais doit être ajouté à la taille existante et vérifié sur l'artefact chiffré réel avant publication. Le plan du compte et l'usage LFS ne sont pas connus. Les 1,64 Go de contenus Actions non récupérés ne sont **pas inclus** ; les ajouter changerait nettement l'évaluation.

## Gratuité réaliste, pas stockage illimité

Git public ordinaire peut recevoir cet instantané sans achat ni LFS, sous les conditions et limites du service. Aucun test d'upload réel réalisé ; aucune garantie d'acceptation ou disponibilité perpétuelle. GitHub indique expressément que Git n'est pas conçu comme outil de sauvegarde. Ne pas détourner un dépôt en miroir quotidien de toutes les machines ou dépendances.

Le chiffrement est aléatoire : rechiffrer la même archive crée de nouveaux blobs. Supprimer les volumes à HEAD ne libère pas leurs anciennes versions sans réécriture d'histoire. Trois snapshots intégraux ajouteraient déjà environ 1,1 GiB, hors dépôt existant. Empêcher la récursion du bundle contenant les snapshots précédents ; décider d'un périmètre incrémental explicite avant toute deuxième campagne.

Pour une fréquence supérieure à un archivage initial contrôlé, préférer une évaluation de Releases **dans le même projet** plutôt qu'accumuler les blobs. Ce n'est pas une copie indépendante de GitHub et ce n'est pas « stocké dans Git ». Aucun asset ni tag de release créé.

## Quatre notions distinctes

- **Présence dans Git** : objet accessible via refs/histoire et normalement récupérable par clone complet ; pas nécessairement présent dans un clone superficiel ou filtré.
- **Rétention distante** : persiste au-delà du sandbox tant que dépôt/compte/service et objets sont conservés ; pas une promesse d'archivage éternel.
- **Copie indépendante** : support ou domaine de panne distinct. Même dépôt + release + clone éphémère ne suffisent pas.
- **Chiffrement** : protège la confidentialité des nouveaux octets contre un lecteur sans clé ; ne protège ni la disponibilité, ni le compte, ni les originaux publiés antérieurement.

Risques résiduels : perte/suspension de compte, suppression dépôt/refs/assets, panne ou changement de conditions, remplacement malveillant de manifeste, perte ou vol de clé. Garder une copie locale personnelle des volumes et des reçus si possible, sur un support déjà possédé ; ne pas présenter ce support comme acquis tant qu'il n'est pas vérifié.
