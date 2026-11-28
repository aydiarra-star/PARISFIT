# Extraits officiels numérotés — lecture seule

Référence Git `a26fe4852a78f30c5e8a437b158847031cb8dc3c`. Numéros de lignes dans les fichiers originaux, empreintes dans source-manifest.json. Citations limitées à l’audit ; espaces de fin de ligne retirés pour présentation, octets originaux inchangés dans le cache ; aucun code exécuté.

## MATLAB tools/trial_class.m

```text
35:     num_forceplates = 6;
36:     force_thresh = 20;
37:     f_cutoff = 6;
38:     f_sample = 1000;
39:
```

```text
127:     function set_paths(trial_class)
128:         trial_class.c3d_path = '../Data';
129:         trial_class.cur_dir = pwd;
130:         trial_class.staticTrcFile_rel = '../../Static/1/Data/static.trc';
131:         trial_class.trcFile = strcat('../Data/',trial_class.trial_name,'.trc');
132:         trial_class.grfMotFile = strcat('../Data/',trial_class.trial_name,'.mot');
133:
134:         trial_class.scaleXml_rel = '../../Static/1/Setup/Setup_Scale.xml';
135:         trial_class.ikXml = '../Setup/Setup_IK.xml';
136:         trial_class.idXml = '../Setup/Setup_ID.xml';
137:         mkdir('../generated');
138:
139:         % Get the absolute path
140:         trial_class.staticTrcFile = fullfile(fileparts(pwd), trial_class.staticTrcFile_rel);
141:         trial_class.scaleXml = fullfile(fileparts(pwd), trial_class.scaleXml_rel);
142:         %%
143:         trial_class.osimOutputFile_dir = strcat([trial_class.cur_dir,'../generated/Generated_Model.osim']);
144:         trial_class.osimOutputFile = '../generated/Generated_Model.osim';
```

```text
191:     function init_forceplate_data(trial_class)
192:
193:         trial_class.c3dpath = fullfile(trial_class.c3d_path,trial_class.c3d_filename);
194:         %% Construct an opensimC3D object with input c3d path
195:         % Constructor takes full path to c3d file and an integer for forceplate
196:         % representation (1 = COP).
197:         trial_class.c3d = osimC3D(trial_class.c3dpath,1);
198:
199:         %% Get some stats...
200:         % Get the number of marker trajectories
201:         trial_class.nTrajectories = trial_class.c3d.getNumTrajectories();
202:         % Get the marker data rate
203:         trial_class.rMakers = trial_class.c3d.getRate_marker();
204:         % Get the number of forces
205:         trial_class.nForces = trial_class.c3d.getNumForces();
206:         % Get the force data rate
207:         trial_class.rForces = trial_class.c3d.getRate_force();
208:
209:         % Get Start and end time
210:         trial_class.t0 = trial_class.c3d.getStartTime();
211:         trial_class.tn = trial_class.c3d.getEndTime();
212:         %% Rotate the data
213:         trial_class.c3d.rotateData('x',-90)
214:
215:         %% Get the c3d in different forms
216:         % Get OpenSim tables
217:         trial_class.markerTable = trial_class.c3d.getTable_markers();
218:         trial_class.forceTable = trial_class.c3d.getTable_forces();
```

```text
264:         for i = 1:trial_class.num_forceplates
265:
266:             trial_class.forceStruct_len(i) = length(trial_class.forceStruct_f{i});
267:             % trial_class.f_z_filt{i} = lowpass(trial_class.forceStruct_f{i}(:,2), trial_class.f_cutoff, trial_class.f_sample);
268:             trial_class.f_z_filt{i} = smoothdata(trial_class.forceStruct_f{i}(:,2), 'gaussian', 30);
269:
270:
271:             % Goal: find the last sample before losing contact (before <
272:             % thresh) and the first sample after contact (after > thresh).
273:
274:             below_thresh_mask = trial_class.f_z_filt{i} < trial_class.force_thresh;
275:             trial_class.f_z_ind{i} = below_thresh_mask;
276:             trial_class.d_f_z{i} = [0;diff(trial_class.f_z_ind{i})];
277:
278:             below_thresh_ind = find(trial_class.d_f_z{i}==1)-1;
279:
280:             above_thresh_mask = trial_class.f_z_filt{i} > trial_class.force_thresh;
281:             above_thresh_diff = [0;diff(above_thresh_mask)];
282:             above_thresh_ind = find(above_thresh_diff==1);
283:
284:             trial_class.d_f_z_ind{i} = sort([below_thresh_ind;above_thresh_ind]);
285:
286:         end
```

