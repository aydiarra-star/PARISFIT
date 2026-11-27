# Cinq passages absents : étude et méthode de création, pas de faux clips

Inventaire renouvelé du sous-arbre Animations Rocketbox à la révision MIT figée : **471 fichiers FBX**, arbre non tronqué. La recherche par noms retient 30 fichiers de crouch/sit/stand, principalement assis/debout sur chaise/table. Voir `source-inventory.json`. Le nombre de fichiers n’équivaut pas à un nombre de gestes uniques. L’inspection des noms n’est pas un visionnage exhaustif : elle ne prouve pas qu’aucune autre bibliothèque appropriée n’existe.

Aucune source exacte pour les cinq passages ci-dessous n’a été acquise avec une provenance exploitable ici. Les alternatives étudiées précédemment restent documentées dans `../phase3/SOURCES.md` : LaFAN1 incompatible avec usage commercial/adaptation ; MoCapAct à sélectionner et retargeter, pas un pack de ces gestes ; pas de redistribution Mixamo présumée. Aucun achat ni commande passée.

## Brief de capture à faire valider, non exécuté

| Passage | Définition à fixer avec le professionnel | Données nécessaires et difficulté principale |
|---|---|---|
| Accroupi → genoux | Quel accroupissement, quelle jambe initie, demi-genou ou deux genoux, appui des mains autorisé ? | Mesurer transfert de charge, contacts genou/orteils, trajectoire du bassin. L’accroupissement asymétrique Rocketbox n’est pas déjà une position à genoux |
| Genoux → sol | Définir « sol » : quadrupédie, décubitus ventral, dorsal ou latéral | Ce terme ne définit pas une pose unique. Capturer la séquence choisie avec mains/coudes visibles et aucun changement caché de côté |
| Sol → gainage | Départ ventral ou quadrupédie ; gainage sur mains ou avant-bras ? | Raccorder exactement la position des avant-bras/pieds du clip gainage ; recréer les appuis avant le soulèvement, sans faire traverser les poignets au sol |
| Allongé → assis | Départ dorsal, passage par le côté ou redressement frontal ; mains en support ? | Plusieurs stratégies ne sont pas interchangeables selon les capacités. Capturer avec choix professionnel, tête et colonne visibles, contact fessier suivi |
| Assis → debout | Assis au sol, pas sur une chaise ; relever via demi-genou ou autre stratégie ? | Besoin de déplacer les appuis sur plusieurs plans. Une animation chaise→debout ferait flotter le personnage au mauvais niveau |

## Pipeline réaliste proposé

1. Définir les sept poses de raccord dans la même scène/échelle/sol et sélectionner une stratégie accessible avec le professionnel. Ne pas annoncer de durée/cadence exacte avant la capture.
2. Filmer un démonstrateur consentant, plusieurs vues synchronisées, sol fixe, mains/pieds et corps entier visibles. Obtenir l’autorisation de redistribution commerciale de la captation et de ses dérivés, avec attribution/licence écrites.
3. Utiliser une capture corporelle adaptée ou un animateur à partir des références. Une reconstruction monoculaire ne mesure ni la profondeur ni les forces ; doigts et contacts nécessitent une reprise. Ne pas l’étiqueter mocap fiable sans preuve.
4. Retargeter en espace monde vers Rocketbox, préserver les segments, identifier les fenêtres de contact **avant** correction. Conserver les translations et rotations de transfert de poids issues de la démonstration.
5. Corriger les appuis sur les surfaces et vérifier les interpolations entre échantillons, genoux/coudes, bassin, doigts, contacts fessiers, récupération et interruptions. Tests 60 Hz et revue continue des trois vues/ralenti.
6. Raccorder pose **et vitesse** aux exercices, contrôler les passages dans les deux sens si nécessaires. Sans récupération approuvée, ne pas autoriser le parcours automatique.

**Résultat actuel :** cinq entrées `NOT_AVAILABLE`, aucune animation factice ni vidéo prétendant les montrer, aucune commande à un prestataire. Les points de définition ci-dessus sont à trancher avec le professionnel avant une capture ; ils ne bloquent pas les tests des deux sources déjà disponibles.
