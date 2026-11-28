# Final author enquiry — English

**Ready for the user's sending decision. NOT SENT. No contact made and no response obtained.**

**Subject: Reproducing S01/P001 — MarkerSet and scaling, dataset 10.5281/zenodo.23979972 v1**

Dear Dr Michaud and colleagues,

We are examining the reproducibility of S01/P001 for PARISFIT. S01 is the anonymized participant; P001 denotes their first squat set, not another participant. Our analysis targets `participants/S01/P001_markers.csv.gz` and the static capture in that folder. The README describes a generic model containing the 37 laboratory markers; the supplied XML contains 66 markers whose names differ from the 37 CSV labels. We would like to understand this difference without assuming anatomical correspondences.

Could you please point us to the following materials, if available?

1. **MarkerSet and placement:** the capture and model MarkerSets actually used, their official correspondence table, palpation protocol, offsets and local frames. Could you clarify `ASIC`, `sacral_crest` and `forearm_centre`, excluded markers and virtual centres? This would distinguish skin landmarks from joint centres.
2. **S01 configuration:** the individualized S01 model, or the exact template and files/scripts needed to reproduce it. Is the distributed XML the template used before individualization?
3. **Six factors:** for S01 we read P1=1.07737, P2=1.08037, P3=1.08637, Fem=1.07018, Tib=1.08885 and Foot=1.14237. Could you confirm their reference geometry, axes/bodies, any isotropic application, operation order and treatment of other segments, masses and inertias? Are these surrogate inputs or a complete reproducible scaling specification? This would prevent applying factors to incorrect axes.
4. **Registration:** static pose and time window, model marker placement, weights, constraints and any manual marker adjustments. This would distinguish skeletal scaling from marker registration.
5. **Frames and acquisition:** signed axes, units and laboratory/force-plate/OpenSim transformations, moment origins, plate geometry, synchronization, gap filling and filtering. These are needed to compare trajectories with forces correctly.
6. **Computational reproduction:** scaling, IK or simulation settings and export scripts, plus the associated article DOI/preprint and supplements. We would retain the parameters and limitations rather than reproduce only a visual result.
7. **Reuse:** preferred attribution and confirmation of the scope of CC BY 4.0, including commercial reuse of the data, together with any separate model/component licences and notices.

A public, versioned response linked to the dataset would be ideal. If an item does not exist or cannot be shared, knowing that limitation would also help. We do not request participant identities, consent signatures or private videos. No IK will be run using merely plausible correspondences.

Thank you for your assistance.

Reference: https://doi.org/10.5281/zenodo.23979972 ; model `LaiUhlrich2022_symmetric.osim`, SHA256 `42eca458626f42aa1e49d5925e14ec3c16fe81324293bacece643e11319ddbd9`.
