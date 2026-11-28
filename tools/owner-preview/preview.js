import * as T from '/vendor/three.module.js';
import {GLTFLoader} from '/vendor/loaders/GLTFLoader.js';
import {OrbitControls} from '/vendor/controls/OrbitControls.js';
const $=s=>document.querySelector(s), names={squat:'Squat',pompes:'Pompes',gainage:'Gainage',fentes:'Fentes',jumpingjacks:'Jumping jacks',mountainclimber:'Mountain climbers',etirementdos:'Étirement du dos',mobiliteepaules:'Mobilité des épaules'};
let active='squat',paused=true,action,mixer,clips,model;
const scene=new T.Scene();scene.background=new T.Color('#dce6df');
const camera=new T.PerspectiveCamera(34,1,.05,50);
const renderer=new T.WebGLRenderer({antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));$('#stage').append(renderer.domElement);
const orbit=new OrbitControls(camera,renderer.domElement);orbit.minDistance=2;orbit.maxDistance=7;orbit.enablePan=false;
scene.add(new T.HemisphereLight(0xffffff,0x739183,2));const light=new T.DirectionalLight(0xfff4e7,2.6);light.position.set(-2,4,3);scene.add(light);
const floor=new T.Mesh(new T.PlaneGeometry(10,10),new T.MeshStandardMaterial({color:0xc3d4c7}));floor.rotation.x=-Math.PI/2;scene.add(floor);
function view(i){const y=['pompes','gainage','mountainclimber'].includes(active)?.56:1.02;orbit.target.set(0,y,0);const r=Number($('#zoom').value);camera.position.set(...[[0,y+.26,r],[r,y+.26,0],[r*.707,y+.26,r*.707]][i]);orbit.update();}
function select(){active=$('#exercise').value;mixer.stopAllAction();action=mixer.clipAction(clips.find(c=>c.name===active));action.reset().play();mixer.update(0);paused=true;$('#play').textContent='Lecture';$('#time').value=0;view(0);}
new ResizeObserver(()=>{const el=$('#stage');renderer.setSize(el.clientWidth,el.clientHeight);camera.aspect=el.clientWidth/el.clientHeight;camera.updateProjectionMatrix();}).observe($('#stage'));
try{const gltf=await new GLTFLoader().loadAsync('/model.glb');model=gltf.scene;clips=gltf.animations;for(const id of Object.keys(names))if(!clips.some(c=>c.name===id))throw Error('Clip absent : '+id);model.traverse(o=>{if(o.isSkinnedMesh)o.frustumCulled=false;});scene.add(model);mixer=new T.AnimationMixer(model);for(const [id,label] of Object.entries(names))$('#exercise').add(new Option(label,id));for(const id of ['exercise','play','reset'])$('#'+id).disabled=false;select();$('#status').textContent='Modèle Rocketbox Sports_Male_04 · 8 clips originaux · non validés';}catch(e){$('#status').textContent='Échec du chargement : '+e.message;}
$('#exercise').onchange=select;$('#play').onclick=()=>{paused=!paused;$('#play').textContent=paused?'Lecture':'Pause';};$('#reset').onclick=()=>{action.reset().play();mixer.update(0);$('#time').value=0;};$('#time').oninput=()=>{if(action){action.time=Number($('#time').value)*action.getClip().duration;mixer.update(0);}};
document.querySelectorAll('[data-view]').forEach(b=>b.onclick=()=>view(Number(b.dataset.view)));
$('#zoom').oninput=()=>{camera.position.sub(orbit.target).setLength(Number($('#zoom').value)).add(orbit.target);orbit.update();};
document.addEventListener('visibilitychange',()=>{if(document.hidden){paused=true;$('#play').textContent='Lecture';}});
const clock=new T.Clock();renderer.setAnimationLoop(()=>{const dt=Math.min(clock.getDelta(),.1);if(action&&!paused){mixer.update(dt*Number($('#speed').value));$('#time').value=action.time/action.getClip().duration;}orbit.update();renderer.render(scene,camera);});
// Read-only diagnostics: tests verify actual bone movement, not merely a timer.
window.inspectPreview=()=>({active,paused,time:action?.time,clips:clips?.map(c=>c.name),bones:model?(()=>{model.updateMatrixWorld(true);const a=[];model.traverse(o=>{if(o.isBone)a.push(o.getWorldPosition(new T.Vector3()).toArray());});return a;})():[]});
const key='parisfit-owner-visual-reviews-v1';let reviews=[],valid=true;
try{const raw=localStorage.getItem(key);if(raw!==null){reviews=JSON.parse(raw);if(!Array.isArray(reviews)||reviews.some(r=>!r||typeof r.notes!=='string'||typeof r.exercise!=='string'||typeof r.at!=='string'))throw Error('format');}}catch{valid=false;$('#saved').textContent='Stockage inaccessible ou données illisibles : aucune donnée écrasée. Exportez avant effacement.';}
function render(){ $('#reviews').replaceChildren();if(valid)for(const r of reviews){const li=document.createElement('li');li.textContent=`${r.at} · ${names[r.exercise]||r.exercise} : ${r.notes}`;$('#reviews').append(li);}}render();
$('#feedback').onsubmit=e=>{e.preventDefault();if(!valid)return;const next=[...reviews,{exercise:active,at:new Date().toISOString(),notes:$('#notes').value,kind:'owner-visual-not-professional'}];try{localStorage.setItem(key,JSON.stringify(next));reviews=next;$('#notes').value='';$('#saved').textContent='Retour enregistré localement.';render();}catch{$('#saved').textContent='Échec de stockage : retour non enregistré, texte conservé.';}};
$('#export').onclick=()=>{try{const raw=localStorage.getItem(key)||'[]';const url=URL.createObjectURL(new Blob([raw],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download='parisfit-visual-reviews.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}catch{$('#saved').textContent='Export impossible : stockage inaccessible.';}};
$('#erase').onclick=()=>{if(!confirm('Effacer uniquement les retours de cette prévisualisation ?'))return;try{localStorage.removeItem(key);reviews=[];valid=true;render();$('#saved').textContent='Retours effacés.';}catch{$('#saved').textContent='Effacement impossible.';}};
