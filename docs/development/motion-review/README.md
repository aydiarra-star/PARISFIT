# Revue du réalisme — premier lot, non terminé

## Portée et état d'accès
Huit animations auditées à 60 Hz sur le GLB réel (squelette et sommets de peau des mains/pieds), originaire du SHA256 1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb. Aucun original ni archive historique modifié. Les fichiers d'autorisation publics n'ont pas été changés.
Aucun lien Render déployé n'est connu/vérifié dans cette session. Aucun service Render modifié. Au push, deux commits distants concurrents ont été détectés : 0e3d682 (vitesses) et f225849 (accès direct PARISFIT_DEMO_OPEN=1). Ils sont intégrés sans écrasement ; l'ajout local des vitesses en double est retiré. Le mode direct côté serveur est conservé et testé isolément : il donne accès sans cookie à toute personne ayant l'URL, sans contrôle d'identité propriétaire. La protection reste le défaut lorsque la variable n'est pas activée. Ni mot de passe dans l'URL ni modification du paquet public. L'URL Render exacte reste nécessaire pour vérifier le déploiement existant.

## Constats par exercice et réserves
Les chiffres ci-dessous sont de nouvelles mesures techniques, pas une revue professionnelle. L'excursion d'un marqueur sur tout le cycle ne signifie pas glissement si le membre est en déplacement volontaire ou en vol. Les anciennes réserves anatomiques restent ouvertes ; elles ne sont pas présentées comme nouvellement mesurées.

| Exercice | Observation actuelle | Intervention de ce lot / restant |
|---|---|---|
| Squat | Excursion horizontale du sommet de pied suivi ≈ 0,022 mm ; accélération max d'articulation 2,00 m/s² | Pas de recalage arbitraire. Placement genoux/bassin et déformations du maillage à examiner visuellement sur cycle entier. |
| Pompes | Marqueur de main ≈ 0,016 mm ; accélération max 0,74 m/s² | Pas de modification ; forme des doigts, poignets et profondeur restent non approuvées. |
| Gainage | Pieds fixes ; marqueurs mains < 0,001 mm ; accélération max ≈ 0,00068 m/s² | Pas de modification ; exercice quasi statique, absence de dynamique de charge/respiration. |
| Fentes | Excursion de pied ≈ 0,59 m incluant les pas ; accélération max 8,65 m/s² | Ce déplacement ne prouve pas du glissement. Définir fenêtres de contact puis mesurer dérive ; transfert de poids à revoir. |
| Jumping jacks | Accélération max 90,85 m/s² à 60 Hz | Signal prioritaire à localiser par os/phase et vérifier à plusieurs fréquences, pas un diagnostic de danger. Aucun correctif appliqué ; réception/IK à examiner. |
| Mountain climbers | Accélération max 44,60 m/s² ; mains stables ; alternance des jambes | Candidat de redistribution temporelle comparé, voir ci-dessous. Anatomie, doigts, charge et contacts non corrigés. |
| Étirement du dos | Marqueurs pieds quasi fixes ; accélération max 2,64 m/s² | Variante debout conservée, pas de nouvelle animation au sol ni de correction anatomique. |
| Mobilité des épaules | Pieds fixes ; accélération max 0,61 m/s² | Petits cercles conservés. Amplitudes, scapulas et déformations des épaules à revoir. |

## Correction expérimentale réellement produite
Uniquement mountain climber : redistribution du temps à l'intérieur de chaque quart de cycle, avec une courbe quintique. Les poses sont interpolées depuis les pistes originales, pas réinventées ni issues de motion capture. Durée 4 s et amplitudes conservées ; aucune augmentation globale de vitesse pour cacher un défaut. Le candidat ne prétend pas résoudre un défaut anatomique par lissage.

