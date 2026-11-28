# Demande aux auteurs — français

**EN ATTENTE DE VALIDATION HUMAINE — NON ENVOYÉE.** Envoi exclusivement sur décision de l’utilisateur ; aucun destinataire personnel inventé. Utiliser le contact officiel du déposant Florian Michaud, via la page du dataset ou son affiliation après vérification.

**Objet : Métadonnées de reconstruction S01/P001 — DOI 10.5281/zenodo.23979972, v1**

Bonjour,

Nous étudions la reproductibilité de S01/P001 pour PARISFIT, sans revendiquer une validation anatomique. Le README décrit un modèle générique avec 37marqueurs de laboratoire, tandis que le XML fourni contient 66marqueurs dont les noms diffèrent des 37labelsCSV. Pour éviter toute correspondance supposée, pourriez-vous fournir ou indiquer :

1. Le MarkerSet 37 original et la table officielle CSV→marqueurs anatomiques→marqueurs du modèle, avec distinction points cutanés/centres virtuels.
2. Le protocole de placement/palpation, coordonnées dans les repères anatomiques, offsets et conventions de nommage (notammentASIC, sacral_crest, forearm_centre).
3. Les transformations signées laboratoire↔plates-formes↔OpenSim, unités, origines des moments, géométrie des surfaces et synchronisation.
4. Le modèle OpenSim individualisé S01, s’il existe, et la version exacte du template.
5. L’application exacte de P1/P2/P3/Fem/Tib/Foot : axes, corps, isotropie, référence, ordre des opérations et traitement des autres segments/masses/inerties.
6. La procédure de registration des marqueurs, la pose statique, les poids et les contraintes utilisées.
7. Les configurations de scaling, simulation ou IK et scripts d’export, ainsi que le DOI/préprint et suppléments de l’article associé.
8. La confirmation des conditions de citation/réutilisation, y compris commerciale sous CC BY4.0 pour les données, et les notices/droits propres au modèle et à ses composants.

Une réponse publique versionnée liée au dépôt serait idéale. Nous ne demandons ni identité des participants, ni signature, ni nouvelle vidéo privée. Aucun calcul IK ne sera entrepris à partir de correspondances seulement plausibles.

Merci pour votre aide.

Référence technique : `LaiUhlrich2022_symmetric.osim`, SHA256 `42eca458626f42aa1e49d5925e14ec3c16fe81324293bacece643e11319ddbd9`. Dataset : https://doi.org/10.5281/zenodo.23979972 .