```text
317:     function set_forceplate_contacts(trial_class, num, c)
318:         % num: force plate number
319:         % Number of contacts
320:
321:         trial_class.fp_contact_inds_low{num} = trial_class.fp_contact_inds{num};
322:         % Note about the second condition: in some trials such as sit to stand, we always have contact so
323:         % while fp_contact_inds_high is empty. So for those, we don't need
324:         % to assign it to fp_contact_inds.
325:         if (trial_class.id_enabled == 1 && ~isempty(trial_class.fp_contact_inds_high) && ~isempty(trial_class.fp_contact_inds_high{num} ))
326:             trial_class.fp_contact_inds{num} = trial_class.fp_contact_inds_high{num};
327:         end
328:
329:         % This can happen in foot on chair; technically, there was contact,
330:         % but it was below the threshold. So we ignore them for inverse
331:         % dynamics purposes.
332:         % Find the number
333:         low_force_contact = isnan(trial_class.fp_contact_inds{num});
334:         % At least one element in the row is NaN (actually, both are NaNs).
335:         low_force_contact_ind = find( sum(low_force_contact,2) ~= 0);
336:
337:         if (trial_class.id_enabled == 1)
338:             % Remove the low force contacts.
339:             c = c - length(low_force_contact_ind);
340:             trial_class.fp_contact_inds_backup{num} = trial_class.fp_contact_inds{num};
341:             trial_class.fp_contact_inds{num}(low_force_contact_ind,:) = [];
342:             % Note: all of the ~isempty( trial_class.fp_contact_inds{num})
343:             % conditions are related to this.
344:         end
345:
346:         % If there were contacts with the force plate, set the force and CoP between the contacts to 0.
347:         if (c > 1)
348:             %for i = 1:length(trial_class.fp_contact_inds{num})-1
349:             for i = 1:c-1
350:                 trial_class.forceStruct_f{num}(trial_class.fp_contact_inds{num}(i,2):trial_class.fp_contact_inds{num}(i+1,1),:) = 0;
351:                 trial_class.forceStruct_p{num}(trial_class.fp_contact_inds{num}(i,2):trial_class.fp_contact_inds{num}(i+1,1),:) = 0;
352:             end
353:
354:         else
355:             temp = trial_class.forceStruct_f{num};
356:             trial_class.forceStruct_f{num}(:) = 0;
357:             if (~isempty( trial_class.fp_contact_inds{num}))
358:                 trial_class.forceStruct_f{num}(trial_class.fp_contact_inds{num}(1,1):trial_class.fp_contact_inds{num}(1,2),:) = ...
359:                     temp(trial_class.fp_contact_inds{num}(1,1):trial_class.fp_contact_inds{num}(1,2),:);
360:             end
361:
362:             temp = trial_class.forceStruct_p{num};
363:             trial_class.forceStruct_p{num}(:) = 0;
364:             if (~isempty( trial_class.fp_contact_inds{num}))
365:                 trial_class.forceStruct_p{num}(trial_class.fp_contact_inds{num}(1,1):trial_class.fp_contact_inds{num}(1,2),:) =...
366:                     temp(trial_class.fp_contact_inds{num}(1,1):trial_class.fp_contact_inds{num}(1,2),:);
367:             end
368:         end
369:
370:         if (~isempty(trial_class.fp_contact_inds{num}))
371:             if (trial_class.fp_contact_inds{num}(1,1) > 1)
372:                 trial_class.forceStruct_f{num}(1:trial_class.fp_contact_inds{num}(1,1)-1,:) = 0;
373:                 trial_class.forceStruct_p{num}(1:trial_class.fp_contact_inds{num}(1,1)-1,:) = 0;
374:             end
375:
376:             if (trial_class.fp_contact_inds{num}(end,2) < trial_class.forceStruct_len(1))
377:                 trial_class.forceStruct_f{num}(trial_class.fp_contact_inds{num}(end,2)+1:trial_class.forceStruct_len(1),:) = 0;
378:                 trial_class.forceStruct_p{num}(trial_class.fp_contact_inds{num}(end,2)+1:trial_class.forceStruct_len(1),:) = 0;
379:             end
380:         end
381:
382:     end
```

```text
444:     function set_foot_force_data(trial_class, p, c, right_foot)
445:
446:         if (trial_class.id_enabled == 1 && ~isempty(trial_class.fp_contact_inds{p}) && ...
447:                 ~(isnan(trial_class.fp_contact_inds_backup{p}(c,1)) || isnan(trial_class.fp_contact_inds_backup{p}(c,2))))
448:
449:             if (right_foot)
450:
451:                 ind_range = trial_class.fp_contact_inds_backup{p}(c,1):trial_class.fp_contact_inds_backup{p}(c,2);
452:                 trial_class.f_right(ind_range,:) = trial_class.forceStruct_f{p}(ind_range,:);
453:                 trial_class.p_right(ind_range,:) = trial_class.forceStruct_p{p}(ind_range,:);
454:
455:             else
456:
457:                 ind_range = trial_class.fp_contact_inds_backup{p}(c,1):trial_class.fp_contact_inds_backup{p}(c,2);
458:                 trial_class.f_left(ind_range,:) = trial_class.forceStruct_f{p}(ind_range,:);
459:                 trial_class.p_left(ind_range,:) = trial_class.forceStruct_p{p}(ind_range,:);
460:
461:             end
462:
463:         end
```

