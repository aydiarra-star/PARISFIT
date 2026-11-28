# Comparaison des solutions — Phase25

**Recommandation : B, sous la forme « dépôt actuel rendu privé pour conserver l'histoire + nouveau dépôt public propre de l'application »**, avec A comme mesure de confinement préalable, **uniquement après votre autorisation**. Ne pas copier l'historique actuel dans le nouveau public. C n'est pas recommandé en première intention.

Les conditions GitHub sont documentées dans [sources.md](sources.md), S1–S5. Le plan actuel du compte n'est pas connu ; aucune disponibilité gratuite de Pages depuis un dépôt privé n'est supposée.

| Critère | A — Dépôt actuel privé | B — Application publique / archives privées | C — Purge de l'histoire publique + originaux privés |
|---|---|---|---|
| Action structurante | Changer la visibilité après contrôles | Séparer code public et preuve scientifique ; traiter aussi l'ancien dépôt | Réécrire tous les historiques/ref pertinents puis remplacer les refs distantes |
| Coût réalisable | Dépôt privé GitHub Free possible ; aucun nouveau service requis | Dépôt public et privé gratuits possibles ; analyses privées localement, Actions privées désactivées | Outils Git gratuits, mais travail et coordination élevés ; pas de garantie de service support |
| Pages | Sur Free, un Pages publié depuis ce dépôt serait dépublié ; Pages privé-source requiert un plan compatible | Pages possible gratuitement depuis le nouveau dépôt **public** ; nouvelle URL/migration séparée, pas de déploiement ici | Pages public potentiellement conservé, mais réglages/workflows/hashes à réauditer |
| Accès aux originaux | Limité aux accès autorisés du dépôt, pas aux clones déjà partis | Séparation lisible et contrôle d'accès distinct, si l'ancien historique n'est plus public | Réduction dans les refs traitées ; caches/PR/forks/clones peuvent rester |
| Collaborateurs | Vérifier propriétaire, collaborateurs, invitations, deploy keys, Apps et tokens avant bascule | Deux ensembles d'accès ; ne pas donner l'accès archive à tous les développeurs publics | Coordination indispensable avec tous les détenteurs de clones pour éviter réintroduction |
| Preuves | Histoire et SHA conservés | Histoire complète conservée privée + manifeste de correspondance public/interne | SHA de commits modifiés, liens de preuves/PR cassés ; conserver un miroir immuable privé et correspondances |
| Risque de perte | Faible pour les fichiers, conséquences sur métriques/forks/fonctionnalités | Omission lors du tri/export ou oubli des fichiers ignorés ; contrôles SHA nécessaires | Élevé : filtre trop large, branche oubliée, travail divergent, perte de signatures et commentaires |
| Réversibilité | Repasser public republierait tout ; stars/watchers et réseau de forks pas nécessairement restaurés | Conserver les deux dépôts rend le rollback technique possible ; toute publication nouvelle reste copiable | Rollback possible depuis sauvegarde mais republierait aussi les données retirées ; effets PR/signatures non intégralement réversibles |
| Limite fondamentale | Pas de confidentialité rétroactive | Déplacer les fichiers sans traiter l'ancien dépôt **ne résout pas** le risque | Force-push ≠ révocation des anciens objets/copies |

## A — Conditions avant décision

L'API déclare actuellement `has_pages: false` et les huit déploiements listés ont échoué. Cela rend A a priori moins perturbant pour ce Pages, mais ne prouve pas l'absence d'un hébergeur externe. Le propriétaire doit confirmer plan, éventuel domaine personnalisé et DNS, Apps, deploy keys et invitations (ces deux derniers endpoints étaient interdits à l'intégration d'audit). Le seul collaborateur listé est le propriétaire ; ce n'est pas une certification de tous les accès.

Si un domaine personnalisé existe, retirer ou adapter correctement les DNS avant dépublication pour éviter un domaine abandonné. Conserver le compte et les droits nécessaires aux audits. Ne pas acheter Pro pour garder Pages sur la source privée : la solution B évite cette dépense. Dépôt privé ne signifie pas site Pages privé.

## B — Variante retenue

1. **Garder le dépôt historique entier comme archive privée** (bascule A autorisée séparément). Pas de suppression, pas de force-push, conservation de tous les SHA scientifiques et des originaux.
2. Créer ultérieurement, après accord sur nom/propriétaire, un **nouveau dépôt public sans lien d'historique ni fork** du dépôt d'archives. Y exporter seulement la version autorisée de l'application et ses licences ; tests publics adaptés sans fixtures biomécaniques. Un simple clone suivi de suppressions serait incorrect.
3. Utiliser les 28 fichiers du paquet contrôlé comme frontière de distribution, pas forcément comme liste exhaustive du dépôt de développement futur. Tout code de build/test supplémentaire doit être revu ; il ne doit pas nécessiter le téléchargement public du GLB animé.
4. Produire le modèle statique dans l'environnement privé/local, comparer ses SHA et publier seulement ce dérivé avec licence/attribution. Ne pas donner à une CI publique un token de lecture du dépôt privé ni y imprimer des trajectoires.
5. Conserver les preuves et données de capture dans un espace privé autorisé, avec index SHA. Ne pas commiter les archives monolithiques de sauvegarde dans Git ; gérer les tailles/quotas et conserver une copie sur stockage déjà possédé. Aucun Git LFS payant ou stockage supplémentaire ne doit être activé sans accord.

**B sans A (ou sans C) laisse l'histoire actuelle publique et est insuffisant.** Si le propriétaire veut absolument garder ce dépôt et son URL publics, B doit être combiné avec une purge C autorisée séparément ; ce n'est plus l'option à faible risque recommandée.

## C — Pourquoi reporter

La suppression de clips non validés n'est pas la même chose qu'une fuite de credentials. Le scan n'a pas établi un secret à révoquer. Si un secret réel est découvert ensuite, sa révocation/rotation est prioritaire, pas seulement l'effacement Git.

Une purge doit couvrir branches, tags, variantes de chemins, refs PR, logs, artefacts, éventuelles releases et forks. GitHub précise que les clones, caches SHA et références PR peuvent survivre ; le support n'efface pas les données non sensibles sur simple demande et son aide n'est pas garantie. Aucun contact support ni tiers n'a été initié.

Ne pas lancer `git filter-repo`, force-push ou suppression de branches dans cette session. Préparer d'abord un plan de filtrage approuvé, une sauvegarde privée durable **restaurée et vérifiée**, un inventaire frais, une correspondance des anciens/nouveaux SHA et un protocole de re-clonage. Les PR existantes nécessiteraient une décision dédiée ; aucune fusion/fermeture n'est implicitement autorisée.

## Critère de décision

Si la priorité est de conserver les preuves sans dépense et de réduire l'accès public futur, choisir **A puis B**. Si la priorité absolue est de préserver le nom/URL du dépôt public actuel, accepter les coûts opérationnels et limites de **B+C**, après un second accord explicite. Aucune solution ne peut promettre d'effacer les téléchargements déjà effectués.
