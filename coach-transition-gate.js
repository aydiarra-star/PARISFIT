// Fail-closed admission checks only. No unreviewed animation is loaded or played here.
export const TRANSITION_POLICY = Object.freeze({positionToleranceM:.015,orientationToleranceRad:.08,maxEntrySpeedMS:.03});
export const TRANSITION_ROUTES = Object.freeze([
 Object.freeze({id:'stand-to-crouch',from:'neutral-standing',to:'asymmetric-crouch',duration:4.5,speed:1,technicalStatus:'CONTACT_WINDOWS_PASS',joinStatus:'BLOCKED',enabled:false}),
 Object.freeze({id:'crouch-to-stand',from:'asymmetric-crouch',to:'neutral-standing',duration:4.5,speed:1,technicalStatus:'CONTACT_WINDOWS_PASS',joinStatus:'BLOCKED',enabled:false})
]);
const finiteVector=(x,n)=>Array.isArray(x)&&x.length===n&&x.every(Number.isFinite);
export function compareTransitionPose(actual,expected){
 if(!actual||!expected||Object.keys(expected).length<60)return {ok:false,reason:'missing-pose'};
 let maxPositionM=0,maxOrientationRad=0;
 for(const [name,e]of Object.entries(expected)){const a=actual[name];if(!a||![a,e].every(p=>finiteVector(p.position,3)&&finiteVector(p.quaternion,4)))return {ok:false,reason:'invalid-pose'};
  for(const p of [a,e])if(Math.abs(Math.hypot(...p.quaternion)-1)>.001)return {ok:false,reason:'invalid-quaternion'};
  maxPositionM=Math.max(maxPositionM,Math.hypot(...a.position.map((v,i)=>v-e.position[i])));
  const dot=Math.abs(a.quaternion.reduce((s,v,i)=>s+v*e.quaternion[i],0));maxOrientationRad=Math.max(maxOrientationRad,2*Math.acos(Math.min(1,dot)));
 }
 return {ok:maxPositionM<=TRANSITION_POLICY.positionToleranceM&&maxOrientationRad<=TRANSITION_POLICY.orientationToleranceRad,reason:'pose-comparison',maxPositionM,maxOrientationRad};
}
export function admitTransition({route,pose,contacts=[],speedMS,modelSHA256,clipSHA256,interrupted=false,reducedMotion=false}){
 const deny=reason=>({allowed:false,reason,fallback:'paused-demonstration-cut'});
 if(!route)return deny('no-route');
 if(interrupted||reducedMotion)return deny('interruption-or-reduced-motion');
 if(!route.enabled||route.technicalStatus!=='PASS'||route.joinStatus!=='PASS')return deny('route-not-approved');
 if(!route.modelSHA256||!route.clipSHA256||modelSHA256!==route.modelSHA256||clipSHA256!==route.clipSHA256)return deny('asset-version-mismatch');
 if(!Number.isFinite(route.duration)||route.duration<=0||route.speed!==1||!Number.isFinite(speedMS)||speedMS<0||speedMS>TRANSITION_POLICY.maxEntrySpeedMS)return deny('unstable-entry');
 if(!Array.isArray(route.requiredContacts)||!route.requiredContacts.length||route.requiredContacts.some(c=>!contacts.includes(c)))return deny('missing-support');
 if(!route.recovery||route.recovery.status!=='PASS'||!compareTransitionPose(route.recovery.pose,route.recovery.pose).ok)return deny('no-approved-recovery');
 if(!compareTransitionPose(route.exitPose,route.exitPose).ok)return deny('missing-exit-pose');
 const check=compareTransitionPose(pose,route.entryPose);if(!check.ok)return deny('entry-pose-mismatch');
 return {allowed:true,id:route.id,duration:route.duration,speed:route.speed,exitPose:route.exitPose};
}
export function findTransitionRoute(from,to){return TRANSITION_ROUTES.find(r=>r.from===from&&r.to===to)||null;}
