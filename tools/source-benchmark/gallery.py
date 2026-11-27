from pathlib import Path
import json,hashlib,shutil
root=Path('.cache/phase12')
page='''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PARISFIT · Source benchmark</title><style>body{font:16px/1.6 system-ui;color:#164b39;background:#edf5ef;max-width:1100px;margin:auto;padding:20px}video,img{max-width:100%}article{background:white;padding:20px;margin:20px 0}a{color:inherit}</style><h1>Audit des sources — pas une admission</h1><p>Squelettes numériques source CMU, pas un avatar de remplacement ni une capture PARISFIT. Point rouge = hypothèse de vitesse faible, jamais contact mesuré. Sol non calibré.</p>'''
for name in ['native_m','filtered_only_m','resampled_channels60_m','historical_normalized60_m']:
 page+='<article><h2>'+name+'</h2><video controls playsinline preload="none" src="'+name+'.mp4"></video><details><summary>Images de diagnostic</summary>'+''.join('<a href="'+p.name+'"><img src="'+p.name+'" alt="Trois vues du squelette source"></a>' for p in sorted(root.glob(name+'-*.png')))+'</details></article>'
page+='<p><a href="benchmark.json">Rapports complets</a> · <a href="original-retrieval.json">Originals availability</a> · <a href="original-analysis.json">Original data screening</a> · <a href="originals/NOTICE.txt">Attributions and licenses</a></p>'
(root/'index.html').write_text(page)
# No new candidate exported; bind reused phase11 retarget evidence exactly.
manifest={'status':'REFUSÉ','newQualifiedReference':None,'retargetReports':{m:{'file':'docs/coach/phase11/'+m+'_report.json','sha256':hashlib.sha256(Path('docs/coach/phase11',m+'_report.json').read_bytes()).hexdigest(),'execution':json.loads(Path('docs/coach/phase11/evidence.json').read_text())['run']} for m in 'ABC'},'note':'existing A/B/C rerun independently by blender-control; filtering branch is NEVER fed to them'}
(root/'stage-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
