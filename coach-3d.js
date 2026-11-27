import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.169.0/build/three.module.js";

const host=document.getElementById("coach-stage-visual");
if(host){
 let renderer,scene,camera,rig,raf=0,active="squat",paused=false,profile=false,elapsed=0,last=0,resizeObserver;
 const mat=(color,roughness=.72)=>new THREE.MeshStandardMaterial({color,roughness});
 const skin=mat("#bd805d"),shirt=mat("#16845c"),shirtLight=mat("#35bd87"),shorts=mat("#183f33"),shoe=mat("#f1a05b"),dark=mat("#26342e"),eye=mat("#24342e",.35);
 const reduce=window.matchMedia("(prefers-reduced-motion: reduce)").matches;
 const status=document.createElement("div");status.className="coach-3d-status";status.textContent="COACH HUMAIN · 3D";host.append(status);
 const hint=document.createElement("div");hint.className="coach-3d-hint";hint.textContent="Animation articulée · vue interactive";host.append(hint);
 function capsule(parent,radius,length,material,x=0,y=0,z=0){
  const group=new THREE.Group();group.position.set(x,y,z);parent.add(group);
  const mesh=new THREE.Mesh(new THREE.CapsuleGeometry(radius,Math.max(.02,length-radius*2),5,10),material);
  mesh.position.y=-length/2;mesh.castShadow=true;mesh.receiveShadow=true;group.add(mesh);return group;
 }
 function sphere(parent,radius,material,x,y,z){const m=new THREE.Mesh(new THREE.SphereGeometry(radius,24,18),material);m.position.set(x,y,z);m.castShadow=true;parent.add(m);return m;}
 function buildRig(){
  const root=new THREE.Group();scene.add(root);
  const pelvis=sphere(root,.19,shorts,0,0,0);pelvis.scale.set(1.05,.72,.72);
  const torso=capsule(root,.205,.58,shirt,0,.37,0);
  const chest=sphere(root,.205,shirtLight,0,.57,.015);chest.scale.set(1,.46,.88);
  capsule(root,.065,.13,skin,0,.72,0);
  const head=sphere(root,.155,skin,0,.88,.015);head.scale.set(.9,1.08,.88);
  const hair=sphere(root,.157,dark,0,.965,-.005);hair.scale.set(.96,.55,.92);
  sphere(root,.018,eye,-.06,.9,.15);sphere(root,.018,eye,.06,.9,.15);
  sphere(root,.105,shirt,-.235,.59,0);sphere(root,.105,shirt,.235,.59,0);
  const armL=capsule(root,.073,.34,skin,-.29,.49,0),armR=capsule(root,.073,.34,skin,.29,.49,0);
  const elbowL=capsule(armL,.061,.30,skin,0,-.32,0),elbowR=capsule(armR,.061,.30,skin,0,-.32,0);
  sphere(elbowL,.067,skin,0,-.28,0);sphere(elbowR,.067,skin,0,-.28,0);
  const hipL=capsule(root,.09,.43,shorts,-.12,-.16,0),hipR=capsule(root,.09,.43,shorts,.12,-.16,0);
  const kneeL=capsule(hipL,.073,.39,skin,0,-.40,0),kneeR=capsule(hipR,.073,.39,skin,0,-.40,0);
  const footL=sphere(kneeL,.085,shoe,0,-.36,.075),footR=sphere(kneeR,.085,shoe,0,-.36,.075);
  footL.scale.set(1.35,.55,1.8);footR.scale.set(1.35,.55,1.8);
  return {root,torso,head,armL,armR,elbowL,elbowR,hipL,hipR,kneeL,kneeR};
 }
 function resetPose(){
  if(!rig)return;
  const {root,torso,head,armL,armR,elbowL,elbowR,hipL,hipR,kneeL,kneeR}=rig;
  root.rotation.set(0,0,0);root.position.set(0,1.05,0);torso.rotation.set(0,0,0);head.rotation.set(0,0,0);
  [armL,armR,elbowL,elbowR,hipL,hipR,kneeL,kneeR].forEach(g=>g.rotation.set(0,0,0));
  armL.rotation.z=-.12;armR.rotation.z=.12;hipL.rotation.z=.025;hipR.rotation.z=-.025;
 }
 function pose(t){
  if(!rig)return;resetPose();const p=(Math.sin(t*Math.PI*2)+1)/2;
  const {root,torso,head,armL,armR,elbowL,elbowR,hipL,hipR,kneeL,kneeR}=rig;
  if(active==="squat"){
   const bend=p*.72;root.position.y=1.05-p*.12;torso.rotation.x=-p*.10;
   hipL.rotation.x=bend*.42;hipR.rotation.x=bend*.42;kneeL.rotation.x=-bend*.9;kneeR.rotation.x=-bend*.9;
   armL.rotation.x=-.48;armR.rotation.x=-.48;armL.rotation.z=-.28;armR.rotation.z=.28;
  }else if(active==="pompes"||active==="gainage"||active==="mountainclimber"){
   root.rotation.z=Math.PI/2;root.position.set(0,.68,0);armL.rotation.z=-.95;armR.rotation.z=-.95;elbowL.rotation.z=-.3;elbowR.rotation.z=-.3;
   if(active==="pompes"){root.position.y=.68-p*.11;elbowL.rotation.x=p*.9;elbowR.rotation.x=p*.9;torso.rotation.x=p*.04;}
   if(active==="gainage"){root.position.y=.68+Math.sin(t*2)*.008;torso.rotation.x=.02;}
   if(active==="mountainclimber"){hipL.rotation.x=Math.sin(t*7)*.7;hipR.rotation.x=-Math.sin(t*7)*.7;kneeL.rotation.x=.8+Math.sin(t*7)*.35;kneeR.rotation.x=.8-Math.sin(t*7)*.35;}
  }else if(active==="fentes"){
   const l=p>.5?1:0;root.position.y=1.05-(.10+.08*Math.sin(t*2*Math.PI));
   hipL.rotation.x=l?.42:.02;hipR.rotation.x=l?-.12:.42;kneeL.rotation.x=l?-.8:-.08;kneeR.rotation.x=l?-.08:-.8;
   armL.rotation.x=-.2;armR.rotation.x=-.2;
  }else if(active==="jumpingjacks"){
   root.position.y=1.05+Math.abs(Math.sin(t*2*Math.PI))*.08;
   armL.rotation.z=-Math.sin(t*2*Math.PI)*1.12;armR.rotation.z=Math.sin(t*2*Math.PI)*1.12;
   hipL.rotation.z=-Math.sin(t*2*Math.PI)*.52;hipR.rotation.z=Math.sin(t*2*Math.PI)*.52;
  }else if(active==="etirementdos"){
   torso.rotation.x=-.22+Math.sin(t*1.3)*.10;head.rotation.x=.12;
   armL.rotation.z=-1.85+Math.sin(t*1.3)*.12;armR.rotation.z=1.85-Math.sin(t*1.3)*.12;
  }else if(active==="mobiliteepaules"){
   armL.rotation.z=-.55-Math.sin(t*2)*.6;armR.rotation.z=.55+Math.sin(t*2)*.6;
   armL.rotation.x=Math.sin(t*2)*.35;armR.rotation.x=-Math.sin(t*2)*.35;torso.rotation.y=Math.sin(t)*.12;
  }
 }
 function resize(){if(!renderer||!camera)return;const w=Math.max(1,host.clientWidth),h=Math.max(240,host.clientHeight);renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();}
 function loop(now){
  raf=requestAnimationFrame(loop);if(!renderer||!scene)return;
  if(!paused&&!reduce)elapsed+=(now-last)/1000;last=now;if(!paused)pose(reduce?0:elapsed);renderer.render(scene,camera);
 }
 function init(){
  try{
   scene=new THREE.Scene();scene.background=new THREE.Color("#edf5ef");
   camera=new THREE.PerspectiveCamera(34,1,.1,100);camera.position.set(0,1.45,5.4);camera.lookAt(0,1,0);
   renderer=new THREE.WebGLRenderer({antialias:true,alpha:false,powerPreference:"low-power"});
   renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,1.6));renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;
   renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.setClearColor("#edf5ef",1);
   renderer.domElement.setAttribute("aria-label","Coach sportif 3D animé");renderer.domElement.setAttribute("role","img");host.prepend(renderer.domElement);
   scene.add(new THREE.HemisphereLight("#ffffff","#a8c4ad",2));
   const key=new THREE.DirectionalLight("#ffffff",2.1);key.position.set(-3,5,4);key.castShadow=true;scene.add(key);
   const fill=new THREE.DirectionalLight("#f4bd8e",.7);fill.position.set(3,2,-2);scene.add(fill);
   const floor=new THREE.Mesh(new THREE.CircleGeometry(2.4,64),new THREE.MeshStandardMaterial({color:"#dcebe0",roughness:1}));
   floor.rotation.x=-Math.PI/2;floor.position.y=-.02;floor.receiveShadow=true;scene.add(floor);
   const ring=new THREE.Mesh(new THREE.TorusGeometry(1.15,.012,8,90),new THREE.MeshBasicMaterial({color:"#c1d9c8"}));ring.rotation.x=Math.PI/2;ring.position.y=.005;scene.add(ring);
   rig=buildRig();resize();resizeObserver=new ResizeObserver(resize);resizeObserver.observe(host);raf=requestAnimationFrame(loop);
  }catch(error){status.textContent="MODE DÉMO";hint.textContent="3D indisponible sur cet appareil";console.error("PARISFIT Coach 3D",error);}
 }
 function changeExercise(id){active=id||"squat";elapsed=0;last=performance.now();paused=false;const b=document.getElementById("coach-stage-toggle");if(b)b.textContent="Ⅱ Pause animation";if(rig)pose(0);}
 window.addEventListener("parisfit:coach-exercise",e=>changeExercise(e.detail?.id));
 document.getElementById("coach-stage-toggle")?.addEventListener("click",()=>{paused=!paused;});
 document.getElementById("coach-stage-view")?.addEventListener("click",e=>{profile=!profile;if(camera){camera.position.set(profile?4.7:0,1.35,profile?1.1:5.4);camera.lookAt(0,.95,0);}e.currentTarget.textContent=profile?"Vue de face":"Vue de profil";});
 document.addEventListener("visibilitychange",()=>{last=performance.now();});
 if(window.WebGLRenderingContext)init();else{status.textContent="MODE DÉMO";hint.textContent="WebGL non disponible";}
 window.addEventListener("resize",resize);
}
