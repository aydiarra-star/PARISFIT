# PR11 — audit actuel et corrections avant fusion

## Périmètre

Audit du travail réel sur `arena/a03f64da-parisfit`, pas validation par reprise des anciens PASS. Base distante main : `83f89f8727c1de1c65dbe1278676f1daafd173fc`, HEAD initial : `fc51383e1a28f649a700057bb4d19bcb420c8eaf`, 0 commit de main manquant et 59 commits de branche. PR11 initialement OPEN/DRAFT, mergeable, ses anciens checks concernaient fc51383 **sans** les changements locaux Phase24–28.

`start-baseline.json` capture aussi le travail non committé. Les sources et rapports de ces phases sont conservés et doivent être inclus au commit candidat ; les archives `.cache` ne doivent jamais être ajoutées. GitHub refuse le diff rendu dépassant 300 fichiers (406) : audit par Git local et API fichiers paginée, pas par une vue tronquée.

## Défauts constatés et corrections

1. **Déploiement automatique lors d'une fusion** : workflow Pages désormais manuel uniquement, avec `confirm_deployment=true` et ref main requises. Aucun déploiement demandé/exécuté.
2. **Habitudes réapparaissant après effacement** : defaults ne partageant plus un tableau mutable, effacement explicite testé après rechargement.
3. **Données locales malformées et stockage indisponible** : module `app-state.js` testé ; données invalides conservées brutes, écritures bloquées jusqu'à réinitialisation explicite ; export utilisateur disponible. Erreur/quota local signalé, aucun faux succès d'enregistrement.
4. **Injection HTML par champs de données locales** : identifiant/fréquence/titre d'habitude et initiale échappés ; scénarios hostiles inertés dans le navigateur.
5. **Métriques illustratives en premier plan** : retrait de l'affichage 92/+12%/série fictive ; indicateur neutre « non calculé », énergie issue uniquement d'un ressenti enregistré. Exemples d'exercices conservés et distingués d'une personnalisation.
6. **Promesses Coach incohérentes** : aucune « démonstration lancée » quand verrouillée ; assistant local à réponses prédéfinies identifié comme tel, pas une IA connectée/diagnostique ; précaution pour douleur ; cartes utilisables au clavier.
7. **Synchronisation d'interface et confidentialité** : profil et ressenti répercutés dans Coach, journal annoncé local sans chiffrement/synchronisation ; aucun réseau tiers observé dans les scénarios fonctionnels.
8. **Débordement mobile détecté à 320 px** : neutral labels autorisés à se replier ; échec initial et capture conservés, suite relancée avec succès.
9. **Publication** : app-state et licence MIT Three.js inclus dans les 30 fichiers autorisés ; pas d'archive, données de capture, vidéos scientifiques ou diagnostic dans le paquet. Upload de validation CI limité aux résultats/screenshots publics synthétiques, plus aux rapports scientifiques Phase3–7.
10. **Préservation** : bytecode Python régénérable ignoré, pas supprimé. Les anciennes preuves restent intactes. L'exception `styles.css`/`.gitignore` des tests de préservation historique est explicite pour les corrections autorisées ; les anciens manifestes ne sont pas réécrits.

## Contrôles réellement exécutés localement

- `npm ci` : PASS ; `npm audit --json` : zéro vulnérabilité rapportée (pas une preuve universelle de sécurité).
- `npm test` : PASS, syntaxe, evidence contracts, huit clips/hash d'origine, verrouillage, état utilisateur et préservation.
- Build statique de production `python tools/animation-lock/build_public.py` : PASS, 30 fichiers ; aucune compilation serveur requise pour cette application statique. `test_static.py` : PASS, dérivé sans animation et modèle/textures préservés.
- `npm run test:browser` : PASS — smoke, huit exercices verrouillés, événements forcés/clavier/URL/historique/hors ligne, vrai ancien worker migré, module de données, journal/profil/habitudes, export/effacement, données hostiles, stockage refusé, cinq vues et huit largeurs (320–1440).
- 8 suites Python via l'environnement `.venv` avec numpy : PASS, contrats modèles/métadonnées/passif/review/dossier/gate/intake/permissions. Premier essai avec Python système a échoué faute de numpy ; sortie conservée, pas masquée comme PASS.
- Audit de release : aucun fichier préexistant perdu, rapports historiques inchangés, GLB et quatre archives Phase26 inchangés, aucun nouveau conteneur d'archive/clé proposé au Git, aucun motif de secret recherché détecté ; vérification de la liste publique et de l'absence de déclenchement de déploiement sur merge.

Commandes de reproduction : serveur local `python3 -m http.server 3000 --bind 0.0.0.0 --directory .cache/public`, puis `npm run test:browser`. Dans le sandbox : `LD_LIBRARY_PATH=/tmp/al2023/lib CHROMIUM_PATH=/tmp/chromium`. Ne pas exécuter les suites de vidéos historiques qui régénèrent des preuves.

## Limites non assimilées à des validations

- Pas de test sur téléphones physiques iPhone/Android ; tests Chromium et largeurs émulées seulement. Petits glyphes emoji manquants dans le rendu Linux possibles ; pas de certification WCAG.
- Application locale sans compte, backend ni synchronisation ; données non chiffrées sur l'appareil. Réponses Coach prédéfinies, programmes personnalisés complets, suivi longitudinal et transitions biomécaniques validées non réalisés.
- Aucune animation validée professionnellement. Toutes les démonstrations restent verrouillées ; la présence d'un modèle statique n'est pas une référence posturale validée.
- Dépôt historique public : les originaux restent accessibles par Git/PR. La sauvegarde chiffrée est toujours bloquée faute de clé propriétaire ; 216 artefacts Actions restent métadonnées seulement. Aucune archive non chiffrée ni clé ajoutée/poussée.
- L'API des protections de main renvoie 403 à l'intégration. Collaborateurs et permissions visibles consignés ; aucun changement de permissions. Une éventuelle fusion utilisera l'opération normale, sans `--admin`, force push, bypass ou suppression de branche.

## Fusion conditionnelle

Les résultats locaux ne remplacent pas les checks GitHub du **commit candidat exact**. Garder PR11 en brouillon tant que ces checks ne sont pas satisfaisants. Puis revoir la base/main, retirer le brouillon, revérifier les checks et effectuer uniquement `gh pr merge 11 --merge`, sans déploiement ni suppression de branche.

Le résultat effectif, SHA exact et vérification du tree de main seront consignés dans `decision-report.md` après l'opération. Ce document ne prétend pas que la fusion a déjà eu lieu.
