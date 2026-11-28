# Reprise et récupération — Phase28 bloquée

## Ne pas chercher une archive qui n'existe pas

Aucun volume Phase28 n'a été créé. `volume-checksums.txt` ne contient aucune empreinte de volume et ne doit pas être utilisé comme certificat. Les archives Phase26 en clair restent temporaires ; ne pas les supprimer et ne pas les considérer publiées/durables.

## Action attendue du propriétaire

Sur votre ordinateur sûr, installer un outil age de provenance vérifiée et suivre la création locale décrite en Phase27 `recovery-procedure.md`. Conserver l'identité privée **hors de tous les dépôts Git**, ainsi qu'une copie indépendante. Tester sa récupération sur un fichier fictif chez vous. Aucune clé privée ni phrase secrète ne doit être transmise au chat, à un rapport, à GitHub ou à Actions.

Pour permettre un futur chiffrement ici, communiquer uniquement le **destinataire public age** et confirmer que vous détenez l'identité privée correspondante et sa sauvegarde. Ne pas utiliser le destinataire d'un exemple ou de la démonstration Phase27.

Pour la restauration réelle, privilégier votre appareil : recevoir les volumes par une méthode explicitement autorisée, les réassembler, puis utiliser localement votre identité privée. Sans accès sûr à la clé privée, l'agent ne peut pas effectuer le déchiffrement dans le sandbox ; il ne vous demandera pas d'y publier votre clé pour contourner cette limite.

## Séquence technique prévue, non exécutée

1. Recontrôler les quatre SHA256 de `archive-manifest.md` ; arrêt sur absence/différence. Relire `input-files.csv` et `input-git-objects.csv` pour connaître précisément le périmètre.
2. Chiffrer exclusivement les entrées vérifiées vers le destinataire confirmé. Aucun ajout de documents Phase27/28 aux sources sans annoncer ce changement de périmètre. Manifeste technique extérieur ne contenant que des métadonnées/chiffres publics ; manifestes internes détaillés à conserver avec les sources chiffrées.
3. Découper chaque ciphertext en volumes **≤ 20 971 520 octets**, numéros zéro-remplis, taille et SHA256 mesurés. Produire un manifeste ordonné et le SHA256 global. Ne pas reprendre les estimations Phase27 comme résultats.
4. `tools/encrypted-backup/volumes.py join` vérifie ordre, taille et hash des parties puis réassemble dans une sortie neuve. Pour le déchiffrement, `age -d -i <chemin-local-identité> -o <sortie-neuve> <ciphertext>` s'exécute **chez le propriétaire**, clé hors Git. Aucun secret comme argument de valeur ou variable d'environnement : seul le chemin local de l'identité.
5. Vérifier le code retour et les hashes internes avant extraction. Refuser les tar contenant chemins absolus, traversées, liens ou fichiers spéciaux inattendus. Ne jamais extraire directement un flux de déchiffrement incomplet sur les originaux.
6. Répéter toute la séquence de `restore-verification.md`. Publier uniquement des résultats/hashes non secrets. Statut « prêt » uniquement après ce test réel réussi et contrôle des exclusions de publication.
7. Demander une autorisation explicite supplémentaire avant tout push/upload des volumes. Aucun accord de publication ne découle automatiquement de la fourniture du destinataire public.

Cette reprise n'efface pas l'exposition historique publique et n'ajoute pas les 216 artefacts Actions absents. La dépendance à GitHub et la conservation de la clé restent des décisions distinctes.
