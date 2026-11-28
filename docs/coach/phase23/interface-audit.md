> Phase23 — audit de consolidation, date de session2026-11-27. État audité : `5379624ffab37417a43546d6cdb6e454956c530d`. Aucun merge, déploiement, contact, devis, dépense ou changement d’animation.

# Interface d’accueil et données

## Observation réelle

[Capture390px](home-390.png), [capture1440px](home-1440.png), [résultats navigateur](browser-audit.json). Tests à320/375/390/430/720/768/1024/1440px : navigation Aujourd'hui/Switch/Nutrition/Mental, cartes dans la largeur et absence de débordement horizontal. Navigation Coach via séance recommandée vérifiée par smoke et coach-browser. Les captures contiennent uniquement des données témoins synthétiques « Audit », pas des données utilisateur.

- Palette calculée : vertforêt `--g:#07573e`, émeraude `--g2:#07875d`, fond `#edf3ee`. CTA de séance corail `#f56b53` dans styles.css ; jeton orange `#f1a05b` distinct, pas assimilé au corail.
- Cartes arrondies, hero, actions, séance recommandée,4essentiels, accès Coach et SOS présents. Citation exacte : « La discipline est la clé d’une liberté durable. » ; texte éditorial, aucune attribution d'auteur inventée.
- Vitalité affichée92/100, +12%,3jours : `PARISFIT_DEMO.dashboard`, **pas des mesures**. Mention visible « Démonstration · score non mesuré ». L'énergie initiale « Pleine » affiche « Exemple · évalue ton énergie ».
- Énergie déclarée low→Douce puis medium→Modérée ; hydratation3verres→38%,4→50%,5→63% ; nom, journal et habitude réels témoins restent présents après reload et hors ligne.
- Render seul n'écrit aucun exemple dans localStorage : stockage initial null ; objet réel et champ sentinelle conservés exactement avant interaction. Les actions enregistrent uniquement les choix. Aucun score réel mesuré n'existe dans le schéma actuel : on ne peut pas garantir la prise en charge d'une future donnée de score.

## Réserves d’interface constatées

1. Les +12% et3jours n'ont pas chacun un badge « exemple » ; ils dépendent de la petite mention du bloc. Le delta/streak ne reflète pas les habitudes réelles. Lisibilité et compréhension à renforcer avant acceptation générale ; ne pas les présenter comme progrès utilisateur.
2. Barre flottante `.mobile-nav` visible **aussi sur desktop**, en plus de la sidebar (règle Shared frame). Sur les captures, elle recouvre temporairement une bande des actions. Le scroll et la marge basse permettent d'atteindre les contrôles testés, mais un test sans débordement ne prouve pas « aucun chevauchement ». Aucun succès global d'accessibilitéWCAG annoncé.
3. Certains glyphes emoji apparaissent en carré dans ce Chromium Linux : le rendu de police de l'environnement doit être distingué d'un défaut confirmé sur téléphone physique.
4. L'hydratation est un compteur local plafonné à8, repère indicatif250ml/verre. Pas de date dans le modèle ni remise à zéro quotidienne automatique. Ce n'est pas une prescription ni une mesure captée.
5. La citation ne change pas au rechargement, comportement éditorial statique normal. Les données illustratives restent affichées si aucune mesure correspondante n'existe ; jamais certifiées réelles.

Pas de modification de l'accueil dans cette phase. Réserves recommandées : badges explicites sur tous les chiffres fictifs, contrôle du recouvrement desktop, tests physiques iOS/Android et revue accessibilité. Les tests effectués ne couvrent ni tous les contenus possibles ni toutes les tailles de texte système.
