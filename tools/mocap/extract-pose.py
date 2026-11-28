"""Local-only MediaPipe 0.10.21 extraction. Public licensed fixture; no uploads.
Not calibrated mocap: image/world landmarks are model estimates, not measurements.
"""
from pathlib import Path
import json,hashlib,time,subprocess
import cv2,numpy as np,mediapipe as mp,imageio_ffmpeg
root=Path('docs/coach/phase5');source=root/'source.webm';cap=cv2.VideoCapture(str(source));fps=cap.get(cv2.CAP_PROP_FPS);assert 1<fps<121
frames=[];start=time.time();ff=imageio_ffmpeg.get_ffmpeg_exe()
encoder=subprocess.Popen([ff,'-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s','640x360','-r',str(fps),'-i','pipe:0','-an','-c:v','libx264','-pix_fmt','yuv420p','-movflags','+faststart',str(root/'pose-overlay.mp4')],stdin=subprocess.PIPE)
with mp.solutions.pose.Pose(model_complexity=1,smooth_landmarks=True,min_detection_confidence=.5,min_tracking_confidence=.5) as pose:
 while True:
  ok,image=cap.read()
  if not ok:break
  result=pose.process(cv2.cvtColor(image,cv2.COLOR_BGR2RGB));f={'time':len(frames)/fps,'detected':bool(result.pose_landmarks)}
  if result.pose_landmarks and result.pose_world_landmarks:
   f['image']=[[p.x,p.y,p.z,p.visibility] for p in result.pose_landmarks.landmark];f['world']=[[p.x,p.y,p.z,p.visibility] for p in result.pose_world_landmarks.landmark]
   mp.solutions.drawing_utils.draw_landmarks(image,result.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
  frames.append(f);image=cv2.resize(image,(640,360));cv2.rectangle(image,(0,322),(640,360),(245,245,245),-1);cv2.putText(image,'FitnessScape | CC BY 3.0 | MediaPipe estimated pose, not mocap',(8,337),cv2.FONT_HERSHEY_SIMPLEX,.38,(30,70,45),1);cv2.putText(image,f't={f["time"]:.2f}s | PARISFIT research only, no professional validation',(8,353),cv2.FONT_HERSHEY_SIMPLEX,.36,(30,70,45),1);encoder.stdin.write(cv2.cvtColor(image,cv2.COLOR_BGR2RGB).tobytes())
cap.release();encoder.stdin.close();assert encoder.wait()==0
assert all(f['detected'] for f in frames),'Missing poses: explicit gap handling required before retargeting'
# A centred five-frame mean reduces jitter offline, but blurs timing and is not a physical filter.
for field in ['image','world']:
 data=np.array([f[field] for f in frames]);smooth=np.stack([np.mean(data[max(0,i-2):min(len(data),i+3),:,:3],axis=0) for i in range(len(data))])
 for i,f in enumerate(frames):f[field+'Filtered']=[list(smooth[i,j])+[data[i,j,3]] for j in range(33)]
model=Path(mp.__file__).parent/'modules/pose_landmark/pose_landmark_full.tflite'
report={'sourceSHA256':hashlib.sha256(source.read_bytes()).hexdigest(),'mediapipe':mp.__version__,'modelSHA256':hashlib.sha256(model.read_bytes()).hexdigest(),'fps':fps,'frames':len(frames),'detected':sum(f['detected'] for f in frames),'cpuElapsedSeconds':time.time()-start,'method':'monocular model inference, local CPU; not instrumented mocap','filter':'centred 5-frame mean on coordinates; no interpolation of missing detections','visibilityMinByLandmark':np.min(np.array([f['image'] for f in frames])[:,:,3],axis=0).tolist(),'framesData':frames}
(root/'pose-estimates.json').write_text(json.dumps(report,separators=(',',':'))+'\n');print({k:v for k,v in report.items() if k not in ['framesData','visibilityMinByLandmark']})
