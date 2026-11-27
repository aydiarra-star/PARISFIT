# Fiche de tournage PARISFIT — un squat, une personne

**État : prêt à organiser, aucune séance réalisée.** Ne pas filmer avant autorisations. Cette fiche n'est pas une prescription sportive ; la personne doit pouvoir effectuer le mouvement confortablement. Un professionnel qualifié doit définir la variante et l'amplitude adaptées. Arrêter à la demande, en cas de douleur, malaise ou perte d'équilibre ; ne pas recommencer pour sauver une prise.

## 1. Avant le rendez-vous

- Une personne adulte volontaire ; opérateur identifié ; professionnel désigné si disponible. Pas de mineur ni de personne dans l'arrière-plan.
- Compléter `CONSENT.md` en privé : captation, traitement local, avatar commercial, droits de l'opérateur, revue ; choisir séparément publication du film et des coordonnées de mouvement. Pas d'autorisation cloud implicite.
- Réserver un espace dégagé et un sol plat non glissant ; pas d'haltère/barre. Tenue confortable contrastant avec le fond, articulations distinguables, chaussures visibles. Ne pas imposer une tenue révélatrice.
- Vérifier deux caméras pouvant filmer **simultanément**. Trois caméras sont préférables pour réduire les occultations ; la troisième est facultative, pas un prérequis à acheter.

## 2. Installation concrète

- Caméra A face au sujet ; B à environ 90° pour le profil. Téléphones sur supports fixes, même hauteur approximative de bassin, axes proches de l'horizontale. Distance initiale indicative 3–4 m, ajustée au cadrage et à l'optique, pas une calibration.
- Mode paysage, 1080p minimum, 60 images/s si les deux appareils le permettent ; 30 images/s acceptable pour une première qualification lente mais à documenter. Objectif principal, pas ultra-grand-angle, pas zoom numérique ni mode portrait/cinématique. Désactiver filtres/retouches ; verrouiller exposition et mise au point si possible.
- Laisser une marge visible au-dessus de la tête et sous les chaussures, avec sol autour de chaque pied pendant **toute** la descente et la remontée. Ne pas déplacer les appareils entre calibration et prise.
- Éclairage diffus et constant sans contre-jour ni scintillement ; faire une courte prise d'essai et vérifier le flou des pieds/mains. Retirer adresses, miroirs montrant d'autres personnes, documents et voix inutiles.
- Garder un repère de longueur mesurée dans le volume. Relever dimensions réelles, orientation du sol, disposition et paramètres des caméras. La taille déclarée d'une personne ne suffit pas à calibrer un volume.

## 3. Calibration et synchronisation

- Filmer une mire ChArUco rigide dont les dimensions imprimées sont **mesurées**, visible simultanément par les deux caméras, dans plusieurs positions et orientations couvrant le volume utilisé, sans déplacer les appareils. Archiver le dictionnaire, nombre de cases et dimensions. Utiliser la procédure de la version FreeMoCap choisie ; ne pas inventer des paramètres intrinsèques.
- Filmer un événement visuel net visible des deux caméras avant la prise, puis un second après (par exemple clap visuel de l'opérateur hors du mouvement). La première synchronisation seule ne détecte pas la dérive des horloges.
- Les deux vues doivent représenter **le même squat** ; deux répétitions successives face/profil ne constituent pas une capture stéréo.
- Conserver les fichiers originaux avec leurs horodatages. Vérifier les PTS et la fréquence variable avant reconstruction ; ne pas interpoler silencieusement pour obtenir 60 Hz. Tolérance de triage : dérive des repères ≤1 frame à 60 Hz ; ce seuil n'est pas une garantie d'erreur 3D acceptable.

## 4. Prise unique visée

Filmer sans coupe : environ 3 s debout immobile → un squat à rythme confortable avec descente, passage bas et remontée → environ 3 s debout après retour naturel. Viser 10–15 s au total sans imposer de cadence artificielle ou de profondeur. Ne pas demander de pause basse si elle dénature la variante retenue par le professionnel. Capturer une pose neutre de calibration avant/après selon le solveur.

Revoir sur place **les deux vidéos complètes** : tête, mains, genoux, talons et avant-pieds toujours dans l'image ; pas d'occultation majeure ; pas de tremblement ni coupe ; retour réellement enregistré. Si reprise nécessaire, la nommer comme prise distincte. Ne pas assembler la descente d'une prise et la remontée d'une autre.

## 5. Dossier privé à remettre

```text
PF-SQUAT-001/
  front-original.mp4
  profile-original.mp4
  calibration-front-original.mp4
  calibration-profile-original.mp4
  calibration.json              # produit par calibration, pas fabriqué
  session.json                  # copie complétée du manifeste
  take-notes.txt                # matériel, FPS, dimensions, événements synchro
```

Les consentements signés et coordonnées restent dans un registre séparé, sécurisé, accessible seulement aux responsables. Référencer dans le manifeste une empreinte SHA256 du dossier d'autorisation, pas le nom/signature. Ne pas les placer dans Git, dans les rapports publics ou dans le chat.

Conservation : originaux en lecture seule, sauvegarde privée chiffrée, accès nominatifs ; durée et procédure d'effacement à fixer avant captation. Le cache Arena n'est **pas** un archivage durable ou une garantie de confidentialité.

## 6. Go / no-go avant extraction

- Droits incomplets → ne pas lire/analyser le film.
- Pied coupé, personnes additionnelles, vue différente dans le temps, calibration absente ou mauvaise → reconstruction bloquée ; ne pas remplacer les zones invisibles par un mouvement idéal.
- Autorisation de traitement local seule → aucune publication ou téléversement dans Arena/service externe sans autorisation distincte applicable.
- Capture techniquement exploitable → estimation autorisée, **pas** validation sportive.

Commande locale documentée dans `PIPELINE.md`. Aucun transfert automatique, achat ou service payant.
