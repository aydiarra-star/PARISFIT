# Reconstruction indépendante : périmètre défendable, pas substitut anatomique

**Décision :** des analyses de trajectoires cutanées sont possibles ; une reconstruction anatomique rigoureuse n’est pas démontrée. **REFUSÉ** de réutiliserH1/H2 comme squelette exact. **NON TESTÉ** pourIK et centres articulaires. **EN ATTENTE DE DOCUMENTATION** pour placement/repères ; **EN ATTENTE DE VALIDATION HUMAINE** pour un protocole indépendant.

## Observabilité : distinguer géométrie et anatomie

`observability.json` calcule le rang de la Jacobienne infinitésimale d’une pose rigide à6paramètres à partir de positions statiques médianes. Les groupes sont formés explicitement dans `tools/metadata-plan/analyze.py` d’après les labels, **pas déclarés anatomiquement calibrés**. Les distances internes sur150frames de rep1 exposent la non-rigidité possible. Le rang n’est pas un nombre deDOF anatomiques validés ; aucuneIK n’est résolue.

|Groupe technique|Points disponibles|Ce qui est observable sous hypothèse rigide|Ce qui ne l’est pas anatomiquement|
|---|---|---|---|
|Bassin|2ASIC+2sacral_crest|pose technique6D si constellation non colinéaire|axes anatomiques, centres de hanche, équivalenceASIS/PSIS|
|Tête|2temporal_bone+Skull_vertex|pose technique6D si non colinéaire|centre cervical, offsets anatomiques, articulationcou/tronc|
|Ligne épaules|2acromioclavicular_joint|position/direction de ligne, rang5|rotation autour de ligne, torsion du tronc, mouvement scapulaire|
|Chaque cuisse|trochanter+épicondyle latéral|ligne, rang5|torsion axiale, centres hanche/genou, axes condyliens|
|Chaque jambe|tubérosité tibiale+malléole latérale|ligne, rang5|torsion, centre/axe cheville et genou ; épicondyle fémoral ne devient pas point tibial|
|Chaque bras|deltoid_tuberosity seul|position du point, rang3|orientation ; ne pas coller épaule et olécrâne au même segment sans protocole|
|Chaque avant-bras|olécrâne+forearm_centre+ulna_head|pose technique si3points non colinéaires et rigides|point«centre» indéfini, tissus mous, pronosupination et relation radius/ulna|
|Chaque main|2têtes métacarpiennes|ligne, rang5|rotation axiale, orientation complète ; tête ulnaire appartient à l’avant-bras|
|Chaque pied|talon+1er/5emétatarsiens|pose technique si non colinéaire|repère anatomique, centre cheville, surface semelle ; orteil distal exclu du pied rigide|

Avec des coordonnées locales **connues**, un point contraint3combinaisons, deuxpoints distincts5, troispoints non colinéaires6. Ici, positions locales osseuses et relation peau/os sont justement inconnues. Fixer une pose technique de référence lève une convention numérique, pas cette ambiguïté anatomique. Les39coordonnées du modèle ne sont donc pas qualifiées par le rang de ces groupes. Aucun test de rang de Jacobienne articulaire du modèle individualisé n’est revendiqué.

## Exploitable maintenant

Trajectoires, continuité, distances et angles de landmarks explicitement nommés ; comparaison aux phases annotées ; composantes et chargement des plates indépendamment. Conserver les données originales et incertitudes. Ne pas estimer une localisation de centre à partir d’une force seule, ni réduire un résidu en déplaçant des pieds.

## Incertitudes non résolubles par les seuls CSV

Placement/palpation exact, compensation des tissus mous, centres et axes articulaires, pose de calibration anatomique, identité des points ambigus, historique d’occlusion/gap-filling, repèresF/M et synchronisation matérielle. Des dérivées plus lisses ne permettent pas de retrouver ces informations perdues. La quantification statistique/clinique de ces erreurs resteNON TESTÉE ; pas d’intervalle95% inventé.

## Si les auteurs ne peuvent compléter le dossier

1. Définir avec un biomécanicien le domaine admis (p.ex. membres inférieurs seulement), la méthode de centres/axes et les degrés de liberté retenus, avant optimisation.
2. Nouvelle calibration anatomique : landmarks médiaux/latéraux et bassin palpés selon protocole explicite, clusters techniques par segment, statique, mouvements fonctionnels de calibration adaptés si la méthode les exige ; documenter offsets, précision et reproductibilité inter-opérateur.
3. Calibration de laboratoire : axes signés, origine, géométrie/orientation de chaqueplate, zéro, conventionsF/M et trigger vérifié. Préparation, cycle complet et stabilisation finale réellement capturés.
4. Autorisation écrite de capture et de réutilisation, y compris commerciale le cas échéant ; pas de publication de données privées. Reprendre le cadrePhase12 sans achat ou réservation automatique.
5. Évaluer incertitudes et validation indépendante ; un professionnel fixe les critères avant mesure.

Une calibration d’un **nouveau participant** ne calibre pas rétroactivementS01. Même une recapture deS01, si possible légalement, nécessite démontrer le lien aux placements de la session d’origine. À défaut, la nouvelle acquisition devient une nouvelle source indépendante, sans réécrireMichaud2026.
