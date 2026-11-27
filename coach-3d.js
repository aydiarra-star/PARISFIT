import * as THREE from './vendor/three/three.module.js';
import {GLTFLoader} from './vendor/three/loaders/GLTFLoader.js';
import {COACH_CONTENT} from './coach-content.js';
import {OrbitControls} from './vendor/three/controls/OrbitControls.js';

// One renderer, one skinned model, eight baked clips. No procedural body geometry.
const host=document.getElementById('coach-stage-visual');
const $=id=>document.getElementById(id);
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const controls=['coach-stage-toggle','coach-stage-view','coach-stage-reset','coach-stage-step','coach-stage-speed','coach-stage-zoom','coach-stage-timeline'];
let scene,renderer,camera,orbit,model,mixer,action,clips=[],raf=0,last=0,loading=false,ready=false,visible=false,disposed=false;
let paused=reduced.matches,speed=1,active=window.parisfitCoachExercise||'squat',viewIndex=0,stepIndex=0;
let observer,resizeObserver,requestToken=0,lastPhaseKey="";
const views=[{name:'Face',x:0,z:5.1},{name:'Profil',x:5.1,z:0},{name:'Trois-quarts',x:3.6,z:3.6}];
const floorExercises=new Set(['pompes','gainage','mountainclimber']);
const status=document.createElement('p');status.className='coach-model-status';status.setAttribute('role','status');
const retry=document.createElement('button');retry.type='button';retry.className='outline coach-retry';retry.textContent='Réessayer le chargement';retry.hidden=true;
if(host){host.append(status,retry);status.textContent='Le modèle 3D se chargera à l’ouverture du Coach.';}
function enable(value){controls.forEach(id=>{if($(id))$(id).disabled=!value});}
function updateUI(){
 $('coach-stage-toggle').textContent=paused?'▶ Reprendre':'Ⅱ Pause';
 $('coach-stage-toggle').setAttribute('aria-pressed',String(!paused));
 host.dataset.paused=String(paused);host.dataset.state=ready?'ready':loading?'loading':'unavailable';host.dataset.exercise=active;
}
function error(message){ready=false;loading=false;host.setAttribute('aria-busy','false');status.textContent=message;retry.hidden=false;enable(false);updateUI();}
function disposeScene(){
 cancelAnimationFrame(raf);raf=0;orbit?.dispose();resizeObserver?.disconnect();
 if(mixer&&model){mixer.stopAllAction();mixer.uncacheRoot(model);}
 const textures=new Set(),materials=new Set(),geometries=new Set();
 scene?.traverse(o=>{if(o.geometry)geometries.add(o.geometry);if(o.material)(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>{materials.add(m);Object.values(m).forEach(t=>{if(t?.isTexture)textures.add(t)})});if(o.isSkinnedMesh)o.skeleton.dispose();});
 textures.forEach(t=>t.dispose());materials.forEach(m=>m.dispose());geometries.forEach(g=>g.dispose());
 renderer?.dispose();renderer?.domElement.remove();renderer=null;scene=null;model=null;mixer=null;action=null;
}
function resize(){if(!renderer)return;const w=Math.max(host.clientWidth,1),h=Math.max(host.clientHeight,320);renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();draw();}
function draw(){if(renderer&&scene)renderer.render(scene,camera);}
function cameraView(index){if(!camera)return;viewIndex=index%views.length;const v=views[viewIndex],target=floorExercises.has(active)?.55:.98;const distance=Number($('coach-stage-zoom').value);camera.position.set(v.x*distance,target+.28,v.z*distance);orbit.target.set(0,target,0);orbit.update();$('coach-stage-view').textContent='Vue : '+v.name;host.dataset.camera=v.name;draw();}
function updateGuidance(){
 const guide=COACH_CONTENT[active];if(!guide)return;
 const fraction=action?action.time/action.getClip().duration:0;
 const phase=guide.phases.filter(p=>p.at<=fraction+1e-6).at(-1)||guide.phases[0];
 const key=active+':'+phase.at;if(key===lastPhaseKey)return;lastPhaseKey=key;
 $('coach-stage-phase').textContent=phase.label+' · '+phase.cue;
 $('coach-phase-label').textContent=phase.label;$('coach-phase-cue').textContent=phase.cue;
 host.dataset.phase=String(phase.at);
}
function select(id){
 if(!COACH_CONTENT[id])return;
 const changed=active!==id&&!!action;active=id;stepIndex=0;lastPhaseKey='';
 const guide=COACH_CONTENT[id];$('coach-stage-desc').textContent=guide.summary;
 for(const key of ['setup','error','correction','caution','accessible'])$('coach-'+key).textContent=guide[key];
 if(!ready){updateGuidance();return;}
 const clip=clips.find(c=>c.name===id);if(!clip){error('Animation indisponible. Les consignes écrites restent accessibles.');return;}
 // Do not morph a standing skeleton through the floor into a support pose.
 // Until reviewed transfer clips exist, use an explicit demonstration cut, not a fake transition.
 mixer.stopAllAction();action=mixer.clipAction(clip);action.reset().setEffectiveTimeScale(1).setEffectiveWeight(1).play();
 if(changed){paused=true;host.classList.remove('coach-view-cut');void host.offsetWidth;host.classList.add('coach-view-cut');host.dataset.transition='demonstration-cut';status.textContent='Nouvelle position · mise en place non animée. Lis les repères, puis reprends.';}
 mixer.update(0);$('coach-stage-timeline').value=0;cameraView(viewIndex);updateUI();updateGuidance();draw();schedule();
}
function tick(now){
 raf=0;if(!visible||document.hidden||!ready||disposed)return;
 const dt=Math.min((now-last)/1000,.05);last=now;
 if(!paused){mixer.update(dt*speed);$('coach-stage-timeline').value=action.time/action.getClip().duration;}
 host.dataset.time=action.time.toFixed(3);updateGuidance();orbit.update();draw();if(!paused)raf=requestAnimationFrame(tick);
}
function schedule(){cancelAnimationFrame(raf);last=performance.now();if(visible&&!document.hidden&&ready&&!paused)raf=requestAnimationFrame(tick);}
async function load(){
 if(loading||disposed)return;disposeScene();const token=++requestToken;loading=true;ready=false;retry.hidden=true;enable(false);updateUI();host.setAttribute('aria-busy','true');status.textContent='Chargement du modèle humain et des huit animations…';
 try{
  const low=matchMedia('(max-width: 600px)').matches||(navigator.deviceMemory&&navigator.deviceMemory<=4);
  renderer=new THREE.WebGLRenderer({antialias:!low,powerPreference:'low-power'});
  renderer.setPixelRatio(Math.min(devicePixelRatio,low?1.25:1.75));renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.12;
  renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;
  renderer.domElement.setAttribute('role','img');renderer.domElement.setAttribute('aria-label','Modèle humain Rocketbox articulé — démonstration expérimentale');renderer.domElement.tabIndex=0;host.prepend(renderer.domElement);
  renderer.domElement.addEventListener('webglcontextrestored',()=>{if(!loading&&!disposed)load();});
  renderer.domElement.addEventListener('webglcontextlost',e=>{e.preventDefault();cancelAnimationFrame(raf);error('Affichage 3D interrompu. Réessaie ou consulte les consignes écrites.');});
  scene=new THREE.Scene();scene.background=new THREE.Color('#edf5ef');
  camera=new THREE.PerspectiveCamera(34,1,.05,30);orbit=new OrbitControls(camera,renderer.domElement);orbit.enablePan=false;orbit.minDistance=2;orbit.maxDistance=6;orbit.minPolarAngle=.35;orbit.maxPolarAngle=1.8;orbit.enableDamping=false;orbit.addEventListener('change',draw);
  scene.add(new THREE.HemisphereLight(0xffffff,0x739183,2));
  const key=new THREE.DirectionalLight(0xfff4e7,2.6);key.position.set(-2,4,3);key.castShadow=true;key.shadow.mapSize.set(low?512:1024,low?512:1024);key.shadow.camera.left=-2;key.shadow.camera.right=2;key.shadow.camera.top=3;key.shadow.camera.bottom=-2;key.shadow.normalBias=.004;scene.add(key);
  const fill=new THREE.DirectionalLight(0xc8e5ee,1);fill.position.set(2,2,-2);scene.add(fill);
  // Geometric primitives are used ONLY for the environment, never the human.
  const floor=new THREE.Mesh(new THREE.PlaneGeometry(8,8),new THREE.MeshStandardMaterial({color:0xe0eae2,roughness:1}));floor.rotation.x=-Math.PI/2;floor.position.y=0;floor.receiveShadow=true;scene.add(floor);
  const gltf=await new GLTFLoader().loadAsync('./assets/coach/coach.glb',e=>{if(e.total)status.textContent='Modèle humain · '+Math.round(e.loaded/e.total*100)+' %';});
  if(token!==requestToken||disposed)return;
  model=gltf.scene;clips=gltf.animations;
  let bones=0,meshes=0;model.traverse(o=>{if(o.isBone)bones++;if(o.isSkinnedMesh){meshes++;o.castShadow=true;o.frustumCulled=false;}});
  if(!meshes||bones<60||clips.length!==8)throw Error('Asset incomplet');
  scene.add(model);mixer=new THREE.AnimationMixer(model);ready=true;loading=false;host.setAttribute('aria-busy','false');host.dataset.bones=bones;host.dataset.clips=clips.length;host.dataset.quality=low?'mobile':'standard';
  status.textContent='Modèle humain 3D · animations expérimentales, non validées';enable(true);select(active);resizeObserver=new ResizeObserver(resize);resizeObserver.observe(host);resize();schedule();
 }catch(e){disposeScene();error('La 3D ne peut pas être chargée. Les exercices et leurs consignes restent disponibles.');console.warn('PARISFIT Coach:',e.message);}
}
if(host){
 enable(false);updateUI();select(active);retry.onclick=load;
 $('coach-stage-toggle').onclick=()=>{paused=!paused;if(!paused)status.textContent='Démonstration expérimentale · avis professionnel requis';updateUI();updateGuidance();schedule();};
 $('coach-stage-view').onclick=()=>cameraView(viewIndex+1);
 $('coach-stage-speed').onchange=e=>{speed=Number(e.target.value);};
 $('coach-stage-zoom').oninput=()=>cameraView(viewIndex);
 function seek(fraction){if(!action)return;mixer.stopAllAction();action.reset().play();action.time=action.getClip().duration*Math.min(.99999,Math.max(0,fraction));mixer.update(0);host.dataset.time=action.time.toFixed(3);lastPhaseKey='';updateGuidance();draw();}
 $('coach-stage-reset').onclick=()=>{paused=true;stepIndex=0;seek(0);$('coach-stage-timeline').value=0;updateUI();};
 $('coach-stage-step').onclick=()=>{paused=true;const phases=COACH_CONTENT[active].phases;const f=action.time/action.getClip().duration;const next=phases.findIndex(p=>p.at>f+.001);stepIndex=next<0?0:next;seek(phases[stepIndex].at);$('coach-stage-timeline').value=phases[stepIndex].at;updateUI();};
 $('coach-stage-timeline').oninput=e=>{paused=true;seek(Number(e.target.value));updateUI();};
 window.addEventListener('parisfit:coach-exercise',e=>select(e.detail.id));
 observer=new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;if(visible&&!ready&&!loading&&retry.hidden)load();schedule();},{threshold:0});observer.observe(host);
 document.addEventListener('visibilitychange',schedule);
 reduced.addEventListener('change',e=>{if(e.matches){paused=true;updateUI();}});
 window.addEventListener('pagehide',e=>{cancelAnimationFrame(raf);if(!e.persisted){disposed=true;requestToken++;observer.disconnect();disposeScene();}});
 window.addEventListener('pageshow',schedule);
}

// Read-only diagnostics for reproducible tests; never exposes mutable Three.js objects.
export function inspectCoach(){
 const joints={},textures=new Set();let skinnedMeshes=0,vertices=0;
 model?.traverse(o=>{if(o.isBone)joints[o.name]={position:o.getWorldPosition(new THREE.Vector3()).toArray(),quaternion:o.quaternion.toArray()};if(o.isSkinnedMesh){skinnedMeshes++;vertices+=o.geometry.attributes.position.count;(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>{if(m.map)textures.add(m.map);if(m.normalMap)textures.add(m.normalMap);});}});
 return {ready,active,paused,speed,time:action?.time||0,duration:action?.getClip().duration||0,clips:clips.map(c=>c.name),skinnedMeshes,vertices,textures:textures.size,joints,render:renderer?{frames:renderer.info.render.frame,memory:{...renderer.info.memory},calls:renderer.info.render.calls,triangles:renderer.info.render.triangles,pixelRatio:renderer.getPixelRatio()}:null};
}
