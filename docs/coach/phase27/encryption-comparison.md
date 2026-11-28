# Chiffrement : age et GPG

| Critère | age / rage | GPG / OpenPGP |
|---|---|---|
| Logiciel libre | age Go, rage Rust ; interface simple | GnuPG, écosystème OpenPGP plus ancien et large |
| Modèle conseillé | Destinataire X25519 et identité privée indépendante | Clé publique/privée, sous-clés, chiffrement et éventuelle signature |
| Phrase secrète | Mode disponible, mais mot de passe faible attaquable hors ligne | Mode symétrique disponible, mêmes exigences de robustesse |
| Gestion propriétaire | Petite identité dédiée, ne pas réutiliser une clé SSH de connexion | Trousseau et export de sauvegarde de clé privée à gérer soigneusement |
| Signature / auteur | Chiffrement authentifié ne prouve pas l'identité de l'expéditeur ; SHA256 seul non plus | Signature détachée possible, à vérifier avec une clé de confiance indépendante |
| Gros fichiers | CLI à flux adaptée ; découpage externe après chiffrement | CLI à flux adaptée ; découpage externe après chiffrement |
| Sans Actions | Oui, terminal local | Oui, terminal local |
| Test ici | **PASS via pyrage 1.4.0**, format age ; pas CLI officielle | Non installé, non testé |

## Compatibilité observée

Linux/Python 3.11.2. Ni `age`, `age-keygen`, GPG ni Go disponibles initialement. Tentative du binaire officiel age v1.3.2 depuis GitHub : **échec réseau URLError**, documenté, pas exécuté. Pas de compilation Go supposée possible.

Alternative effective : roue précompilée **pyrage 1.4.0** obtenue depuis PyPI, installée seulement sous `.cache/phase27/lib`, sans modifier les dépendances de l'application. Son SHA256 correspond aux métadonnées PyPI ; ce contrôle n'est pas une signature de confiance indépendante. Bindings d'une implémentation age existante, pas une cryptographie maison.

La compatibilité croisée CLI Go ↔ pyrage est documentée par le format partagé mais **n'a pas été testée dans cet environnement**. Avant chiffrement d'originaux, répéter le petit test sur la machine propriétaire avec l'outil de restauration qu'il conservera. GPG reste une alternative, pas un second outil réputé validé sans test.

## Taille et découpage

Le test chiffre 10 240 octets de tar et produit 10 479 octets chiffrés. Il ne permet pas d'annoncer une vitesse ou une capacité maximale mesurée sur 300 MiB ou plusieurs GiB. Pour les vraies archives, privilégier les interfaces à flux (`age` CLI ou API de fichier/flux dûment testée), et prévoir la place de l'archive, du chiffré et des fichiers restaurés. L'API mémoire utilisée au PoC n'est pas le choix validé pour de grandes archives.

Les tailles envisagées (environ 30, 47 et 293 MiB par archive) ne nécessitent pas un algorithme spécifique ; le plafond pratique sera l'espace disque, le transport, les quotas et la taille des volumes. Aucun plafond cryptographique « illimité » n'est promis.

Découper le chiffré en volumes ordonnés, puis vérifier tous les hashes avant réassemblage. Un morceau manquant rend cette archive impossible à restaurer ; le découpage ne donne ni redondance ni réparation. Une corruption ou mauvaise clé doit bloquer l'usage du résultat.

## Conservation de la clé

Créer l'identité réelle **sur l'appareil du propriétaire**, hors du dépôt et des répertoires synchronisés publiquement. Garder au moins deux copies indépendantes de la clé si des supports déjà possédés le permettent : gestionnaire local déjà disponible, support personnel chiffré, copie papier soigneusement vérifiée et rangée séparément. Aucune disponibilité de ces supports n'est supposée ni achat demandé. À défaut de conservation indépendante de la clé, la solution n'est pas acceptable.

Ne jamais envoyer la clé/phrase secrète au chat, à GitHub, à Actions ou à l'agent. Ne pas la mettre en argument de commande, variable d'environnement persistante ou historique shell. La clé publique de destinataire peut servir au chiffrement sans transmettre la clé privée, mais elle doit être vérifiée indépendamment.

Perdre la clé et ses sauvegardes peut rendre les archives définitivement irrécupérables. Compromettre la clé peut exposer toutes les archives publiques copiées auparavant ; changer de clé et rechiffrer plus tard ne révoque pas ces anciennes copies. Le PoC utilise une clé jetable en mémoire seulement, aucune clé de production n'a été créée.
