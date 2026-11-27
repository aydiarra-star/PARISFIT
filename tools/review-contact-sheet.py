"""Build review sheets from real browser screenshots, never synthesized illustrations."""
from PIL import Image,ImageDraw
from pathlib import Path
ids=['squat','pompes','gainage','fentes','jumpingjacks','mountainclimber','etirementdos','mobiliteepaules']
Path('docs/coach/evidence').mkdir(parents=True,exist_ok=True)
for view in [0,1,2]:
 im=Image.new('RGB',(1200,870),'white');d=ImageDraw.Draw(im)
 for i,id in enumerate(ids):
  a=Image.open(f'.cache/coach-review/{id}-{view}.png').convert('RGB')
  if view==2:
   crop=a.crop((0,0,a.width,a.height-45));crop.thumbnail((300,360));crop.save(f'assets/coach/previews/{id}.jpg',quality=88)
  a.thumbnail((300,400));x=(i%4)*300;y=(i//4)*435;im.paste(a,(x,y+25));d.text((x+5,y+5),id,fill='black')
 im.save(f'docs/coach/evidence/eight-exercises-{view}.jpg',quality=90)
Image.open('.cache/coach-review/mobile-390.png').convert('RGB').save('docs/coach/evidence/mobile-390.jpg',quality=90)
