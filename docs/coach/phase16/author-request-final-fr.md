# Demande finale — français

**Prête pour décision d’envoi par l’utilisateur. NON ENVOYÉE. Aucun contact ni réponse obtenue.**

**Objet : Reproductibilité S01/P001 — MarkerSet et scaling, dataset 10.5281/zenodo.23979972 v1**

Bonjour Dr Michaud et collègues,

Nous examinons la reproductibilité de S01/P001 pour PARISFIT. S01 est le participant anonymisé ; P001 désigne sa première série de squats, et non un autre participant. Notre analyse cible `participants/S01/P001_markers.csv.gz` et la capture statique du même dossier. Le README décrit un modèle générique contenant les 37 marqueurs du laboratoire ; le XML fourni expose 66 marqueurs avec des noms différents des 37 labels CSV. Nous souhaitons comprendre cette différence sans supposer de correspondances anatomiques.

Pourriez-vous nous orienter vers les pièces suivantes, si elles existent ?

1. **MarkerSet et placement :** le MarkerSet de capture et celui du modèle effectivement utilisés, leur table de correspondance officielle, le protocole de palpation, les offsets et repères locaux. Pourriez-vous préciser notamment `ASIC`, `sacral_crest` et `forearm_centre`, ainsi que les marqueurs exclus et les centres virtuels ? Cela permettrait de distinguer un point cutané d’un centre articulaire.
2. **Configuration S01 :** le modèle individualisé S01, ou le template exact et les fichiers/scripts permettant de le reconstruire. Le XML distribué est-il le template utilisé avant individualisation ?
3. **Six facteurs :** pour S01 nous lisons P1=1,07737, P2=1,08037, P3=1,08637, Fem=1,07018, Tib=1,08885 et Foot=1,14237. Confirmez-vous leur référence, les axes/corps concernés, l’isotropie éventuelle, l’ordre d’application et le traitement des autres segments, masses et inerties ? S’agit-il d’entrées d’un surrogate ou d’un scaling complet rejouable ? Ces précisions sont nécessaires pour ne pas attribuer les facteurs à de mauvais axes.
4. **Registration :** pose et fenêtre statiques, placement des marqueurs du modèle, poids, contraintes et éventuels déplacements manuels. Cela distinguerait la mise à l’échelle du squelette de l’ajustement des marqueurs.
5. **Repères et acquisition :** axes signés, unités et transformations laboratoire/plates-formes/OpenSim, origine des moments, géométrie des plates, synchronisation et traitements des lacunes/filtrage. Cela permettrait de comparer correctement trajectoires et forces.
6. **Reproduction des calculs :** configurations de scaling, IK ou simulation utilisées et scripts d’export ; article associé, DOI/préprint et suppléments. Nous conserverons les paramètres et les limites plutôt que reproduire seulement un résultat visuel.
7. **Réutilisation :** attribution souhaitée et confirmation du périmètre CC BY 4.0, notamment pour un usage commercial des données, ainsi que les licences/notices distinctes du modèle et de ses composants.

Une réponse publique versionnée, liée au dépôt, serait idéale. Si une pièce n’existe pas ou ne peut être partagée, une indication de cette limite nous aiderait. Nous ne demandons aucune identité, signature de consentement ou vidéo privée de participant. Aucune IK ne sera lancée à partir de correspondances simplement plausibles.

Merci pour votre aide.

Référence : https://doi.org/10.5281/zenodo.23979972 ; modèle `LaiUhlrich2022_symmetric.osim`, SHA256 `42eca458626f42aa1e49d5925e14ec3c16fe81324293bacece643e11319ddbd9`.
