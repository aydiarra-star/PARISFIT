# Sources professionnelles et retargeting — décision phase 3

## Source réellement intégrée à la galerie

Microsoft Rocketbox, révision figée `0943055db6ec570bcef9f2c8b41c9e5467c808f9` : bibliothèque officielle annoncée à 417 animations. Deux fichiers masculins `m_crouch_in.max.fbx` et `m_crouch_out.max.fbx`, dossier `all_animations_max_motextr_xy`, ont été téléchargés via l’API GitHub puis leur SHA Git de blob vérifié. La notice MIT (copyright Microsoft 2020) est conservée dans `assets/coach/licenses/ROCKETBOX-MIT.txt`. Aucun fichier de licence distinct dans le sous-arbre Animations au commit examiné.

Les chemins, tailles et identifiants exacts figurent dans `assets/coach/transitions/source.json`. Le script `tools/download-coach-transitions.py` est reproductible. FBX bruts en cache, pas d’ajout inutile des sources volumineuses au dépôt. Deux sources féminines du dossier `static` ont aussi été essayées localement, sans être retenues ni distribuées.

Références officielles :
- https://github.com/microsoft/Microsoft-Rocketbox/tree/0943055db6ec570bcef9f2c8b41c9e5467c808f9/Assets/Animations
- https://github.com/microsoft/Microsoft-Rocketbox/blob/0943055db6ec570bcef9f2c8b41c9e5467c808f9/LICENSE.md
- https://github.com/microsoft/Microsoft-Rocketbox/blob/0943055db6ec570bcef9f2c8b41c9e5467c808f9/README.md

**Droits retenus :** MIT permet adaptation, redistribution et usage commercial avec maintien de la notice. **Méthode de production :** aucune attestation par fichier de capture réelle ni de démonstration sportive professionnelle ; ne pas présenter ces clips comme mocap certifiée. Ce sont des animations humaines de bibliothèque, pas une validation d’exercice.

## Résultat concret versus auteur IK de phase 2

| Point | Huit exercices phase 2 | Deux candidates Rocketbox |
|---|---|---|
| Origine | Courbes et IK originales PARISFIT | Courbes complètes issues des fichiers officiels |
| Temporalité | Cycles et phases pédagogiques écrits | Timing source 4,5 s, asymétrie et repositionnement conservés |
| Squelette | Rocketbox corrigé | Transfert des rotations monde vers le même squelette, aucun des 80 os absent |
| Segments | Longueurs du modèle conservées | Idem ; translation racine mise à l’échelle selon longueurs des jambes |
| Contact | Appuis spécifiques aux exercices, garde-fous 60 Hz | Recalage vertical global seulement ; pas d’ancrage latéral, calendrier de contact non validé |
| Raccord | Boucles testées | Pas de correspondance approuvée avec l’entrée/sortie des exercices |
| Diffusion | Parcours existant, mention expérimentale | Galerie uniquement, HOLD |

Le comparatif « avant/après » phase 3 signifie **retarget brut / retarget avec recalage vertical**. L’ajustement n’est que de quelques millimètres ; il ne faut pas le présenter comme une refonte spectaculaire de la gestuelle. Les vidéos phase 2 restent la référence des exercices actuels. Aucun clip ne couvre le passage complet debout→sol→debout.

## Autres pistes, sans achat ni importation non autorisée

L’étude de phase 2 reste disponible dans `../phase2/MOTION-SOURCES.md` : MoCapAct (code MIT, dataset annoncé CDLA-Permissive-2.0) nécessite sélection et retargeting de trajectoires d’humanoïde simulé ; aucune couverture des six transferts vérifiée. Les fichiers distants ne sont pas acquis ici. LaFAN1 est exclu pour la licence CC BY-NC-ND 4.0. Mixamo n’est pas intégré sans vérification des droits de redistribution des fichiers dans ce dépôt public. Le fait qu’une animation soit lisible par Three.js n’accorde aucun droit sur son contenu.

Pour les cinq transferts manquants, privilégier une capture consentie d’un professionnel ou une bibliothèque avec droits commerciaux/redistribution vérifiés et séquences exactes. Exiger poses neutres de calibration, échelle, pieds/mains visibles, fréquence connue, sol fixe, données de contact si disponibles, accord écrit et licence de livraison. Faire retargeter puis revoir contacts, doigts, auto-intersections et raccords. Aucun prestataire contacté, aucune validation obtenue et aucun coût engagé.
