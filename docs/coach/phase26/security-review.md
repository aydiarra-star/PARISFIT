# Sécurité des archives — Phase26

## Mesures exécutées

- Pas de lecture ni archivage de la configuration d'authentification Git, `.git/credentials`, `.git/config`, `.netrc`, `.env` ou jetons de session. Le bundle inclut uniquement les objets/références Git, pas les secrets de configuration locale.
- Scan des **octets restaurés**, et non uniquement des noms : 1 783 fichiers de travail, 1 135 blobs historiques et 884 membres d'archives imbriquées, soit **3 802 unités**.
- Six familles de motifs : matière de clé privée, jetons GitHub, identifiants AWS, clés API Google, affectations de credentials littéraux, URL signées/tokens de query string.
- Résultat : **aucune correspondance** dans ce périmètre. Les rapports n'impriment pas de valeur sensible. Les URL signées éventuelles de téléchargement et stderr brut ne sont pas archivés.
- Tentatives Actions échouées conservées comme échecs, jamais comme archives valides. Aucun upload, aucun nouveau lien de partage, aucun compte ni permissions modifiés.

## Limites qui interdisent une garantie absolue

Un scan de motifs ne prouve pas l'absence de tout secret : formats inconnus, fragments, chiffrement, constructions dynamiques et compression récursive peuvent échapper à la détection. Inspection d'un niveau d'archive seulement. `.cache/phase8/xrender.tar.gz` est vide/invalide ; ce défaut historique est conservé. Les dépendances binaires ne font pas l'objet d'une analyse sémantique complète.

Contacts professionnels publics, auteurs de commits et données pseudonymes de mouvement restent des données potentiellement personnelles ; ne pas assimiler une licence de code/dataset à une autorisation illimitée de traitement ou republication. Les preuves négatives et licences/conditions des phases précédentes sont conservées. Aucun consentement supplémentaire inventé.

La revue Phase25 avait identifié les distinctions Rocketbox MIT, conditions CMU, dataset Michaud CC BY, article/dataset AB01 et notices à restrictions Phase7. Aucune nouvelle vérification juridique complète de chaque vidéo/fichier n'est prétendue. Les archives sont **internes, non chiffrées dans le sandbox et non autorisées au partage**.

## Décision de sécurité

`security-scan.json` indique `certifiesNoSecret: false`, `sharingAuthorized: false`. Un résultat sans correspondance est un contrôle utile, **pas un certificat de contenu partageable**. Une revue ciblée des exceptions, une destination privée autorisée et, si nécessaire, chiffrement/gestion de clés par le propriétaire sont requis avant tout transfert.

Si un secret est découvert ultérieurement : suspendre le transfert, prévenir le propriétaire sans reproduire le secret, préparer sa révocation/rotation avec son autorisation. Purger Git seul ne le révoque pas. Aucun de ces actes n'est réalisé ici.
