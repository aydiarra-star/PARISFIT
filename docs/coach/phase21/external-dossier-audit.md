> Phase21 — préparation locale, aucune transmission. Référence : `5eeb144aaa1c1f47f956776fa5a6dc1c1425fd9a`. Date de session : 2026-11-27 ; les horodatages CI sont ceux retournés par GitHub et ne sont pas réécrits.

# Audit du dossier externe20

## Périmètre et méthode

Les7 fichiers de `phase20/external` ont été lus ;6 empreintes du manifest vérifiées, et4 documents communs comparés aux internes après les seules substitutions prévues d'URL/navigation. Contrôle des liens épinglés dans les objets Git, du journal original et des définitions de marqueurs. [Résultats reproductibles](audit-results.json), commande : `.venv/bin/python tools/submission-readiness/audit.py`. Aucune archive réacquise, aucun traitement source exécuté.

| Point | Constat et preuve | Réserve / action |
|---|---|---|
| Cohérence interne/externe | Dossier, matrice15, questions11 et formulaire identiques après substitutions documentées ; hashes20 conformes | README simplifie les renvois partage/portes, mais rappelle les interdictions |
| AB01/Static, C3D et version | Sources17/19 citées, hashes dans le dossier ; Motive3.0.3 Final est une déclaration de fichier | Pas une revalidation de capture ou de placement |
| Journal | SHA256 du grand log identique ; lignes13369/13555 concordent avec AB01/Squat/1 et2948 lignes | Résumé explicitement non verbatim ; ne prouve pas la validité anatomique |
| Marqueurs |57 définitions,44 Confirmé/13 plausibles dans registre17 | Ni57 placements validés ni57 centres articulaires |
| Identité / confidentialité | AB01 pseudonyme utile ; pas d'identité civile, coordonnées participant ou profil Windows dans les fichiers externes | Pseudonyme ≠ anonymisation garantie ; liens vers preuves internes à minimiser séparément |
| Secrets | Aucun motif de jeton, clé privée, URL signée, email ou chemin de profil détecté dans le paquet ; relecture du contenu | Contrôle borné, pas certification de sécurité ; ne pas inclure les caches/logs CI |
| Redistribution | Extensions.md/.csv/.json seulement, aucune archive/C3D/modèle/photo/figure de l'article jointe | Licences différentes selon objet ; ajouter la note21 obligatoire |
| Limites scientifiques |4.21cm statique, pas squat ; forces≠contact complet ;200/1000Hz≠sync ; pas de transfert Rocketbox validé | Toutes conservées, aucune simplification scientifique requise |
| Validation revendiquée | Aucun avis reçu et aucune validation anatomique annoncés ; réponses nulles | A porte sur la préparation documentaire uniquement |

## Vérification des références scientifiques

Consultation publique (sans contacter d'auteur) :
- [Article PMC12717423](https://pmc.ncbi.nlm.nih.gov/articles/PMC12717423/), en-tête : *Whole-body optical marker and ground reaction force data of healthy humans performing non-cyclic activities*, Mohsen Alizadeh Noghani, Sebastian Green, Edgar Bolívar-Nieto ; Scientific Data12:1971(2025), DOI10.1038/s41597-025-06227-7. Identité bibliographique conforme au dossier.
- [API dataset28689221](https://api.figshare.com/v2/articles/28689221) : titre/auteurs concordants, version1, DOI10.7274/28689221.v1, licence CC BY4.0. Le DOI sans suffixe du dossier est le DOI conceptuel, pas une erreur ; utiliser.v1 pour la version examinée.
- **Précision de droits découverte : l'article affiche CC BY-NC-ND4.0**, distincte de CC BY4.0 des données. Le dossier20 n'affirmait pas que l'article était sous CC BY, mais la distinction doit devenir explicite. La [note de soumission](submission-addendum.md) corrige cette ambiguïté sans modifier20. Ne pas reproduire/adaptation de figures ou texte de l'article en présumant une licence commerciale.
- Guide OptiTrack Biomech57 : référence fournisseur déjà examinée19 ; adresse conservée, non certification de sa stabilité ou de la pose individuelle. Les contradictions sont conservées, pas corrigées implicitement.

## Portée des liens et composition autorisable

Les liens GitHub pointent sur des objets existants au commit25ebee0 ; leur existence n'établit pas l'accès d'un destinataire externe. Aucun accès privé testé ni accordé. Certaines preuves liées contiennent des chemins de laboratoire ou du contexte non nécessaire : **ne pas envoyer tout le dépôt ou archive-probe.json automatiquement**. Fournir d'abord le paquet minimisé et la note21 ; organiser les extraits complémentaires seulement après accord et nouvelle minimisation.

Conclusion : pas de risque bloquant identifié dans le paquet textuel contrôlé, sous réserve de joindre la note21 et de conserver les limites de partage. Données scientifiques nécessaires maintenues. L'autorisation utilisateur, le destinataire réel et tout budget restent absents ; c'est attendu avant soumission, pas un avis professionnel.