```text
484:     function update_forcestruct_data(trial_class)
485:
486:         trial_class.forceStruct.f1 = trial_class.f_right;
487:         trial_class.forceStruct.p1 = trial_class.p_right;
488:
489:         trial_class.forceStruct.f2 = trial_class.f_left;
490:         trial_class.forceStruct.p2 = trial_class.p_left;
491:
492:         trial_class.forceStruct.p3(isnan(trial_class.forceStruct.p3)) = 0;
493:         trial_class.forceStruct.p4(isnan(trial_class.forceStruct.p4)) = 0;
494:         trial_class.forceStruct.p5(isnan(trial_class.forceStruct.p5)) = 0;
495:         trial_class.forceStruct.p6(isnan(trial_class.forceStruct.p6)) = 0;
496:         %%
```

```text
616:     function export_trc_mot_files(trial_class)
617:     %Write the marker and force data to file
618:
619:     % Write marker data to trc file.
620:     trial_class.c3d.writeTRC(strcat(trial_class.trial_name,'.trc'));
621:
622:     % Write force data to mot file.
623:     trial_class.c3d.writeMOT(strcat(trial_class.trial_name,'.mot'));
624:
625:     end
626:
627:     function osim_scale(trial_class)
628:
629:         Osim.Scale(trial_class.staticTrcFile,trial_class.scaleXml,trial_class.osimOutputFile);
630:
631:     end
632:
633:     function osim_ik(trial_class)
634:
635:         [JointKinematicsTable, errorInfo, trial_class.ikMotOutputFile] =...
636:             Osim.IK(trial_class.trcFile, trial_class.ikXml, trial_class.ikMotOutputFile);
637:
638:         [fig_rms, trial_class.max_error, trial_class.rms_error] = Osim.viewIKError(errorInfo);
639:
640:         if trial_class.results_fig_visible == 1
```

```text
770:     function osim_id(trial_class)
771:
772:         if (trial_class.id_enabled == 1)
773:
774:             forcePlatesUsed = {'ground_force_1', 'ground_force_2'};
775:             grfMotTable = Osim.readMOT(trial_class.grfMotFile);
776:             columnsToKeep = contains(grfMotTable.Properties.VariableNames, forcePlatesUsed);
777:             columnsToKeep(1) = true; % keep Header column
778:             grfMotTable = grfMotTable(:, columnsToKeep);
779:
780:             sides = 'rl';
781:             trial_class.extLoadsFile = Osim.createExternalLoads(forcePlatesUsed, sides, trial_class.extLoadsFile);
782:
783:             trial_class.extLoadsFile = GetFullPath(trial_class.extLoadsFile);
784:
785:             trial_class.idXmlUpdated = Osim.editSetupXML(trial_class.idXml, 'external_loads_file', trial_class.extLoadsFile, 'FilePath', trial_class.idXmlUpdated);
786:             %% Compute Inverse Dynamics
787:             [JointTorquesTable, trial_class.stoOutputFile] = Osim.ID(trial_class.grfMotFile,trial_class.idXmlUpdated,trial_class.ikMotOutputFile,trial_class.stoOutputFile);
788:
789:             data = JointTorquesTable;
790:             trial_id_results = data;
```

## AB01/Squat/1/Processing/process_trial_data.m

```text
1: clear;
2: close all;
3: trial_name = 'squat_1';
4: c3d_filename = 'squat_1.c3d';
5:
6: trial = trial_class(trial_name, c3d_filename);
7: trial.set_paths();
8: %%
9: trial.init_forceplate_data();
10: process_force_data;
11: trial.update_forcestruct_data();
12: trial.export_trc_mot_files();
13: %%
14: trial.osim_scale();
15:
16: trial.osim_ik();
17:
18: trial.osim_com();
19:
20: trial.osim_id();
21:
22: trial.plot_results();
```

## AB01/Squat/1/Processing/process_force_data.m

