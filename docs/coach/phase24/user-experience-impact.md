# Impact utilisateur — Phase24

Les huit exercices, titres, descriptions, indications musculaires et consignes restent présents. La bibliothèque ouvre désormais les instructions plutôt qu'une promesse de démonstration. Rocketbox reste le modèle humain ; son apparence, géométrie et textures ne sont pas remplacées. Le modèle est affiché au repos : **ce n'est pas la posture validée d'un exercice**.

Message permanent dans le Coach, également exposé par le statut accessible lors de la sélection :

> La démonstration animée de cet exercice est temporairement indisponible dans l’attente d’une validation biomécanique professionnelle.

Les contrôles temporels restent dans l'interface mais sont désactivés par défaut dès le HTML. Aucun autoplay. Précédent/suivant, bibliothèque, consignes, lancement du parcours de séance, trois vues, rotation et zoom restent disponibles. Les repères textuels existants ne sont pas une nouvelle certification scientifique. Aucune saisie ni mesure utilisateur n'est remplacée par une démo.

Accueil, Nutrition, Mental, habitudes et navigation : pas de refonte. `styles.css`, données démo et contenu Coach inchangés ; seules trois modifications dans `app.js` (libellé bibliothèque, sous-titre, version worker). Smoke vérifie les parcours de base ; texte des sections hors Coach conservé. Les captures et limites ergonomiques historiques ne sont pas réécrites ni déclarées résolues.

La mise à jour recharge les fenêtres de l'application lorsqu'un ancien cache est trouvé. Le localStorage est conservé ; un état de formulaire non enregistré peut être perdu lors de cette navigation. Le modèle statique est maintenant précaché : téléchargement initial un peu plus lourd, mais disponibilité hors ligne après installation réussie. Voir taille réelle du dérivé dans `public-build.json`.

Hors ligne avant réception de la correction : l'ancienne version ne peut pas être neutralisée à distance. Vérifications mobiles physiques et audit d'accessibilité complet restent à faire. Les contrôles de largeur automatiques ne remplacent pas ces validations.