| Mesure à 60 Hz | Original | Candidat |
|---|---:|---:|
| Pic vitesse articulaire | 0,9646 m/s | 1,0430 m/s |
| Pic accélération articulaire | 44,6017 m/s² | 32,4137 m/s² |
| Minimum surface de support | 0,0019995 m | 0,0019995 m |
| Écart de position boucle | 0 m | 0 m |

Réduction du pic d'accélération ≈ 27,3 %, augmentation du pic de vitesse ≈ 8,1 %. Compromis explicite, PAS validation. Le rééchantillonnage et la dérivation numérique influencent ces pics : confirmation à plusieurs fréquences requise. Les mesures des sept autres clips sont identiques dans les deux audits.
`comparison.html` : douze captures avant/candidat, six instants, trois vues ; aucune vidéo intégrale revendiquée. La capture candidat à 0,25 s a été examinée : personnage humain, appuis des mains visibles ; aucune conclusion globale sur absence de pénétration/déformation.
`comparison.json` conserve hashes et mesures. Le clip dérivé JSON est séparé dans tools/motion-review, chargé seulement par le paquet démo. Sélecteur facultatif dans Coach, effectif seulement pour mountain climber. Original par défaut. Les archives et le GLB source sont préservés.

## Transitions
Aucune transition nouvellement créée. Les transferts historiques debout/accroupi restent HOLD, faute de raccord approuvé aux exercices ; cinq autres transitions historiques sont absentes. Les noms de poses ne prouvent pas la compatibilité des articulations et contacts. Coupure explicite en pause conservée, plutôt qu'une interpolation qui traverse le sol. Ce point ne satisfait pas encore l'objectif de transitions naturelles.

## Reproductibilité
1. `LD_LIBRARY_PATH=/tmp/al2023/lib CHROMIUM_PATH=/tmp/chromium node tools/motion-review/candidate.cjs`
2. Même environnement, `node tools/motion-review/audit.cjs`, puis `MOTION_CANDIDATE=1 node tools/motion-review/audit.cjs`.
3. `node tools/motion-review/compare.cjs` pour les captures.
4. Le JSON généré dans .cache contient huit clips ; seul mountainclimber est copié dans tools/motion-review/mountainclimber-candidate.json pour le paquet démonstration.
Les scripts interceptent les requêtes dans le navigateur de test avec une liste limitée de fichiers ; aucun serveur du dépôt n'est exposé pour cette analyse.

Une première tentative utilisant l'ancien auteur sur le GLB exporté a échoué (racine non récupérée comme os). Elle n'a produit aucune correction ; logs d'échec conservés. Approche abandonnée : ne pas confondre le GLB exporté avec le squelette source d'authoring. L'essai réussi utilise uniquement les pistes originales et leur interpolation.

## Tests réellement exécutés
- Deux audits 60 Hz des huit cycles, mesures squelette et surfaces : terminés, JSON conservés (pas de seuil médical PASS).
- Capture comparative : terminée. Vitesses .5/1/1.5/1.75/2 : vitesses/accélérations analytiquement mises à l'échelle dans les rapports, PAS cinq visionnages complets.
- Tests navigateur intégrés : PASS, huit clips originaux joués, pause/reset, comparaison candidat à temps identique, durée conservée, sélecteurs .25/.5/1/1.5/1.75/2, quatre largeurs mobiles, taps émulés, retour/export/effacement. Les contrôles de vitesse sont testés, pas la qualité visuelle de chaque cycle à toutes les vitesses.
- npm test : PASS. Serveur isolé : PASS. Verrouillage public navigateur : PASS.
- Build séparé démo : PASS. Les listes Docker incluent le clip candidat interne, le constructeur public ne l'inclut pas.

Non faits : Safari/iPhone physique, réseau mobile, collision exhaustive maillage/maillage, audit complet des poids de skinning, forces/centre de gravité, validation biomécanique, visionnage expert des huit cycles à chaque vitesse, déploiement Render. Prochain correctif à instruire : localiser les pics jumping jacks par os et phase, mesurer réception/contacts avant toute nouvelle variante.