```text
1: fp_num = 1;
2: trial.plot_forceplate_data(fp_num);
3:
4: % Contact 1 start --- Contact 1 end
5: % Contact 2 start --- Contact 2 end
6: % ...
7: trial.fp_contact_inds{fp_num} = zeros(1,2);
8:
9: c = 1;
10: trial.fp_contact_inds{fp_num}(c,1) = 1;
11: trial.fp_contact_inds{fp_num}(c,2) = trial.forceStruct_len(fp_num);
12:
13: trial.set_forceplate_contacts(fp_num, c);
14: %%
15: fp_num = 2;
16: trial.plot_forceplate_data(fp_num);
17:
18: trial.fp_contact_inds{fp_num} = zeros(1,2);
19:
20: c = 1;
21: trial.fp_contact_inds{fp_num}(c,1) = 1;
22: trial.fp_contact_inds{fp_num}(c,2) = trial.forceStruct_len(fp_num);
23:
24: trial.set_forceplate_contacts(fp_num, c);
25: %%
26: fp_num = 3;
27: trial.plot_forceplate_data(fp_num);
28:
29: trial.fp_contact_inds{fp_num} = zeros(1,2);
30:
31: c = 1;
32: trial.fp_contact_inds{fp_num}(c,1) = 1;
33: trial.fp_contact_inds{fp_num}(c,2) = trial.forceStruct_len(fp_num);
34:
35: trial.set_forceplate_contacts(fp_num, c);
36: %%
37: fp_num = 4;
38: trial.plot_forceplate_data(fp_num);
39:
40: trial.fp_contact_inds{fp_num} = zeros(1,2);
41:
42: c = 1;
43: trial.fp_contact_inds{fp_num}(c,1) = 1;
44: trial.fp_contact_inds{fp_num}(c,2) = trial.forceStruct_len(fp_num);
45:
46: trial.set_forceplate_contacts(fp_num, c);
47: %%
48: fp_num = 5;
49: trial.plot_forceplate_data(fp_num);
50:
51: trial.fp_contact_inds{fp_num} = zeros(1,2);
52:
53: c = 1;
54: trial.fp_contact_inds{fp_num}(c,1) = 1;
55: trial.fp_contact_inds{fp_num}(c,2) = trial.forceStruct_len(fp_num);
56:
57: trial.set_forceplate_contacts(fp_num, c);
58: %%
59: fp_num = 6;
60: trial.plot_forceplate_data(fp_num);
61:
62: trial.fp_contact_inds{fp_num} = zeros(1,2);
63:
64: c = 1;
65: trial.fp_contact_inds{fp_num}(c,1) = 1;
66: trial.fp_contact_inds{fp_num}(c,2) = trial.forceStruct_len(fp_num);
67:
68: trial.set_forceplate_contacts(fp_num, c);
69: %%
70: trial.plot_all_forceplates();
71: %% Right foot data
72: is_right_foot = 1;
73:
74: % Have to look at the data in Motive.
75: % First part of the right foot force. c'th contact interval of force plate p.
76: p = 1;
77: c = 1;
78: trial.set_foot_force_data(p, c, is_right_foot);
79:
80:
81: %% Left foot data
82: is_right_foot = 0;
83:
84: p = 2;
85: c = 1;
86: trial.set_foot_force_data(p, c, is_right_foot);
87:
```

## AB01/Static/1/Setup/Setup_Scale.xml

```text
1: <?xml version="1.0" encoding="UTF-8" ?>
2: <OpenSimDocument Version="40000">
3: 	<ScaleTool name="FullBodyModel_MuscleActuatedLowerLimb_TorqueActuatedUpperBody-scaled">
4: 		<!--Mass of the subject in kg.  Subject-specific model generated by scaling step will have this total mass.-->
5: 		<mass>49.81</mass>
6: 		<!--Height of the subject in mm.  For informational purposes only (not used by scaling).-->
7: 		<height>-1</height>
8: 		<!--Age of the subject in years.  For informational purposes only (not used by scaling).-->
9: 		<age>-1</age>
10: 		<!--Notes for the subject.-->
11: 		<notes>Unassigned</notes>
12: 		<!--Specifies the name of the unscaled model (.osim) and the marker set.-->
13: 		<GenericModelMaker>
14: 			<!--Model file (.osim) for the unscaled model.-->
15: 			<model_file>../../../../Model/Biomech57.osim</model_file>
16: 			<!--Set of model markers used to scale the model. Scaling is done based on distances between model markers compared to the same distances between the corresponding experimental markers.-->
17: 			<marker_set_file>../../../../Model/marker_set.xml</marker_set_file>
18: 		</GenericModelMaker>
19: 		<!--Specifies parameters for scaling the model.-->
20: 		<ModelScaler>
21: 			<!--Whether or not to use the model scaler during scale-->
22: 			<apply>true</apply>
23: 			<!--Specifies the scaling method and order. Valid options are 'measurements', 'manualScale', singly or both in any sequence.-->
24: 			<scaling_order> measurements</scaling_order>
25: 			<!--Specifies the measurements by which body segments are to be scaled.-->
```

