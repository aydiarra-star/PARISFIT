# Vérifications et conservation des résultats

## Contrôles locaux

- `npm test` : PASS, y compris contrôles antérieurs et contrat Phase17.
- Tests Python : 7 tests passifs nouveaux, 8 contrats Phase14, 5 tests Phase15 : PASS.
- Page Phase17 : sept livrables dépliés, table des 57 marqueurs, images et liens locaux, à 320/390/768/1200 px : PASS Chromium.
- Suite historique `npm run test:browser` : toutes les étapes chaînées ont atteint leur PASS, jusqu’au dernier test de galerie Phase7. Le premier appel de suivi a dépassé 180 s ; le processus a continué, sans seconde exécution concurrente. La fin du journal et la disparition du processus ont été vérifiées. Cette suite rejoue les actifs préexistants : aucun mouvement Notre Dame ni nouvelle animation produit.

## Deux sorties historiques régénérées, pas remplacées

Les tests historiques réécrivent quelques rapports. Deux ont changé pendant cette exécution :

- [legacy-mobile-rerun.json](legacy-mobile-rerun.json) conserve les mesures variables de temps, FPS logiciel et mémoire. Elles ne sont pas des mesures de téléphone physique.
- [legacy-transition-rerun.json](legacy-transition-rerun.json) conserve une différence plus importante du diagnostic historique `crouch-to-stand` : vitesse maximale1,185711→1,810210m/s et variation de hauteur du bassin−0,464054→+0,464054m environ. Le statut reste **HOLD** et toutes les réserves restent visibles. L’origine de cette différence de lecture/échantillonnage historique n’est pas établie ici : **le PASS navigateur ne prouve pas une reproduction numérique identique de ce diagnostic**.

Les rapports originaux des phases2/3 sont restaurés exactement à leur contenu du commit de référence, après copie des nouvelles sorties dans ce dossier. Aucun ancien résultat négatif effacé. Ni runtime ni données des mouvements modifiés pour faire passer les tests. Cette divergence historique n’est pas utilisée pour qualifier AB01 ; elle reste un point à examiner séparément si ces anciens résultats sont réutilisés scientifiquement.

`protected-baseline.json` et le testNode comparent **552 fichiers préexistants protégés**, dont l’application, Rocketbox, les données et documents précédents. Les nouveaux rapports n’écrasent pas ces preuves. Les seules extensions prévues hors Phase17 sont les tests, leurs scripts et les commandes CI.

## Limite des tests

Aucun test ne produit d’IK, de modèle individualisé ou d’animation Notre Dame. Les tests de structure, lecture, géométrie descriptive et affichage n’accordent aucune admission anatomique. Aucun examen professionnel et aucun essai physique sur iPhone Safari/Android Chrome obtenus. La référence CI finale se trouve dans le compte rendu de livraison et la PR11.
