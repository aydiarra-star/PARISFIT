# Premier lot après fusion PR11 : ressentis datés

Base effective : `644508d1568bccfb737e1fd0ccd0a821b2caf1c9`, fusion PR11 vérifiée. Travail sur la branche de session existante, avancée en fast-forward sur ce main avant développement. Aucune modification directe/push vers main.

- Les nouveaux ressentis d'énergie enregistrent `energyRecordedAt` à l'instant de saisie.
- Un ancien ressenti sans date garde ses octets/données : affichage « date inconnue », aucune date historique inventée.
- Le jour local est pris en compte : ressenti du jour explicite, ancien jour à actualiser, horodatage futur incohérent signalé.
- Aucune réinitialisation automatique de l'eau, des habitudes ou du journal ; aucun score de santé déduit de cette autoévaluation.
- Cache v30 et URL app-state versionnée pour éviter l'utilisation de l'ancien module après mise à jour.

Tests unitaires : date inconnue, jour courant, jour passé, horloge future, persistance et absence de mutation de l'ancien état. Tests navigateur : horodatage réellement enregistré/rechargé, libellé du jour et données historiques sans date non réécrites ; suite fonctionnelle/Coach/hors ligne complète repassée. Résultats locaux conservés dans ce dossier.

Ce lot est distinct du contenu fusionné dans PR11. Il doit être revu dans une nouvelle PR et ne bénéficie d'aucune autorisation de fusion/déploiement implicite. Prochaine étape : définir le suivi journalier eau/habitudes avec conservation de l'historique et consentement utilisateur, avant personnalisation de programmes.