```text
544: 				</objects>
545: 				<groups />
546: 			</MeasurementSet>
547: 			<!--Scale factors to be used for manual scaling.-->
548: 			<ScaleSet>
549: 				<objects />
550: 				<groups />
551: 			</ScaleSet>
552: 			<!--TRC file (.trc) containing the marker positions used for measurement-based scaling. This is usually a static trial, but doesn't need to be.  The marker-pair distances are computed for each time step in the TRC file and averaged across the time range.-->
553: 			<marker_file>Unassigned</marker_file>
554: 			<!--Time range over which to average marker-pair distances in the marker file (.trc) for measurement-based scaling.-->
555: 			<time_range>Unassigned</time_range>
556: 			<!--Flag (true or false) indicating whether or not to preserve relative mass between segments.-->
557: 			<preserve_mass_distribution>true</preserve_mass_distribution>
558: 			<!--Name of OpenSim model file (.osim) to write when done scaling.-->
559: 			<output_model_file />
560: 			<!--Name of file to write containing the scale factors that were applied to the unscaled model (optional).-->
561: 			<output_model_file />
562: 		</ModelScaler>
563: 		<!--Specifies parameters for placing markers on the model once a model is scaled. -->
564: 		<MarkerPlacer>
565: 			<!--Whether or not to use the marker placer during scale-->
566: 			<apply>true</apply>
567: 			<!--Task set used to specify weights used in the IK computation of the static pose.-->
568: 			<IKTaskSet>
569: 				<objects>
570: 					<IKMarkerTask name="RCAJ">
571: 						<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
572: 						<apply>true</apply>
573: 						<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
574: 						<weight>1</weight>
```

```text
910: 						<weight>1</weight>
911: 					</IKMarkerTask>
912: 				</objects>
913: 				<groups />
914: 			</IKTaskSet>
915: 			<!--TRC file (.trc) containing the time history of experimental marker positions (usually a static trial).-->
916: 			<marker_file>Unassigned</marker_file>
917: 			<!--Name of file containing the joint angles used to set the initial configuration of the model for the purpose of placing the markers. These coordinate values can also be included in the optimization problem used to place the markers. Before the model markers are placed, a single frame of an inverse kinematics (IK) problem is solved. The IK problem can be solved simply by matching marker positions, but if the model markers are not in the correct locations, the IK solution will not be very good and neither will marker placement. Alternatively, coordinate values (specified in this file) can be specified and used to influence the IK solution. This is valuable particularly if you have high confidence in the coordinate values. For example, you know for the static trial the subject was standing will all joint angles close to zero. If the coordinate set (see the CoordinateSet property) contains non-zero weights for coordinates, the IK solution will try to match not only the marker positions, but also the coordinates in this file. Least-squared error is used to solve the IK problem. -->
918: 			<coordinate_file>Unassigned</coordinate_file>
919: 			<!--Time range over which the marker positions are averaged.-->
920: 			<time_range>Unassigned</time_range>
921: 			<!--Name of the motion file (.mot) written after marker relocation (optional).-->
922: 			<output_motion_file>Unassigned</output_motion_file>
923: 			<!--Output OpenSim model file (.osim) after scaling and maker placement.-->
924: 			<output_model_file>Unassigned</output_model_file>
925: 			<!--Output marker set containing the new marker locations after markers have been placed.-->
926: 			<output_marker_file>Unassigned</output_marker_file>
927: 			<!--Maximum amount of movement allowed in marker data when averaging frames of the static trial. A negative value means there is not limit.-->
928: 			<max_marker_movement>-1</max_marker_movement>
929: 		</MarkerPlacer>
930: 	</ScaleTool>
931: </OpenSimDocument>
```

## AB01/Static/1/Setup/Setup_Scale_GUI.xml

```text
1: <?xml version="1.0" encoding="UTF-8" ?>
2: <OpenSimDocument Version="40000">
3: 	<ScaleTool name="FullBodyModel_MuscleActuatedLowerLimb_TorqueActuatedUpperBody-scaled">
4: 		<!--Mass of the subject in kg.  Subject-specific model generated by scaling step will have this total mass.-->
5: 		<mass>49.81</mass>
6: 		<!--Height of the subject in mm.  For informational purposes only (not used by scaling).-->
7: 		<height>-1</height>
8: 		<!--Age of the subject in years.  For informational purposes only (not used by scaling).-->
9: 		<age>-1</age>
10: 		<!--Notes for the subject.-->
11: 		<notes>Unassigned</notes>
12: 		<!--Specifies the name of the unscaled model (.osim) and the marker set.-->
13: 		<GenericModelMaker>
14: 			<!--Model file (.osim) for the unscaled model.-->
15: 			<model_file>Unassigned</model_file>
16: 			<!--Set of model markers used to scale the model. Scaling is done based on distances between model markers compared to the same distances between the corresponding experimental markers.-->
17: 			<marker_set_file>Unassigned</marker_set_file>
18: 		</GenericModelMaker>
19: 		<!--Specifies parameters for scaling the model.-->
20: 		<ModelScaler>
21: 			<!--Whether or not to use the model scaler during scale-->
22: 			<apply>true</apply>
23: 			<!--Specifies the scaling method and order. Valid options are 'measurements', 'manualScale', singly or both in any sequence.-->
24: 			<scaling_order> measurements</scaling_order>
25: 			<!--Specifies the measurements by which body segments are to be scaled.-->
```

