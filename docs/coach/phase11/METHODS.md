# Phase11 — protocole comparatif figé

**Trois diagnostics sur la même source, aucune admission automatique.** CMU14_06, fenêtre8,6–11s,145poses à60Hz, Rocketbox Sports_Male_04 (80os,22correspondances). Le clip conserve le nom technique `phase9-cmu-control` pour les contrats ; les fichiers sont isolés par dossiers A/B/C. Ce nom ne signifie pas validation phase9/10/11.

## A — direct actuel

Reproduction du calcul phase10 : delta de rotation source depuis la pose artificielle0, offset directionnel source/cible, heading initial, FK et déplacement de racine multiplié par0,9469891624. Les offsets incluent des vecteurs nuls dans la colonne : ils sont conservés ici **uniquement pour reproduire la référence défectueuse**. Leur résultat numérique Blender n'est jamais une orientation anatomique valide.

## B — calibration morphologique par directions de segments

Même déplacement racine et mêmes timestamps, longueurs natives Rocketbox conservées, aucun étirement ni lissage. Pour cuisses, jambes, pieds, bras et avant-bras : orientation cible calculée à partir de la direction source courante, appliquée à la direction repos cible correspondante. La longueur de la cible remplace donc celle de la source pour la chaîne FK ; il ne s'agit pas d'une copie de positions avec membre extensible.

Pour les autres correspondances, conjugaison du delta source dans le heading : `H × Qsource(t) × inverse(Qsource(0)) × inverse(H)` appliqué à la rotation cible de repos. Aucun offset de direction nulle utilisé dans B/C. Le facteur racine reste celui de A afin d'isoler cette intervention. Cette méthode modifie conjointement conventions de rotation et calibration directionnelle : l'amélioration éventuelle n'est pas attribuable à une seule cause sans ablation supplémentaire.

**Limite importante :** une direction 3D ne détermine pas la torsion axiale. L'alignement court choisi pour les membres ne conserve pas nécessairement la torsion humaine. Les subdivisions de colonne restent des correspondances approximatives. Pas de nouvelle longueur inventée pour les segments source coïncidents.

## C — B + cinématique à deux segments et hypothèse d'appuis

Reprend B, puis chaque jambe résout analytiquement hanche→genou→cheville avec les longueurs cible. Cible de cheville = déplacement hanche/cheville source multiplié par le rapport des longueurs de chaîne ; plan de flexion issu du genou source. Une portée impossible est bornée à l'enveloppe des deux segments et son résidu est enregistré (pas effacé).

Une fenêtre de vitesse du pivot pied source<80mm/s entre deux poses déclenche une **hypothèse de contact**, ancre la cheville à sa position cible lors de l'entrée et libère l'ancre lorsque le seuil est dépassé. C'est un test volontairement incomplet : aucune mesure de force, aucun patch plantaire validé, aucune confirmation de hauteur de sol, et un pied lent en l'air peut être mal classé. Donc cette version de C n'est **pas** un système de contacts admissible. Les activations sont toutes consignées ; les changements de régime ne sont pas lissés. Ni le bassin ni le sol ne sont projetés pour absorber le résidu.

Aucun plafond physiologique de genou/torsion ne fait autorité dans cette expérience : amplitudes et continuité restent soumises au validateur indépendant. Pas de mains verrouillées pour simuler des appuis inexistants.

## Mesures et limites

| Famille | Mesure | Nature |
|---|---|---|
| Trajectoires | RMS/max des22pivots face à la source avec heading, facteur global et placement racine **fixes** | Exact pour ces pivots numériques ; proxy de fidélité, biaisé par morphologie et subdivisions |
| Bassin | vitesse/accélération, continuité | Géométrie exacte de modèle, pas stabilité musculaire |
| Temps |145poses, pas, vitesse, accélération, variation quaternion | Dérivées discrètes, pas forces réelles |
| Appuis | minima de peau ; dérive sur fenêtres candidates | Peau exacte du modèle ; fenêtres/patches estimés |
| Sol | profondeur du point le plus bas de peau | Référentiel Y=0 non calibré par capture physique |
| ROM | angles3pivots, genoux, coudes, hanches/chevilles proxy, inclinaison tronc | Angles non signés, pas axes anatomiques cliniques |
| Torsions | incrément quaternion/global | Rotation3D mesurée ; torsion anatomique NON TESTÉE |
| Collisions | quelques paires de sphères de pivots | Candidats estimés ; intersection exhaustive des triangles NON TESTÉE |
| COM | poids fixes sur milieux de segments, enveloppe supposée des pieds | Estimation non anthropométrique validée |
| Reconstruction | préparation/descente/bas/remontée/stabilisation | À annoter humainement, pas de phases ni pauses synthétiques ajoutées |

Les seuils phase10 sont inchangés. Les scores ne se substituent pas à la revue des poses et de la source. Aucun recalage par frame pour diminuer les erreurs de trajectoire ; aucun filtrage passe-bas. Un résultat moins mauvais n'est pas un résultat admissible.

## Reproduction

Installer l'environnement natif Ubuntu/Blender du workflow. Depuis la racine :

```sh
for method in A B C; do
  blender --background --factory-startup --python-exit-code 1 --python tools/anatomy/export.py -- --method "$method"
done
# serveur HTTP dans un autre terminal : python -m http.server 3000 --bind 0.0.0.0
node tools/anatomy/check.cjs
FFMPEG_PATH=$(command -v ffmpeg) node tools/anatomy/capture.cjs
node tools/anatomy/diagnostic-video.cjs
python tools/anatomy/package.py
python tools/anatomy/test_metrics.py
```

Sortie autorisée exclusivement `.cache/phase11/{A,B,C}`. Les entrées sont verrouillées par SHA256. Chaque export est répété deux fois ; le hash doit rester identique. Le validateur est exécuté avant l'export de diagnostic. Chaque fichier reste `runtimeEnabled=false` / admission bloquée, avec licences dans son dossier. Ne pas copier ces GLB dans le runtime.
