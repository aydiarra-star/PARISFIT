# Sources vérifiées — Phase27

Date de session : 2026-11-27. L'horloge observée du sandbox indique 2026-11-28 ; les horodatages de test sont conservés tels quels. Les limites de service peuvent changer : les revérifier avant un transfert autorisé.

- S1 : https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github — avertissement au-delà de 50 MiB, blocage au-delà de 100 MiB, ajout navigateur limité à 25 MiB, dépôt idéalement <1 Go et fortement recommandé <5 Go ; Git n'est pas conçu comme outil de sauvegarde.
- S2 : https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits — push limité à 2 Go, recommandation de taille sur disque 10 Go ; ce n'est pas une garantie d'espace de sauvegarde réservé. Les recommandations de cette page ne remplacent pas les conseils plus conservateurs de S1.
- S3 : https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases — jusqu'à 1 000 pièces par release, chaque pièce sous 2 GiB, pas de limite de taille totale/bande passante annoncée sur cette page. Conditions d'usage et disponibilité restent applicables. S1 renvoie aussi au plafond par fichier du plan LFS ; choix de petits volumes très en dessous des deux indications.
- S4 : https://docs.github.com/en/billing/concepts/product-billing/git-lfs — quotas inclus, stockage/téléchargement comptabilisés, blocage possible avec budget zéro et facturation possible au-delà selon configuration. Ne pas activer LFS sans vérification de budget/usage ; le plan actuel du compte n'est pas établi.
- S5 : https://github.com/FiloSottile/age (README, Usage) — clés age, identité privée séparée, chiffrement/déchiffrement local, mode phrase secrète, binaires multiplateformes et vérification Sigsum. Release consultée v1.3.2 : `age-release.json`.
- S6 : https://github.com/woodruffw/pyrage — bindings Python de rage (implémentation Rust du format age). Version de test PyPI **1.4.0**, roue Linux épinglée et SHA256 comparé aux métadonnées PyPI : `pyrage-provenance.json`.
- S7 : https://www.gnupg.org/documentation/manuals/gnupg/GPG-Examples.html — chiffrement/signatures OpenPGP, protection des clés et précautions d'interopérabilité. GPG non exécuté ici.

Les appels aux sources et téléchargements d'outillage sont entrants ; aucun contenu PARISFIT, archive ou clé n'a été envoyé à un service externe. Aucun compte ni service créé.