```text
544: 				</objects>
545: 				<groups />
546: 			</MeasurementSet>
547: 			<!--Scale factors to be used for manual scaling.-->
548: 			<ScaleSet>
549: 				<objects />
550: 				<groups />
551: 			</ScaleSet>
552: 			<!--TRC file (.trc) containing the marker positions used for measurement-based scaling. This is usually a static trial, but doesn't need to be.  The marker-pair distances are computed for each time step in the TRC file and averaged across the time range.-->
553: 			<marker_file>../Data/static.trc</marker_file>
554: 			<!--Time range over which to average marker-pair distances in the marker file (.trc) for measurement-based scaling.-->
555: 			<time_range> 0 7.82</time_range>
556: 			<!--Flag (true or false) indicating whether or not to preserve relative mass between segments.-->
557: 			<preserve_mass_distribution>true</preserve_mass_distribution>
558: 			<!--Name of OpenSim model file (.osim) to write when done scaling.-->
559: 			<output_model_file>Unassigned</output_model_file>
560: 			<!--Name of file to write containing the scale factors that were applied to the unscaled model (optional).-->
561: 			<output_scale_file>Unassigned</output_scale_file>
562: 		</ModelScaler>
563: 		<!--Specifies parameters for placing markers on the model once a model is scaled. -->
564: 		<MarkerPlacer>
565: 			<!--Whether or not to use the marker placer during scale-->
566: 			<apply>true</apply>
567: 			<!--Task set used to specify weights used in the IK computation of the static pose.-->
568: 			<IKTaskSet>
569: 				<objects>
570: 					<IKMarkerTask name="RCAJ">
571: 						<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
572: 						<apply>true</apply>
573: 						<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
574: 						<weight>1</weight>
```

```text
910: 						<weight>1</weight>
911: 					</IKMarkerTask>
912: 				</objects>
913: 				<groups />
914: 			</IKTaskSet>
915: 			<!--TRC file (.trc) containing the time history of experimental marker positions (usually a static trial).-->
916: 			<marker_file>../Data/static.trc</marker_file>
917: 			<!--Name of file containing the joint angles used to set the initial configuration of the model for the purpose of placing the markers. These coordinate values can also be included in the optimization problem used to place the markers. Before the model markers are placed, a single frame of an inverse kinematics (IK) problem is solved. The IK problem can be solved simply by matching marker positions, but if the model markers are not in the correct locations, the IK solution will not be very good and neither will marker placement. Alternatively, coordinate values (specified in this file) can be specified and used to influence the IK solution. This is valuable particularly if you have high confidence in the coordinate values. For example, you know for the static trial the subject was standing will all joint angles close to zero. If the coordinate set (see the CoordinateSet property) contains non-zero weights for coordinates, the IK solution will try to match not only the marker positions, but also the coordinates in this file. Least-squared error is used to solve the IK problem. -->
918: 			<coordinate_file>Unassigned</coordinate_file>
919: 			<!--Time range over which the marker positions are averaged.-->
920: 			<time_range> 0 7.82</time_range>
921: 			<!--Name of the motion file (.mot) written after marker relocation (optional).-->
922: 			<output_motion_file>Unassigned</output_motion_file>
923: 			<!--Output OpenSim model file (.osim) after scaling and maker placement.-->
924: 			<output_model_file>Unassigned</output_model_file>
925: 			<!--Output marker set containing the new marker locations after markers have been placed.-->
926: 			<output_marker_file>Unassigned</output_marker_file>
927: 			<!--Maximum amount of movement allowed in marker data when averaging frames of the static trial. A negative value means there is not limit.-->
928: 			<max_marker_movement>-1</max_marker_movement>
929: 		</MarkerPlacer>
930: 	</ScaleTool>
931: </OpenSimDocument>
```

## AB01/Squat/1/Setup/Setup_IK.xml

```text
1: <?xml version="1.0" encoding="UTF-8" ?>
2: <OpenSimDocument Version="40000">
3: 	<InverseKinematicsTool>
4: 		<!--Directory used for writing results.-->
5: 		<results_directory>./</results_directory>
6: 		<!--Directory for input files-->
7: 		<input_directory />
8: 		<!--Name of the model file (.osim) to use for inverse kinematics.-->
9: 		<model_file>../generated/Generated_Model.osim</model_file>
10: 		<!--A positive scalar that weights the relative importance of satisfying constraints. A weighting of 'Infinity' (the default) results in the constraints being strictly enforced. Otherwise, the weighted-squared constraint errors are appended to the cost function.-->
11: 		<constraint_weight>Inf</constraint_weight>
12: 		<!--The accuracy of the solution in absolute terms. Default is 1e-5. It determines the number of significant digits to which the solution can be trusted.-->
13: 		<accuracy>1.0000000000000001e-05</accuracy>
14: 		<!--Markers and coordinates to be considered (tasks) and their weightings. The sum of weighted-squared task errors composes the cost function.-->
15: 		<IKTaskSet>
16: 			<objects>
17: 				<IKMarkerTask name="SJN">
18: 					<!--Whether or not this task will be used during inverse kinematics solve, default is true.-->
19: 					<apply>true</apply>
20: 					<!--Weight given to the task when solving inverse kinematics problems, default is 0.-->
21: 					<weight>1</weight>
22: 				</IKMarkerTask>
```

