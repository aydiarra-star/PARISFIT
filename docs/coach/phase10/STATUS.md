# État des vérifications

- Run46052018457 : deux jobs réussis (calculs, exports, Three.js, films et régressions) ; annotations incomplètes, transport corrigé ensuite.
- Run46052597634, commit e5c34ea : job Blender-control **VALIDÉ**, six rapports récupérés sans perte et vérifiés ; job `validate` **REFUSÉ** à l'étape Browser regression and3D tests. Détail du log inaccessible via le proxy (EOF) ; aucune cause précise affirmée. La demande de relance ciblée a été rejetée par GitHub. Ne pas confondre succès de ce job de contrôle avec succès global de cette exécution.
- Tests locaux : `npm test`,22tests de contrats,12tests d'intake/autorisations, contrôles de la page phase10 et liens à320/390/768/1200px réussis.7mutations de géométrie et8décodages vidéo exécutés dans le job Blender-control.
- Une nouvelle exécution sur le commit de livraison est demandée par le push. Son état final sera indiqué dans la PR, sans modifier rétrospectivement ces preuves.
- Films/GLB : artifact GitHub produit, téléchargement ici en échec EOF ; revue visuelle/professionnelle toujours en attente. L'archive ne contient que la fixture publique, aucune capture privée.
