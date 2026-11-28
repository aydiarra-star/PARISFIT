# Première capture : prête à organiser, pas encore réalisée

Utiliser la [fiche pratique phase9](../phase9/CAPTURE-QUICKSTART.md) et le [modèle d'accords phase8](../phase8/CONSENT.md), toujours non signé. Aucun ancien CMU/film public ne devient une capture PARISFIT.

## Checklist de séance

- Un adulte volontaire, opérateur identifié, variante choisie avec un professionnel si disponible ; arrêt immédiat à la demande, douleur ou gêne. Aucun avis médical déduit du protocole.
- Deux caméras fixes simultanées : face et profil. Corps entier, tête, pieds et mains dans l'image avec marge au sol ; fond dégagé, lumière uniforme, tenue permettant de distinguer les articulations.
- 1080p,60Hz si possible ; paramètres identiques, pas de filtre/recadrage automatique. Mesurer hauteur/distance des objectifs et repère métrique ; enregistrer la mire couvrant le volume. La taille du participant ne remplace pas une calibration.
- Clap visuel au début et à la fin visible des deux caméras. Comparer offsets et dérive avec les timestamps ; si fréquence variable, ne pas utiliser seulement numéro de frame/FPS nominal. Deux prises successives ne sont pas deux vues synchronisées.
- Une prise = debout3s → squat confortable complet → retour naturel debout3s. Deux ou trois prises séparées si souhaitées, repos indicatif30–60s ou plus selon besoin. Ne pas assembler des phases de prises différentes.
- Avant départ : relire les deux vidéos entières, vérifier cadrage pieds/mains, synchro, absence d'occultation et retour enregistré. Conserver les originaux natifs, calibration, notes et hashes en privé.

Alternative monoculaire : une prise fixe profil/trois-quarts peut permettre une estimation locale autorisée, avec ambiguïtés de profondeur/échelle/rotation et occultations. Une prise frontale distincte sert de contexte mais pas de triangulation. Aucune promesse de contact ou reconstruction métrique fiable ; pas d'achat automatique d'une caméra.

## Matrice des autorisations (aucune obtenue)

| Opération | Accord requis | Par défaut |
|---|---|---|
| Filmer | participant adulte, séance/périmètre déterminés | Non autorisé |
| Traiter localement | film + analyse de pose/reconstruction + droits de l'opérateur | Non autorisé |
| Avatar commercial | traitement + exploitation commerciale explicite, supports/durée/territoire | Non autorisé |
| Publier la vidéo | publication des images source, distincte de l'avatar | Non autorisé |
| Redistribuer poses/GLB | licence publique et réutilisations comprises explicitement | Non autorisé |
| Partager au professionnel | destinataire nommé, finalité et confidentialité | Non autorisé |
| Service externe/Arena/CI | service nommé, finalité, hébergement/transferts, accord adapté | Non autorisé |

`tools/capture-pipeline/intake.py` et `permissions.py` restent en place. Les attestations logicielles ne vérifient pas juridiquement une signature. Ne jamais publier signature, pièce d'identité, coordonnées ou film privé dans la PR. La CI publique est verrouillée sur les hashes du CMU/Rocketbox autorisés, sans entrée de vidéo personnelle. Aucune capture privée traitée/transmise, aucun professionnel inventé.