```text
310: 				</IKMarkerTask>
311: 			</objects>
312: 			<groups />
313: 		</IKTaskSet>
314: 		<!--TRC file (.trc) containing the time history of observations of marker positions obtained during a motion capture experiment. Markers in this file that have a corresponding task and model marker are included.-->
315: 		<marker_file>Unassigned</marker_file>
316: 		<!--The name of the storage (.sto or .mot) file containing the time history of coordinate observations. Coordinate values from this file are included if there is a corresponding model coordinate and task. -->
317: 		<coordinate_file>Unassigned</coordinate_file>
318: 		<!--The desired time range over which inverse kinematics is solved. The closest start and final times from the provided observations are used to specify the actual time range to be processed.-->
319: 		<time_range>Unassigned</time_range>
320: 		<!--Flag (true or false) indicating whether or not to report marker errors from the inverse kinematics solution.-->
321: 		<report_errors>false</report_errors>
322: 		<!--Name of the resulting inverse kinematics motion (.mot) file.-->
323: 		<output_motion_file>Unassigned</output_motion_file>
324: 		<!--Flag indicating whether or not to report model marker locations. Note, model marker locations are expressed in Ground.-->
325: 		<report_marker_locations>false</report_marker_locations>
326: 	</InverseKinematicsTool>
327: </OpenSimDocument>
```

## AB01/Squat/1/Setup/Setup_External_Forces.xml

```text
1: <?xml version="1.0" encoding="utf-8"?>
2: <OpenSimDocument Version="40000">
3: 	<ExternalLoads>
4: 		<objects>
5: 			<ExternalForce name="ExternalForce_1">
6: 				<!--Name of the body the force is applied to.-->
7: 				<applied_to_body> calcn_r </applied_to_body>
8: 				<!--Name of the body the force is expressed in (default is ground).-->
9: 				<force_expressed_in_body> ground </force_expressed_in_body>
10: 				<!--Name of the body the point is expressed in (default is ground).-->
11: 				<point_expressed_in_body> ground </point_expressed_in_body>
12: 				<!--Identifier (string) to locate the force to be applied in the data
13: 				    source.-->
14: 				<force_identifier> ground_force_1_v </force_identifier>
15: 				<!--Identifier (string) to locate the point to be applied in the data
16: 				    source.-->
17: 				<point_identifier> ground_force_1_p </point_identifier>
18: 				<!--Identifier (string) to locate the torque to be applied in the data
19: 				    source.-->
20: 				<torque_identifier/>
21: 				<!--Name of the data source (Storage) that will supply the force data.-->
22: 				<data_source_name> Unassigned </data_source_name>
23: 			</ExternalForce>
24: 			<ExternalForce name="ExternalForce_2">
25: 				<!--Name of the body the force is applied to.-->
26: 				<applied_to_body> calcn_l </applied_to_body>
27: 				<!--Name of the body the force is expressed in (default is ground).-->
28: 				<force_expressed_in_body> ground </force_expressed_in_body>
29: 				<!--Name of the body the point is expressed in (default is ground).-->
30: 				<point_expressed_in_body> ground </point_expressed_in_body>
31: 				<!--Identifier (string) to locate the force to be applied in the data
32: 				    source.-->
33: 				<force_identifier> ground_force_2_v </force_identifier>
34: 				<!--Identifier (string) to locate the point to be applied in the data
35: 				    source.-->
36: 				<point_identifier> ground_force_2_p </point_identifier>
37: 				<!--Identifier (string) to locate the torque to be applied in the data
38: 				    source.-->
39: 				<torque_identifier/>
40: 				<!--Name of the data source (Storage) that will supply the force data.-->
41: 				<data_source_name> Unassigned </data_source_name>
42: 			</ExternalForce>
43: 		</objects>
44:     	<groups/>
45:         <datafile>Unassigned</datafile>
46:         <external_loads_model_kinematics_file/>
47:         <lowpass_cutoff_frequency_for_load_kinematics>-1</lowpass_cutoff_frequency_for_load_kinematics>
48: 	</ExternalLoads>
49: </OpenSimDocument>
```

## All subjects processing/save_data_info.m

