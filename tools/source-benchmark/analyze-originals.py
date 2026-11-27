"""Original-file availability audit. Marker and joint derivatives are NOT interchangeable."""
from pathlib import Path
import json,io,gzip,csv,hashlib,numpy as np
root=Path('.cache/phase12/originals');out=[]
p=root/'14_06.c3d'
if p.exists():
 r={'id':'CMU14_06/C3D','status':'NON TESTÉ'}
 try:
  import c3d
  with p.open('rb') as f:
   reader=c3d.Reader(f);labels=[str(x).strip() for x in reader.point_labels];rate=reader.point_rate;units=reader.get('POINT:UNITS').string_value.strip().lower();scale={'mm':.001,'cm':.01,'m':1}.get(units)
   if scale is None:raise ValueError('UNSUPPORTED_UNITS:'+units)
   frames=[];valid=[];ids=[]
   for number,points,analog in reader.read_frames():ids.append(number);frames.append(points[:,:3].copy()*scale);valid.append((points[:,3]>=0)&np.isfinite(points[:,:3]).all(axis=1))
  positions=np.array(frames);valid=np.array(valid);good=valid[:-2]&valid[1:-1]&valid[2:];acc=np.linalg.norm(np.diff(positions,n=2,axis=0)*rate**2,axis=2);masked=np.where(good,acc,np.nan);i,j=np.unravel_index(np.nanargmax(masked),masked.shape)
  r.update(status='EN ATTENTE DE VALIDATION HUMAINE',sampleHz=rate,frames=len(frames),units=units,consecutiveFrameNumbers=bool(np.all(np.diff(ids)==1)),markerCount=len(labels),labels=labels,invalidPointObservations=int((~valid).sum()),maxValidMarkerAccelerationMS2=float(masked[i,j]),peakMarker=labels[j],peakFrame=ids[i+1],meaning='all C3D point channels, including possible Vicon model outputs; not mapped to anatomical pivots, not a causal comparison with BVH',sha256=hashlib.sha256(p.read_bytes()).hexdigest())
 except Exception as e:r['error']=str(e)
 out.append(r)
else:out.append({'id':'CMU14_06/C3D','status':'NON TESTÉ','reason':'original file unavailable'})
p=root/'14_06.amc'
if p.exists():
 r={'id':'CMU14_06/AMC','status':'NON TESTÉ'}
 try:
  frames=[];current=None
  for line in p.read_text().splitlines():
   parts=line.split()
   if not parts or parts[0].startswith(('#',':')):continue
   if len(parts)==1 and parts[0].isdigit():current={};frames.append(current)
   elif current is not None:current[parts[0]]=[float(v) for v in parts[1:]]
  sets=[set(f) for f in frames];rootpos=np.array([f['root'][:3] for f in frames])*.056444;rate=120.;acc=np.linalg.norm(np.diff(rootpos,n=2,axis=0)*rate**2,axis=1)
  r.update(status='EN ATTENTE DE VALIDATION HUMAINE',frames=len(frames),sameJointSet=all(s==sets[0] for s in sets),joints=sorted(sets[0]),assumedHzFromPrimaryCatalog=120,maxRootTranslationAccelerationMS2=float(acc.max()),meaning='root translation only;120Hz from CMU catalogue, not AMC timestamps; no AMC FK anatomical comparison')
 except Exception as e:r['error']=str(e)
 out.append(r)
else:out.append({'id':'CMU14_06/AMC','status':'NON TESTÉ','reason':'original file unavailable'})
p=root/'zenodo-P001_markers.csv.gz'
if p.exists():
 r={'id':'Zenodo23979972/S01/P001','status':'NON TESTÉ'}
 try:
  text=gzip.decompress(p.read_bytes()).decode();table=np.genfromtxt(io.StringIO(text),delimiter=',',names=True);names=list(table.dtype.names);r['columns']=names
  if 'time' not in names:raise ValueError('EXPLICIT_TIME_COLUMN_REQUIRED')
  times=table['time'];intervals=np.diff(times)
  if not (np.isfinite(times).all() and np.all(intervals>0)):raise ValueError('INVALID_TIME')
  r.update(status='EN ATTENTE DE VALIDATION HUMAINE',frames=len(times),medianHz=float(1/np.median(intervals)),minDt=float(intervals.min()),maxDt=float(intervals.max()),nonfiniteValues=int(sum(np.count_nonzero(~np.isfinite(table[n])) for n in names)),durationS=float(times[-1]-times[0]),meaning='marker time/finite screening only. Column-to-anatomy calibration and paired forces NOT qualified; no joint-pivot ranking against CMU')
 except Exception as e:r['error']=str(e)
 out.append(r)
else:out.append({'id':'Zenodo23979972/S01/P001','status':'NON TESTÉ','reason':'download unavailable; metadata alone does not qualify quality'})
(root.parent/'original-analysis.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
