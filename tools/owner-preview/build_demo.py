"""Build a separate internal PARISFIT package; never alter public sources/artifact."""
from pathlib import Path
import shutil, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(ROOT/'tools/animation-lock/build_public.py')],check=True)
OUT=ROOT/'.cache/owner-demo'
shutil.rmtree(OUT,ignore_errors=True)
shutil.copytree(ROOT/'.cache/public',OUT)
def replace(text,old,new):
    if text.count(old)!=1: raise ValueError('Source contract changed: '+old[:80])
    return text.replace(old,new)
# Only this isolated derivative loads original animation resources.
s=(ROOT/'coach-3d.js').read_text()
s=replace(s,'return admission(registry,active,assetHash).allowed&&clips.some(c=>c.name===active);','return clips.some(c=>c.name===active);')
s=replace(s,"fetch('./assets/coach/coach-static.glb')","fetch('./assets/coach/coach-review.glb')")
s=replace(s,"if(gltf.animations.length)throw Error('Public static asset contains animations');","if(gltf.animations.length!==8)throw Error('Expected eight review clips');")
s=s.replace('Chargement du modèle humain statique…','Chargement du Coach humain · prévisualisation…').replace('Modèle humain Rocketbox statique — animation verrouillée','Coach humain animé — prévisualisation non validée').replace('status.textContent=LOCK_MESSAGE;enable(true);','status.textContent="Prévisualisation en cours — animation non encore validée professionnellement";enable(true);').replace("paused?'▶ Reprendre'","paused?'▶ Lecture'")
s=replace(s,'let registry=null,assetHash=null;','let registry=null,assetHash=null,reviewCandidate=null;')
s=replace(s,'model=gltf.scene;clips=gltf.animations;', "model=gltf.scene;clips=gltf.animations;reviewCandidate=THREE.AnimationClip.parse(await (await fetch('./motion-candidate.json')).json());")
s=replace(s,'const clip=clips.find(c=>c.name===id);', "const clip=(id==='mountainclimber'&&document.getElementById('review-variant')?.value==='candidate')?reviewCandidate:clips.find(c=>c.name===id);")
shutil.copyfile(ROOT/'tools/motion-review/mountainclimber-candidate.json',OUT/'motion-candidate.json')
(OUT/'coach-3d.js').write_text(s)
shutil.copyfile(ROOT/'assets/coach/coach.glb',OUT/'assets/coach/coach-review.glb')
# No offline worker may capture authenticated resources or outlive session access.
app=(ROOT/'app.js').read_text()
line=next(x for x in app.splitlines() if 'navigator.serviceWorker.register' in x)
app=replace(app,line,'')
app=app.replace('Instructions ouvertes. La démonstration animée reste verrouillée.','Prévisualisation non validée : utilise Lecture pour observer le mouvement.')
(OUT/'app.js').write_text(app)
(OUT/'service-worker.js').unlink()
legacy=(ROOT/'tools/owner-preview/index.html').read_text()
feedback=legacy[legacy.index('<section><h2>Votre évaluation'):legacy.index('</main>')]
html=(ROOT/'index.html').read_text()
# Owner preview adds faster playback choices without changing public Coach controls.
html=replace(html,'<option value="1" selected>× 1</option>','<option value="1" selected>× 1</option><option value="1.5">× 1,5</option><option value="1.75">× 1,75</option><option value="2">× 2</option>')
html=replace(html,'<div class="coach-stage-main">','<p role="note" class="review-warning">Prévisualisation en cours — animation non encore validée professionnellement. Revue visuelle uniquement, pas une consigne d’entraînement.</p><div class="coach-stage-main">')
html=replace(html,'<div class="coach-stage-main">','<label>Comparaison mountain climber uniquement <select id="review-variant"><option value="original">Original</option><option value="candidate">Candidat temporel — non validé</option></select></label><p>Le candidat conserve les poses et la durée. Pic d’accélération mesuré réduit, vitesse maximale légèrement augmentée. Aucune correction anatomique revendiquée. Les sept autres clips restent identiques.</p><div class="coach-stage-main">')
html=replace(html,'</body>','<script type="module" src="./review-feedback.js"></script></body>')
html=replace(html,'<div class="coach-stage-main">', '<label class="review-picker">Observer un mouvement <select id="review-exercise">'+''.join(f'<option value="{id}">{name}</option>' for id,name in [('squat','Squat'),('pompes','Pompes'),('gainage','Gainage'),('fentes','Fentes'),('jumpingjacks','Jumping jacks'),('mountainclimber','Mountain climbers'),('etirementdos','Étirement du dos'),('mobiliteepaules','Mobilité des épaules')])+'</select></label><div class="coach-stage-main">')
# Place feedback inside the real Coach view, before its closing section.
start=html.index('id="view-coach"');end=html.index('</section>',start)
html=html[:end]+'<div id="review-feedback">'+feedback+'</div>'+html[end:]
html=replace(html,'</head>','<style>.review-warning{padding:16px;background:#fff0c4;border-radius:12px}.review-picker,#review-feedback{display:block;margin:20px 0}#review-feedback textarea{width:100%;min-height:120px}#review-feedback button,#review-exercise{min-height:44px;max-width:100%;padding:10px}#reviews{overflow-wrap:anywhere}#review-feedback section{padding:16px;background:white;border-radius:16px}</style></head>')
(OUT/'index.html').write_text(html)
preview=(ROOT/'tools/owner-preview/preview.js').read_text()
names="{squat:'Squat',pompes:'Pompes',gainage:'Gainage',fentes:'Fentes',jumpingjacks:'Jumping jacks',mountainclimber:'Mountain climbers',etirementdos:'Étirement du dos',mobiliteepaules:'Mobilité des épaules'}"
js="const $=s=>document.querySelector(s),names="+names+";let active=window.parisfitCoachExercise||'squat';\n"
js+="window.addEventListener('parisfit:coach-exercise',e=>{active=e.detail.id;$('#review-exercise').value=active;});$('#review-exercise').onchange=e=>window.renderCoachStage(e.target.value);\n"
js+="$('#review-variant').onchange=()=>window.renderCoachStage(active);\n"
js+=preview[preview.index("const key='parisfit-owner-visual-reviews-v1'"):]
(OUT/'review-feedback.js').write_text(js)
print('Separate authenticated demo built:',OUT)
