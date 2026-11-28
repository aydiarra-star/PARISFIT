"""Measured-marker benchmark, not joint-centre reconstruction or animation input."""
from pathlib import Path
import numpy as np,json,gzip,io,csv,subprocess,hashlib
from PIL import Image,ImageDraw
root=Path('.cache/phase12');src=root/'originals';out={'status':'NON TESTÉ','qualifiedReference':False}
def table(name):return np.genfromtxt(io.StringIO(gzip.decompress((src/name).read_bytes()).decode()),delimiter=',',names=True)
try:
 data=table('zenodo-P001_markers.csv.gz');force=table('zenodo-P001_force_plates.csv.gz');assert np.max(np.abs(data['time']-force['time']))<1e-6,'FORCE_TIME_MISMATCH'
 reps=list(csv.DictReader((src/'zenodo-squat_repetitions.csv').read_text().splitlines()));rep=next(r for r in reps if r['trial']=='P001' and r['rep']=='1');start,bottom,end=[float(rep[k]) for k in ['t_start','t_bottom','t_end']];mask=(data['time']>=start-1e-8)&(data['time']<=end+1e-8);data=data[mask];force=force[mask];t=data['time'];dt=np.diff(t)
 assert np.all(dt>0) and np.ptp(dt)<1e-6,'IRREGULAR_MARKER_TIME'
 names=[n[:-2] for n in data.dtype.names if n.endswith('_x')];p=np.stack([np.stack([data[n+'_'+a] for a in 'xyz'],axis=1) for n in names],axis=1);assert np.isfinite(p).all(),'MISSING_MARKERS'
 def marker(name):return p[:,names.index(name)]
 def angle(a,b,c):
  u=a-b;v=c-b;return 180-np.rad2deg(np.arccos(np.clip(np.sum(u*v,axis=1)/(np.linalg.norm(u,axis=1)*np.linalg.norm(v,axis=1)),-1,1)))
 v=np.diff(p,axis=0)/dt[:,None,None];a=np.diff(v,axis=0)/((dt[1:]+dt[:-1])/2)[:,None,None];norm=np.linalg.norm(a,axis=2);i,j=np.unravel_index(norm.argmax(),norm.shape)
 feet={};knees={}
 for side,plate in [('Right',1),('Left',2)]:
  heel=marker(side+'_calcaneal_tuberosity');toe=marker(side+'_1st_metatarsal_head');F=force['PLATE_'+str(plate)+'_Fz'];loaded=F>20
  # No contact patch inferred from marker height; force association is a documented hypothesis.
  feet[side]={'plateAssignmentHypothesis':plate,'minFzN':float(F.min()),'maxFzN':float(F.max()),'fractionAbove20N':float(loaded.mean()),'heelHorizontalRangeM':np.ptp(heel[:,:2],axis=0).tolist(),'heelMaxDisplacementFromStartM':float(np.linalg.norm(heel[:,:2]-heel[0,:2],axis=1).max()),'heelHeightRangeM':[float(heel[:,2].min()),float(heel[:,2].max())],'metatarsalHeightRangeM':[float(toe[:,2].min()),float(toe[:,2].max())],'notSoleGap':True}
  k=angle(marker(side+'_greater_trochanter'),marker(side+'_lateral_epicondyle'),marker(side+'_lateral_malleolus'));knees[side]={'min':float(k.min()),'max':float(k.max()),'meaning':'skin-marker three-point proxy, NOT anatomical knee angle'}
 pelvis=(marker('Right_ASIC')+marker('Left_ASIC')+marker('Right_sacral_crest')+marker('Left_sacral_crest'))/4;shoulders=(marker('Right_acromioclavicular_joint')+marker('Left_acromioclavicular_joint'))/2;trunk=shoulders-pelvis;tilt=np.rad2deg(np.arccos(np.clip(trunk[:,2]/np.linalg.norm(trunk,axis=1),-1,1)))
 out.update(status='EN ATTENTE DE VALIDATION HUMAINE',id='Zenodo23979972/v1/S01/P001/rep1',times={'start':start,'bottom':bottom,'end':end},frames=len(t),sampleHz=float(1/np.median(dt)),axes='Z-up inferred from ground-plane x/y plate centres and marker/force axes; confirm with depositor before retarget',units='m per dataset README; N for forces',maxMarkerSpeedMS=float(np.linalg.norm(v,axis=2).max()),maxMarkerAccelerationMS2=float(norm.max()),peakMarker=names[j],peakTime=float(t[i+1]),feet=feet,kneeProxyDeg=knees,trunkProxyTiltDeg={'min':float(tilt.min()),'max':float(tilt.max())},pelvisProxyMaxAccelerationMS2=float(np.linalg.norm(np.diff(pelvis,n=2,axis=0)/np.median(dt)**2,axis=1).max()),entryExitMarkerMaxDistanceM=float(np.linalg.norm(p[-1]-p[0],axis=1).max()),comparison='do NOT rank marker acceleration against BVH pivot acceleration; no joint-centre model or matched variant',blockers=['no stable preparation/final hold in this cropped repetition','loaded fatigue squat, not unweighted control','anatomical joint axes uncalibrated','plate-to-foot mapping and ground reference pending review','no professional review'])
 (root/'marker-rep1.npz').parent.mkdir(parents=True,exist_ok=True);np.savez_compressed(root/'marker-rep1.npz',time=t,positions=p,names=names,force1=force['PLATE_1_Fz'],force2=force['PLATE_2_Fz'])
 origin=pelvis[0].copy();origin[2]=0
 def draw(i):
  im=Image.new('RGB',(960,380),'#edf5ef');d=ImageDraw.Draw(im);q=p[i]-origin
  d.text((12,8),'Michaud 2026 / CC BY4.0 / S01 P001 rep1 | markers, NOT joint centres | t='+str(round(t[i],2)),fill='#164b39')
  for view in range(3):
   x=q[:,0] if view==0 else q[:,1] if view==1 else (q[:,0]+q[:,1])/2**.5
   for xx,zz in zip(x,q[:,2]):
    xx=int(view*320+160+xx*150);yy=int(330-zz*150);d.ellipse((xx-2,yy-2,xx+2,yy+2),fill='#164b39')
   d.text((view*320+12,35),['Front-like','Side-like','Oblique'][view]+' | lab axes',fill='#164b39')
  d.text((12,352),'Plate1 Fz='+str(round(force['PLATE_1_Fz'][i],1))+' N | Plate2 Fz='+str(round(force['PLATE_2_Fz'][i],1))+' N | no PARISFIT capture',fill='#84301f');return im
 dest=root/'marker-rep1.mp4';proc=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s','960x380','-r','100','-i','pipe:0','-an','-c:v','libx264','-pix_fmt','yuv420p','-movflags','+faststart',str(dest)],stdin=subprocess.PIPE)
 for i in range(len(t)):proc.stdin.write(draw(i).tobytes())
 proc.stdin.close();assert proc.wait()==0
 draw(int(np.argmin(abs(t-bottom)))).save(root/'marker-preview.png');out['video']={'file':dest.name,'frames':len(t),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
 dec=subprocess.run(['ffmpeg','-v','error','-i',str(dest),'-f','null','-'],capture_output=True,text=True,check=True);assert not dec.stderr.strip();out['video']['decode']='VALIDÉ'
except Exception as e:out['error']=str(e)
(root/'marker-benchmark.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
