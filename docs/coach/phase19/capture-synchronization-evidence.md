> Supplément Phase19 — 2026-11-27 (date de session). Référence immuable : `71bae7d1ed34227b2fc2c1c4e79aa7fdf1be22f1`. AB01 / Squat / 1 et Static / 1. Les phases17–18 ne sont ni remplacées ni réexécutées.

# Synchronisation capture / plateformes

## Établi dans les fichiers — sans refaire l'audit18

Source : [audit byte-à-byte conservé](../phase18/c3d-independent-byte-audit.json), [interprétation](../phase18/c3d-integrity-and-timing.md), lecture limitée des groupes de métadonnées phase19 dans [inventaire](local-and-preserved-inventory.json).

- Points **200Hz**, analogiques **1000Hz**, cinq sous-échantillons analogiques par frame ;2948 frames dynamiques et1565 statiques. En-têtes zéro-based cohérents (0..2947 et0..1564).
- Squat : temps points0–14.735s ; analogiques0–14.739s. Statique : points0–7.82s ;7825 échantillons analogiques. La queue4ms est une conséquence de grille, **pas une latence mesurée**.
- Les seuls groupes présents sont POINT, ANALOG, FORCE_PLATFORM, MANUFACTURER, SUBJECTS ; pas de groupe EVENT ni TRIAL. Les36 canaux analogiques sont Fx/Fy/Fz/Mx/My/Mz de6 plateformes, sans canal de trigger explicitement étiqueté. « Skeleton » n'est pas un horodatage ou identifiant de séance.
- Les horodatages du journal OpenSim sont des heures de **traitement**, pas des timestamps d'exposition caméra ni de conversion ADC.

## Non établi

L'article décrit12 caméras PrimeX22 et6 plateformes Kistler9260AA6, fréquences et calibration générique. Aucune preuve AB01 retrouvée du câblage de déclenchement, horloge maîtresse, configuration de synchronisation, latence calibrée, dérive ou test d'impulsion commune. Une fréquence dans le C3D et un ratio entier ne prouvent pas un alignement physique. L'absence de canal de trigger étiqueté ne prouve pas l'absence d'une synchronisation matérielle externe.

Aucun offset imposé, aucune estimation de délai par corrélation, aucun filtre, COP, correction ni trajectoire calculée. Le registre distingue **grille numérique vérifiée** et **synchronisation physique partielle**. Il faut une configuration/log de séance et une caractérisation de timing pour fermer ce point ; aucune demande n'a été envoyée.
