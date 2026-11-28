# Fatigue_Squat_2026 dataset

Motion capture, ground reaction forces and knee extension force of 11 healthy young adults during a resistance
training session of repeated dumbbell squats, and the OpenSim model used in the associated article
("Toward Real-Time Estimation of Muscle Force and Fatigue During Resistance Training Using a Neural Network
Surrogate of OpenSim Musculotendon Kinematics").

## Protocol
MVC0 (P000) - three cycles of three sets of 15 squats, each followed by an MVC - MVC4 about 1 h later.

| Trial | Content |
|---|---|
| P000, P004, P008, P012, P013 | MVC0, MVC1, MVC2, MVC3, MVC4 (isometric right knee extension, hip and knee at 90 deg) |
| P001-P003, P005-P007, P009-P011 | Squat sets of cycles 1, 2 and 3 |

## Files
- `participants.csv`: body mass (kg), dumbbell mass (kg), lever arm of the MVC force (m) and six surrogate scale factors
  (pelvis P1-P3, femur Fem, tibia Tib, foot Foot). P1-P3 are the scale factors along the three pelvis axes.
- `measured_mvc.csv`: peak force at each MVC (N) and percentage of MVC0.
- `participants/Sxx/` (all the files of a set share the same `time` column, in s)
  - `static_markers.csv.gz`: static capture used for scaling.
  - `Pxxx_markers.csv.gz`: reconstructed trajectories of the 37 markers (m, laboratory frame), 100 Hz, cropped to the set.
  - `Pxxx_force_plates.csv.gz`: unfiltered forces (N) and moments (N m) of plates 1 and 2, 100 Hz.
  - `MVCn_Pxxx_force.csv.gz`: load cell signal and force (N), unfiltered, 100 Hz. Force = 119.715 x signal - 1.59 N.
  - `squat_repetitions.csv`: start, bottom and end time of each repetition (s).
  - `rest_schedule.csv`: rest after each capture (s). `measured`: from capture times; otherwise nominal.
- `model/LaiUhlrich2022_symmetric.osim`: generic OpenSim 4.6 musculoskeletal model used in the study, with left-right symmetric
  wrapping surfaces and the 37 laboratory markers.

In `force_plates` the plate centres are at (x, y) = (-0.698, 0) m for plate 1 and
(0, 0) m for plate 2, in the laboratory frame.

## Participants
Participants are identified by codes in random order.

## License
This dataset is distributed under the Creative Commons Attribution 4.0 International license (CC BY 4.0,
https://creativecommons.org/licenses/by/4.0/). If you use it, please cite the associated article and this dataset.
