"""Documentary mapping: curated official definitions, never joint-centre estimation."""
import csv,json,collections,struct
from pathlib import Path
D=Path('docs/coach/phase17');URL='https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57'
# key: label suffix (or unpaired label), site, segment in documentation, source section, ambiguity
DEFS={
'AH':('Front, côté antérieur','Tête','Head Markers',''),
'PH':('Tête postérieure, environ 2 cm derrière l’oreille','Tête','Head Markers',''),
'SJN':('Incisure jugulaire du sternum','Thorax','Torso Markers',''),
'SXS':('Processus xiphoïde ; placement 1–2 cm au-dessus de la jonction des côtes','Thorax','Torso Markers',''),
'CV7':('Processus palpable de la septième vertèbre cervicale','Thorax','Torso Markers',''),
'TV2':('Deuxième vertèbre thoracique selon le titre','Thorax','Torso Markers','Texte dit aussi «three spine levels below C7» : discordance de niveau à vérifier, non corrigée silencieusement.'),
'TV7':('Septième vertèbre thoracique','Thorax','Torso Markers',''),
'HGT':('Face postérieure de l’axe de l’épaule, intitulée glenohumeral joint','Bras / épaule','Torso Markers','Aucun centre glénohuméral profond observé ; XML rattache au torso, pas à humerus.'),
'IAS':('Épine iliaque antérieure selon texte de placement','Bassin','Waist Markers','Alias PSIS dans le tableau contredit anterior/front ; direction retenue seulement comme plausible, pas correction de la source.'),
'IPS':('Épine iliaque postérieure selon texte de placement','Bassin','Waist Markers','Alias ASIS contredit posterior/dimples ; direction retenue seulement comme plausible.'),
'CAJ':('Proéminence clavicule-acromion, sommet de l’épaule','Thorax','Upper Extremity Markers','Repère superficiel, pas centre de rotation de l’épaule.'),
'HLE':('Épicondyle latéral de l’humérus','Bras','Upper Extremity Markers',''),
'HME':('Épicondyle médial de l’humérus','Bras','Upper Extremity Markers',''),
'UA':('Bras, sillon entre les triceps en T-pose','Bras','Upper Extremity Markers',''),
'HM2':('Sous l’articulation de l’index selon placement','Main','Hand Markers','Source écrit «Hand Second metatarsal» ; métacarpien paraît cohérent mais non démontré par ce libellé. Offset asymétrique conseillé.'),
'USP':('Processus styloïde ulnaire selon nom','Main','Hand Markers','Placement source «lateral side» : orientation anatomique ambiguë ; XML rattache à radius et non ulna.'),
'RSP':('Processus styloïde radial selon nom','Main','Hand Markers','Placement source «medial side» : orientation anatomique ambiguë ; ne pas inverser les labels.'),
'FTC':('Proéminence du grand trochanter fémoral','Bassin','Lower Extremity Markers','Source et XML rattachent au bassin malgré repère sur fémur ; hypothèse de rigidité à contester.'),
'FLE':('Épicondyle latéral fémoral','Cuisse','Lower Extremity Markers',''),
'FME':('Épicondyle médial fémoral','Cuisse','Lower Extremity Markers',''),
'TH':('Face antérieure de la cuisse, proche de la ligne médiane','Cuisse','Lower Extremity Markers','Hauteurs asymétriques droite/gauche conseillées ; pas un centre articulaire.'),
'SK':('Tibia antérieur près de la ligne médiane selon placement','Jambe selon placement','Lower Extremity Markers','Table affiche «Upper Leg / Superior Knee» mais décrit le shin/lower leg : garder ambiguïté documentaire.'),
'TTC':('Tubérosité tibiale, point antérieur 2–3 cm sous la patella','Jambe','Lower Extremity Markers',''),
'FAX':('Proéminence latérale proximale de la fibula','Jambe','Lower Extremity Markers',''),
'FAL':('Malléole latérale','Jambe / pied','Foot Markers',''),
'TAM':('Malléole médiale selon placement','Jambe / pied','Foot Markers','Titre «Talus Ankle Medial» conservé ; la malléole médiale est tibiale, pas centre de cheville.'),
'FM5':('Face dorsale du cinquième métatarsien','Pied','Foot Markers',''),
'FM2':('Face dorsale du deuxième métatarsien','Pied','Foot Markers',''),
'FM1':('Face dorsale du premier métatarsien','Pied','Foot Markers',''),
'FCC':('Talon, insertion du tendon d’Achille sur le calcanéus','Pied','Foot Markers',''),
'DP1':('Extrémité distale du gros orteil','Orteils','Foot Markers','XML rattache au calcn et non toes ; pas de mesure indépendante de flexion MTP.')}
AMB={'TV2','IAS','IPS','HM2','USP','RSP','SK'}
JOINTS={'head':'head_joint','torso':'back / acromial_r / acromial_l / head_joint','pelvis':'ground_pelvis / hip_r / hip_l / back','humerus':'acromial / elbow','radius':'radioulnar / radius_hand','hand':'radius_hand','femur':'hip / walker_knee','tibia':'walker_knee / ankle','calcn':'subtalar / mtp'}
def main():
 j=json.loads((D/'configuration-inspection.json').read_text());rows=[]
 for m in j['markers']:
  name=m['name'];key=name if name in DEFS else name[1:];site,seg,section,note=DEFS[key];body=m['parent'].split('/')[-1];base=body.rsplit('_',1)[0] if body.endswith(('_l','_r')) else body
  role=('Calibration statique retirée avant les tâches' if not m['dynamicPresent'] else 'Suivi de segment / tâche IK de marqueur')+' ; rôle de calcul confirmé dans XML, pas centre articulaire'
  rows.append({'original_name':name,'documented_anatomical_location':site,'anatomical_segment':seg,'side':'gauche' if name.startswith('L') else 'droite' if name.startswith('R') else 'médian','biomechanical_role':role,'anatomical_status':'Plausible' if key in AMB else 'Confirmé','confidence_scope':'Définition documentaire seulement ; palpation individuelle AB01 non vérifiée','opensim_parent_frame':m['parent'],'opensim_attachment_status':'Confirmé','opensim_local_location_m':' '.join(str(v) for v in m['location']),'opensim_joint_relevance':JOINTS[base]+(' (côté '+body[-1]+')' if body.endswith(('_r','_l')) else ''),'opensim_joint_status':'Plausible','joint_centre_equivalence':'Inconnu — aucune équivalence marqueur-centre admise','rocketbox_correspondence':'Aucune correspondance anatomique établie','rocketbox_status':'Inconnu','static_present':str(m['staticPresent']).lower(),'dynamic_present':str(m['dynamicPresent']).lower(),'marker_fixed':m['fixed'] if m['fixed'] is not None else 'Inconnu — champ absent, défaut logiciel à vérifier','justification':note or 'Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel.','source_documentation':URL+' — '+section+' ; article PMC12717423 Figure1/Participant Preparation','source_xml':'Model/marker_set.xml:L'+str(m['line'])+'–'+str(m['line']+7)})
 with (D/'marker-anatomical-mapping.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
 (D/'mapping-status.json').write_text(json.dumps({'anatomicalDefinitions':dict(collections.Counter(r['anatomical_status'] for r in rows)),'explicitOpenSimAttachments':57,'confirmedJointCentres':0,'confirmedRocketboxMappings':0,'decision':'B','expertReviewed':False,'IKExecuted':False,'retargetExecuted':False,'trajectoryCorrected':False,'runtimeChanged':False,'MichaudFactorsTransferred':False},ensure_ascii=False,indent=2)+'\n')
 # Schematic inventory by body region, deliberately not a reconstructed person or calibrated geometry.
 groups=collections.defaultdict(list)
 for r in rows:groups[r['anatomical_segment']].append(r['original_name']+('*' if r['dynamic_present']=='false' else '')+('?' if r['anatomical_status']=='Plausible' else ''))
 import html
 svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 1100" role="img" aria-label="Schéma documentaire des 57 marqueurs regroupés par région, non anatomométrique"><rect width="880" height="1100" fill="#edf5ef"/><g font-family="sans-serif" fill="#173f33"><text x="28" y="38" font-size="24">57 marqueurs · schéma documentaire par région</text><text x="28" y="68" font-size="16">Pas une reconstruction anatomique. * calibration retirée ; ? définition ambiguë.</text>'
 for i,(group,names) in enumerate(groups.items()):
  x=28+(i%2)*424;y=95+(i//2)*130;svg+=f'<rect x="{x}" y="{y}" width="398" height="112" rx="10" fill="white"/><text x="{x+14}" y="{y+28}" font-size="18">{html.escape(group)}</text>'
  for a in range(0,len(names),5):svg+=f'<text x="{x+14}" y="{y+56+(a//5)*23}" font-size="16">{html.escape(" · ".join(names[a:a+5]))}</text>'
 svg+='<text x="28" y="1068" font-size="15">Source : OptiTrack Biomech57 + XML épinglé ; voir le CSV pour contester chaque ligne.</text></g></svg>'
 (D/'markerset-schematic.svg').write_text(svg)
 # Record actual Rocketbox names, no mapping inferred.
 b=Path('assets/coach/coach.glb').read_bytes();ln=struct.unpack_from('<I',b,12)[0];g=json.loads(b[20:20+ln]);(D/'rocketbox-readonly.json').write_text(json.dumps({'skinJointNames':[g['nodes'][i].get('name') for i in g['skins'][0]['joints']],'clipNames':[a['name'] for a in g['animations']],'mappingInferred':False,'modified':False},indent=2)+'\n')
if __name__=='__main__':main()
