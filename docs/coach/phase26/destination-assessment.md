# Destinations — Phase26

**Conclusion : aucune destination privée, durable et autorisée au transfert n'est vérifiée. Aucun transfert effectué.**

| Destination | Vérification effectuée | Gratuité / durabilité / décision |
|---|---|---|
| Dépôt PARISFIT existant | API : public, accès administrateur déclaré, `has_pages: false` | Pas une destination privée. Aucun changement de visibilité autorisé. Les modifications Phase24–26 non poussées n'y sont pas sauvegardées. |
| Autres dépôts visibles | Pagination `user/repos`, 19 dépôts visibles, zéro privé ; aucun contenu des autres projets inspecté | Aucun dépôt privé disponible **dans le périmètre de l'intégration**. Ne prouve pas que le compte ne possède aucun autre dépôt privé. Ne pas utiliser un dépôt sans autorisation. |
| Services connectés à la session | Aucun annoncé ; connecteur GitHub non pris en charge, CLI `gh` fonctionnel en lecture | Aucun stockage privé connecté n'est attesté. Aucune recherche de credentials dans l'environnement. |
| Disque du sandbox | Montage `/` sur disque ext4 ; environ 13,8 Go disponibles au contrôle | Utilisable pour préparer/restaurer localement. Ni disque utilisateur ni sauvegarde durable indépendante ; `.cache` exclu des snapshots persistés. |
| Snapshots de l'espace de travail Arena | Les rapports et scripts hors cache sont conservés comme travail de session | Pas une archive externe indépendante restaurée ; ne couvre pas les archives `.cache`. Aucune garantie de rétention inventée. |
| Disque ou espace privé déjà possédé par le propriétaire | Non connecté, ni quota ni permissions testés | Piste gratuite possible, **non disponible vérifiée**. Nécessite désignation, accès et autorisation explicite. |

Le compte identifié est `aydiarra-star`. Le forfait est **non exposé** par l'API : ne pas affirmer qu'il est Free/Pro ou qu'un quota est disponible. GitHub documente des dépôts privés gratuits, mais la possibilité théorique d'en créer un n'est ni une destination existante ni une autorisation ; création interdite pendant cette phase. Conditions documentées en Phase25 `sources.md`, pas d'abonnement souscrit.

Les endpoints deploy keys/invitations étaient refusés en Phase25 ; ne pas prétendre à un audit exhaustif des accès. Un espace privé signifie un contrôle d'accès vérifié, pas seulement un lien difficile à deviner.

Preuves : `destination-evidence.json`, `storage-mount.txt`. Seuls comptages des autres dépôts conservés, pas leurs noms. `gh --slurp` n'étant pas disponible dans cette version de CLI, la collecte a été refaite avec décodage des pages JSON concaténées ; le premier essai n'a créé aucune ressource distante.
