> Phase23 — audit de consolidation, date de session2026-11-27. État audité : `5379624ffab37417a43546d6cdb6e454956c530d`. Aucun merge, déploiement, contact, devis, dépense ou changement d’animation.

# Cache hors ligne et mises à jour

## Fonctionnement observé

Source : service-worker.js, `CACHE=parisfit-shell-v10`, installation addAll puis skipWaiting ; activation supprime les caches parisfit-shell-* anciens et revendique les clients. Navigation network-first, fallback index.html ; ressources same-origin cache-first. Requêtes Range non mises en cache par ce worker. Le modèle GLB est mis en cache **à la demande**, pas dans FILES.

Tests réels Chromium, [preuve](browser-audit.json) :
- shell chargé puis rechargé hors ligne : accueil/image disponibles ; navigation et saisies énergie/eau/journal fonctionnent, données locales conservées après reload ; aucune pageerror inattendue dans ce parcours ;
- premier accès Coach hors ligne sans téléchargement préalable du GLB : message/retry, **pas de Coach3D disponible** ; retour réseau puis retry réussi ;
- après chargement du GLB et des modules : rechargement hors ligne et huit clips accessibles (coach-browser.log) ;
- une première visite entièrement hors ligne sans installation antérieure n'est pas promise ni qualifiée par ces tests.

## Cycle de mise à jour isolé, pas déploiement

`tools/consolidation/cache-server.cjs` sert des octets en mémoire sur3011. Version de test sans écriture application ; cache HTTP no-store contrôlé. Après installation10, ajout d'un cache ancien témoin et d'un cache sans préfixe Parisfit. Mise à jour intentionnellement cassée (ressource404) : nouveau worker redundant, ancien shell toujours utilisable hors ligne. Un cache vide/incomplet audit-broken peut subsister jusqu'à la prochaine activation réussie.

Mise à jour correcte v11 : attendre **state=activated**, vérifier suppression de tous les anciens caches Parisfit, conservation du cache tiers et de localStorage, puis reload hors ligne réussi. Aucune hypothèse sur un futur hébergeur/CDN n'en découle.

Deux premiers essais du harnais, utilisant update() puis une attente de prédicat, ont échoué sur la suppression du cache témoin. La synchronisation de l'observation avec l'activation est suspectée ; la cause fine du décalage n'a pas été isolée. Le succès suivant ne permet pas d'effacer ces échecs ni d'affirmer un diagnostic certain. [Erreur1](initial-browser-failure.log), [erreur2](second-browser-failure.log), [résultat initial partiel](initial-browser-audit.json) conservés. Test corrigé pour attendre explicitement l'événement d'activation ; **mêmes assertions de suppression**, aucun changement du service worker produit. Résultat final PASS ; pas de masquage d'un ancien échec.

## Risques non fermés

- app.js absorbe l'échec de register via catch vide : pas de signal utilisateur dédié en cas d'impossibilité de préparer le hors-ligne.
- cache-first exige une discipline de versionnement ; changer une ressource à URL identique sans nouvelle version peut laisser du contenu ancien. L'upgrade contrôlé ne certifie pas les en-têtes HTTP réels de production.
- éviction stockage, quota, changement simultané entre plusieurs onglets, modes privés et Safari/iOS physiques non testés ; pas de garantie universelle.
- la mise à jour écrit index.html en cache sans event.waitUntil sur cette écriture particulière : à examiner pour robustesse en arrêt abrupt du worker, non reproduit comme panne ici.

Aucune modification du cache produit, aucun déploiement. Il faut distinguer succès du parcours chaud et absence de modèle à froid.
