from pathlib import Path
import subprocess,os,io
from PIL import Image,ImageDraw
stage=os.environ.get('STAGE','before');ff=os.environ['FFMPEG_PATH'];root=Path('docs/coach/phase2')/stage
import json
for clip in json.loads((root/'capture-manifest.json').read_text())['clips']:
 sheet=Image.new('RGB',(1440,750),'white');draw=ImageDraw.Draw(sheet)
 for row,view in enumerate(['face','profil','trois-quarts']):
  for col in range(8):
   t=clip['duration']*col/8
   raw=subprocess.check_output([ff,'-loglevel','error','-ss',str(t),'-i',str(root/(clip['name']+'-'+view+'.mp4')),'-frames:v','1','-f','image2pipe','-vcodec','png','-'])
   im=Image.open(io.BytesIO(raw));im.thumbnail((180,230));sheet.paste(im,(col*180,row*250+20));draw.text((col*180+4,row*250+4),f'{view} {t:.2f}s',fill='black')
 sheet.save(root/(clip['name']+'-sequence.jpg'),quality=90)
