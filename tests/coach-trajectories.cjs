// Engineering regression checks, NOT biomechanical approval. Units: metres / seconds / degrees.
const assert=require('node:assert/strict'),fs=require('node:fs');const {chromium}=require('@playwright/test');
const base=process.env.BASE_URL||'http://localhost:3000',hz=60,baseline=process.env.COACH_AUDIT_BEFORE==='1';
const diff=(a,b)=>a.map((x,i)=>x-b[i]),len=a=>Math.hypot(...a),dist=(a,b)=>len(diff(a,b));
const flex=(a,b,c)=>{const u=diff(a,b),v=diff(c,b);return 180-Math.acos(Math.max(-1,Math.min(1,u.reduce((s,x,i)=>s+x*v[i],0)/(len(u)*len(v)))))*180/Math.PI};
const round=x=>+x.toFixed(5);
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||undefined,args:['--no-sandbox','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const report={modelSHA256:require('node:crypto').createHash('sha256').update(fs.readFileSync(baseline?'.cache/phase2/before.glb':'assets/coach/coach.glb')).digest('hex'),method:'60 Hz sampling of the actual GLB skin and skeleton; no medical/sports validation',tolerances:{groundPenetrationM:.004,plantedSupportGapM:.007,plantedStepM:.008,loopJointErrorM:.001,maxJointSpeedMS:4.5,kneeFlexMaxDeg:145,elbowFlexMaxDeg:155},clips:[],failures:[]};
 try{
  const page=await browser.newPage();await page.goto(base+'/tools/coach-lab.html'+(baseline?'?model=../.cache/phase2/before.glb':''));await page.waitForFunction(()=>window.ready);const clips=await page.evaluate(()=>lab.clips);
  for(const clip of clips){
   const samples=await page.evaluate(({clip,hz})=>{lab.select(clip.name);return Array.from({length:Math.round(clip.duration*hz)+1},(_,i)=>lab.sample(Math.min(clip.duration,i/hz)))},{clip,hz});
   fs.mkdirSync('.cache/phase2',{recursive:true});fs.writeFileSync(`.cache/phase2/${baseline?'before':'after'}-${clip.name}-samples.json`,JSON.stringify(samples));
   const first=samples[0],last=samples.at(-1),support={};let maxJointSpeed=0,loopError=0,hipDrift=0;const knee=[],elbow=[];let maxSupportStep=0;
   for(const name of Object.keys(first.support))support[name]={min:Math.min(...samples.map(x=>x.support[name])),max:Math.max(...samples.map(x=>x.support[name]))};
   for(const name of Object.keys(first.joints))loopError=Math.max(loopError,dist(first.joints[name],last.joints[name]));
   for(let i=0;i<samples.length;i++){
    const s=samples[i],j=s.joints;
    hipDrift=Math.max(hipDrift,dist(j.Bip01_Pelvis,first.joints.Bip01_Pelvis));
    for(const side of ['L','R']){
     knee.push(flex(j[`Bip01_${side}_Thigh`],j[`Bip01_${side}_Calf`],j[`Bip01_${side}_Foot`]));
     elbow.push(flex(j[`Bip01_${side}_UpperArm`],j[`Bip01_${side}_Forearm`],j[`Bip01_${side}_Hand`]));
     if(i){for(const part of ['Hand','Foot']){const key=side+'_'+part;if(s.support[key]<.004&&samples[i-1].support[key]<.004)maxSupportStep=Math.max(maxSupportStep,dist(j['Bip01_'+key],samples[i-1].joints['Bip01_'+key]));}}
    }
    if(i)for(const name of Object.keys(j))maxJointSpeed=Math.max(maxJointSpeed,dist(j[name],samples[i-1].joints[name])*hz);
   }
   const r={id:clip.name,samples:samples.length,duration:clip.duration,support:Object.fromEntries(Object.entries(support).map(([k,v])=>[k,{min:round(v.min),max:round(v.max)}])),loopErrorM:round(loopError),maxJointSpeedMS:round(maxJointSpeed),maxPlantedStepM:round(maxSupportStep),kneeFlexDeg:[round(Math.min(...knee)),round(Math.max(...knee))],elbowFlexDeg:[round(Math.min(...elbow)),round(Math.max(...elbow))],hipDriftM:round(hipDrift)};
   const check=(ok,message)=>{if(!ok)report.failures.push(clip.name+': '+message)};
   check(Object.values(support).every(x=>x.min>=-.004),'skin penetrates ground');check(loopError<.001,'loop discontinuity');check(maxJointSpeed<4.5,'joint trajectory spike');check(maxSupportStep<.008,'planted support drift');check(Math.max(...knee)<145,'knee flexion guardrail');check(Math.max(...elbow)<155,'elbow flexion guardrail');
   if(['squat','gainage','etirementdos','mobiliteepaules','pompes'].includes(clip.name))for(const side of ['L','R'])check(support[side+'_Foot'].max<.007,'foot loses ground contact');
   if(['pompes','gainage','mountainclimber'].includes(clip.name))for(const side of ['L','R']){check(support[side+'_Hand'].max<.007,'hand loses ground contact');check(support[side+'_Palm'].max<.007,'palm loses ground contact');}
   if(clip.name==='mountainclimber')check(hipDrift<.001,'climber pelvis oscillates');
   if(clip.name==='gainage'){check(hipDrift<.001,'pelvis oscillates');for(const side of ['L','R'])check(support[side+'_Forearm'].max<.007,'forearm loses support');}
   if(clip.name==='fentes'){
    const footZ=side=>samples.map(s=>s.joints[`Bip01_${side}_Foot`][2]);
    const l=footZ('L'),r=footZ('R'),mid=Math.floor(samples.length/2);
    check(Math.min(...r.slice(0,mid))<-.4&&Math.min(...l.slice(mid))<-.4,'missing left/right alternation');
    check(Math.min(...l.slice(0,mid))>-.05&&Math.min(...r.slice(mid))>-.05,'front foot is not anchored');
   }
   report.clips.push(r);
  }
  report.status=report.failures.length?'FAIL':'PASS';fs.mkdirSync('docs/coach/phase2',{recursive:true});fs.writeFileSync('docs/coach/phase2/'+(baseline?'before-trajectory-report.json':'trajectory-report.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report,null,2));if(!baseline)assert.deepEqual(report.failures,[]);
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
