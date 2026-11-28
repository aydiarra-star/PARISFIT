# Procédure propriétaire — sauvegarde et récupération

**Procédure future, non exécutée sur les originaux.** Aucun besoin de GitHub Actions ou d'un deuxième dépôt. Choisir et vérifier le logiciel sur la machine propriétaire avant d'utiliser une vraie clé.

## 1. Préparer la clé, uniquement chez le propriétaire

Installer age depuis la source officielle ou un gestionnaire de confiance ; vérifier la provenance/version et conserver l'outil compatible. Les commandes suivantes sont documentées pour la CLI age, **non testée dans ce sandbox**. Ne jamais copier leur sortie secrète dans le chat.

```sh
# Sur votre ordinateur, hors du dépôt et de toute synchronisation publique :
umask 077
KEYDIR="$HOME/.local/share/parisfit-private-key"
mkdir -p "$KEYDIR"
test ! -e "$KEYDIR/identity.txt" || exit 1
age-keygen -o "$KEYDIR/identity.txt"
age-keygen -y "$KEYDIR/identity.txt" > "$KEYDIR/recipient.txt"
```

Vérifier que KEYDIR est bien **en dehors de tout dépôt Git**. `identity.txt` est SECRET ; `recipient.txt` contient seulement le destinataire public. Faire une sauvegarde indépendante de l'identité et tester sa lecture sur un fichier fictif. Une copie papier doit être contrôlée après transcription. Si aucun endroit indépendant pour conserver la clé n'est accepté, **arrêter** : une archive seule sans clé récupérable est inutilisable.

Une protection de l'identité par phrase secrète est possible, à évaluer selon l'appareil. Ne pas placer la phrase dans un script, variable d'environnement ou commande ; utiliser une saisie interactive locale. Ne pas se reposer uniquement sur la mémoire humaine. Aucune identité de production n'a été créée pendant Phase27.

## 2. Après autorisation : préparer l'enveloppe et chiffrer localement

Choisir les sources et vérifier le périmètre (dont manques Actions). Inclure à l'intérieur de l'enveloppe les fichiers/archives, leurs tailles/SHA256, les refs et instructions de restauration. Exclure clés, tokens, données d'authentification, anciens volumes chiffrés et sorties temporaires. Les manifestes internes peuvent contenir des noms scientifiques ; ne pas les publier automatiquement en clair.

Compresser avant chiffrement ; utiliser des chemins de sortie neufs, séparés des sources. Exemple avec un fichier `envelope.tar.gz` déjà préparé et son manifeste interne :

```sh
test ! -e envelope.tar.gz.age || exit 1
age -R "$KEYDIR/recipient.txt" -o envelope.tar.gz.age envelope.tar.gz
python tools/encrypted-backup/volumes.py split envelope.tar.gz.age volumes-neufs
```

Avant chiffrement, vérifier le destinataire public contre la copie indépendante du propriétaire, pas seulement un fichier modifiable dans Git. Conserver hors Git un reçu de référence du SHA256 chiffré ou une signature à clé de confiance indépendante : un attaquant qui remplace ciphertext **et** manifeste dans le dépôt ne doit pas définir seul la « bonne » sauvegarde.

Effectuer immédiatement un déchiffrement/restauration de contrôle, puis seulement demander l'autorisation de publier les volumes. Les volumes réels ne doivent être ajoutés/poussés qu'après cette autorisation et contrôle de taille. Il ne suffit pas de placer une clé dans `.gitignore` : elle doit rester hors du dépôt dès sa création.

## 3. Récupérer depuis le même dépôt

Sur la machine propriétaire, récupérer tous les volumes du snapshot et son manifeste, via un clone approprié ou téléchargement explicite. Une archive ZIP GitHub ne contient que le tree de la ref choisie ; elle n'inclut pas nécessairement les versions historiques désirées ni les pièces Releases. En mode Releases, télécharger chaque asset séparément. Vérifier nombre, taille et SHA256 de chaque volume.

Comparer le manifeste/hash global avec le reçu indépendant. Sans reçu indépendant, les hashes contrôlent l'intégrité par rapport au manifeste téléchargé, **pas l'authenticité de ce manifeste**.

```sh
python tools/encrypted-backup/volumes.py join volumes-neufs reassembled.age
# Ne jamais extraire directement le flux de déchiffrement dans les originaux.
test ! -e decrypted-envelope.tar.gz || exit 1
age -d -i "$KEYDIR/identity.txt" -o decrypted-envelope.tar.gz reassembled.age
```

Si `age` retourne un code non nul, ne pas utiliser un éventuel fichier partiel. Conserver l'erreur pour diagnostic, ne pas tenter une restauration « au mieux ». L'outil de volumes refuse un morceau absent/corrompu, un ordre incohérent, des chemins de pièces suspects et l'écrasement de la sortie. Il lit en flux des blocs de 1 MiB.

## 4. Restaurer sans écraser

Lister les membres du tar avant extraction. Refuser chemins absolus, `..`, liens ou fichiers spéciaux inattendus. Extraire dans un répertoire neuf, jamais par-dessus PARISFIT. Contrôler **le manifeste interne déchiffré** et les SHA256 des fichiers restaurés.

Pour le bundle, répéter la méthode Phase26 : vérification bundle/pack, objets Git et références dans un magasin isolé sans alternance vers les objets originaux, puis reconstruction de HEAD et application du snapshot de travail. Une réinstallation complète du dépôt local peut être faite ensuite par le propriétaire sur sa machine ; aucun dépôt distant supplémentaire n'est nécessaire.

Ne pas confondre la restauration des fichiers ignorés (C3D, sources locales) avec celle du seul historique Git. Tester le modèle statique et les contrôles publics sans exécuter d'anciens workflows de capture. Les vidéos/captures restent des preuves internes non validées biomécaniquement.

## 5. Vérification de rétention

Après tout futur transfert autorisé, retélécharger les volumes depuis GitHub et restaurer sur la machine propriétaire. Garder les reçus et la clé hors du compte GitHub. Répéter périodiquement un test de récupération ; un premier upload réussi ne prouve pas une disponibilité future.

Conserver une copie personnelle des volumes si possible. Un compte GitHub unique est un domaine de panne unique ; la clé sur papier protège contre sa perte numérique mais **ne recrée pas** des volumes disparus. Tant qu'aucune copie des volumes hors GitHub n'est conservée, cette dépendance reste acceptée explicitement, pas résolue.
