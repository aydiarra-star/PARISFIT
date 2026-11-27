"""Decode all review videos; build local artifact review page and compact inventory."""
import json,subprocess,hashlib,html
from pathlib import Path
root=Path('.cache/phase11');rows=[]
for method in ['A','B','C']:
 for view in ['face','profil','trois-quarts','slow','supports','skeleton','overlay']:
  p=root/(method+'-'+view+'.mp4');r=subprocess.run(['ffmpeg','-v','error','-i',str(p),'-progress','pipe:1','-f','null','-'],capture_output=True,text=True,check=True);assert not r.stderr.strip();fields=dict(x.split('=',1) for x in r.stdout.splitlines() if '=' in x);frames=int(fields['frame']);duration=int(fields['out_time_us'])/1e6;assert frames>=59 and duration>=(4.7 if view=='slow' else 2.4);rows.append({'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'frames':frames,'seconds':duration})
(root/'video-report.json').write_text(json.dumps({'status':'VALIDÉ','scope':'complete decoding, NOT visual review','videos':rows})+'\n')
rig=json.loads((root/'A/anatomy.json').read_text())
# Full original matrices stay in A/anatomy.json. Compact named axes and normalized
# rest quaternion export sufficient for public inspectable 111-bone table.
compact={'units':'m','up':'Z','sourceBVHScale':rig['sourceBVHScale'],'sourceAxes':rig['sourceAxes'],'mapping':rig['mapping']}
for side in ['source','target']:
 compact[side]={'objectMatrix':rig[side]['objectMatrix'],'objectScale':rig[side]['objectScale'],'bones':[{k:v for k,v in b.items() if k not in ['restMatrixLocal','parentRelativeRest']} for b in rig[side]['bones']]}
(root/'anatomy-summary.json').write_text(json.dumps(compact,separators=(',',':'))+'\n')
page='''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PARISFIT — Phase11 diagnostics</title><style>body{font:16px/1.6 system-ui;background:#edf5ef;color:#164b39;max-width:1200px;margin:auto;padding:20px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}video{width:100%}article{padding:16px;background:white}a{color:inherit}select{padding:12px}</style><h1>Trois expériences, aucune admission</h1><p>CMU autorisé, pas une capture PARISFIT. Source rouge en superposition ; cible Rocketbox conservée. Alignement source fixe, pas de recalage par image. Les vues squelettiques sont des diagnostics, pas un remplacement d’avatar.</p><select id="view">'''+''.join('<option>'+v+'</option>' for v in ['face','profil','trois-quarts','slow','supports','skeleton','overlay'])+'''</select><div class="grid">'''+''.join('<article><h2>'+m+'</h2><video controls playsinline preload="none" data-method="'+m+'"></video><a href="'+m+'/report.json">Mesures</a> · <a href="'+m+'/diagnostic.glb">GLB diagnostic refusé</a> · <a href="'+m+'/anatomy.json">Inventaire complet</a></article>' for m in ['A','B','C'])+'''</div><p>Lire les licences et notices dans chaque dossier A/B/C. Aucun avis professionnel. Aucun candidat d’intégration.</p><script>function load(){document.querySelectorAll('video').forEach(v=>{v.pause();v.src=v.dataset.method+'-'+document.getElementById('view').value+'.mp4'})}document.getElementById('view').onchange=load;load()</script></html>'''
(root/'index.html').write_text(page)