```text
1: clear;
2: close all;
3:
4: subject_ids = ["AB01", "AB02", "AB03", "AB04", "AB05", ...
5:     "AB06", "AB07", "AB08", "AB09", "AB10"];
6:
7: subject_masses = [49.81	 65.2	60.01	64.16	71.08	74.22	67.58	49.89	55.99	78.66];
8: subject_heights = [173	176	170	175.26	182.88	177.8	168	170	156	185.42]/100;
9:
10: trial_names = ["Static", "Sit to stand", "Stand to sit", "Foot on chair", "Stride",...
11:     "Look behind", "Feet together", "Eyes closed", "Turn", "Tandem feet",...
12:     "One leg", "Squat", "Reach forward", "Object pickup", "Shoe lace"];
13:
14: trial_nums = 1:length(trial_names);
15: trial_dict = dictionary(trial_names, trial_nums);
16:
17: repeats = ["1","2","3"];
18:
19: num_subjects = length(subject_ids);
20: num_trials = length(trial_names);
21: num_repeats = length(repeats);
22:
23: save('data_info');
```

## All subjects processing/add_to_path.m

```text
1: %% Add the folders to the MATLAB path
2: addpath(fullfile(pwd, '../MATLAB tools/'));
3:
4: % Display a confirmation message
5: disp(['Added to path: ', fullfile(pwd, '../MATLAB tools/')]);
```

## Model/Biomech57.osim

```text
29: 		<credits>Rajagopal, A, Dembia, C.L., DeMers, M.S., Delp, D.D., Hicks, J.L., and Delp, S.L.</credits>
30: 		<!--Publications and references associated with the model.-->
31: 		<publications>Rajagopal, Apoorva, et al. "Full-Body Musculoskeletal Model for Muscle-Driven Simulation of Human Gait." IEEE Transactions on Biomedical Engineering 63.10 (2016): 2068-2079. (2016)</publications>
32: 		<!--Units for all lengths.-->
33: 		<length_units>meters</length_units>
34: 		<!--Units for all forces.-->
35: 		<force_units>N</force_units>
```

```text
5759: 				<CoordinateCouplerConstraint name="patellofemoral_knee_angle_r_con">
5760: 					<!--Flag indicating whether the constraint is enforced or not.Enforced means that the constraint is active in subsequent dynamics realizations. NOTE: Prior to OpenSim 4.0, this behavior was controlled by the 'isDisabled' property, where 'true' meant the constraint was not being enforced. Thus, if 'isDisabled' is'true', then 'isEnforced' is false.-->
5761: 					<isEnforced>true</isEnforced>
5762: 					<!--Constraint function of generalized coordinates (to be specified) used to evaluate the constraint errors and their derivatives, and must valid to at least 2nd order. Constraint function must evaluate to zero when coordinates satisfy the constraint.-->
5763: 					<coupled_coordinates_function>
5764: 						<LinearFunction>
5765: 							<coefficients> 1 0</coefficients>
5766: 						</LinearFunction>
5767: 					</coupled_coordinates_function>
5768: 					<!--List of names of the right hand side (independent) coordinates. Note the constraint function above, must be able to handle multiple coordinate values if more than one coordinate name is provided.-->
5769: 					<independent_coordinate_names>knee_angle_r</independent_coordinate_names>
5770: 					<!--Name of the left-hand side (dependent) coordinate of the constraint coupling function.-->
5771: 					<dependent_coordinate_name>knee_angle_r_beta</dependent_coordinate_name>
5772: 					<!--Scale factor for the coupling function.-->
5773: 					<scale_factor>1</scale_factor>
5774: 				</CoordinateCouplerConstraint>
5775: 				<CoordinateCouplerConstraint name="patellofemoral_knee_angle_l_con">
5776: 					<!--Flag indicating whether the constraint is enforced or not.Enforced means that the constraint is active in subsequent dynamics realizations. NOTE: Prior to OpenSim 4.0, this behavior was controlled by the 'isDisabled' property, where 'true' meant the constraint was not being enforced. Thus, if 'isDisabled' is'true', then 'isEnforced' is false.-->
5777: 					<isEnforced>true</isEnforced>
5778: 					<!--Constraint function of generalized coordinates (to be specified) used to evaluate the constraint errors and their derivatives, and must valid to at least 2nd order. Constraint function must evaluate to zero when coordinates satisfy the constraint.-->
5779: 					<coupled_coordinates_function>
5780: 						<LinearFunction>
5781: 							<coefficients> 1 0</coefficients>
5782: 						</LinearFunction>
5783: 					</coupled_coordinates_function>
5784: 					<!--List of names of the right hand side (independent) coordinates. Note the constraint function above, must be able to handle multiple coordinate values if more than one coordinate name is provided.-->
5785: 					<independent_coordinate_names>knee_angle_l</independent_coordinate_names>
5786: 					<!--Name of the left-hand side (dependent) coordinate of the constraint coupling function.-->
5787: 					<dependent_coordinate_name>knee_angle_l_beta</dependent_coordinate_name>
5788: 					<!--Scale factor for the coupling function.-->
5789: 					<scale_factor>1</scale_factor>
5790: 				</CoordinateCouplerConstraint>
5791: 			</objects>
5792: 			<groups />
```
