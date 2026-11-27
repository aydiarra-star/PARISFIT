/* Original Parisfit keyframe authoring. Not mocap; requires sports-professional review.
 * World-space two-bone IK preserves segment lengths and anchors support points.
 * This offline authoring module is NOT included in the application runtime.
 */
import * as T from '../vendor/three/three.module.js';
export function bakeExercises(model) {
  model.updateMatrixWorld(true);
  const bones={};model.traverse(o=>{if(o.isBone)bones[o.name]=o});
  const bone=n=>bones[n==='Root'?'Bip01':'Bip01_'+n];
  const v=(x=0,y=0,z=0)=>new T.Vector3(x,y,z);
  const pos=o=>o.getWorldPosition(v());
  const rest={};for(const [n,b] of Object.entries(bones))rest[n]={q:b.quaternion.clone(),p:b.position.clone(),world:b.getWorldQuaternion(new T.Quaternion()),point:pos(b)};
  const R=n=>rest[bone(n).name];
  const worldQ=(n,q)=>{const b=bone(n);b.quaternion.copy(b.parent.getWorldQuaternion(new T.Quaternion()).invert().multiply(q));b.updateWorldMatrix(false,true)};
  const axis=v(1,0,0);
  const tilt=(n,a)=>worldQ(n,new T.Quaternion().setFromAxisAngle(axis,a).multiply(R(n).world));
  function aim(n,child,target){const start=pos(bone(n)),a=R(child).point.clone().sub(R(n).point).normalize(),b=target.clone().sub(start).normalize();worldQ(n,new T.Quaternion().setFromUnitVectors(a,b).multiply(R(n).world));}
  function ik(a,b,c,target,pole){
    const start=pos(bone(a)),l1=R(a).point.distanceTo(R(b).point),l2=R(b).point.distanceTo(R(c).point);
    const delta=target.clone().sub(start),d=Math.max(.001,Math.min(delta.length(),l1+l2-.0001)),dir=delta.normalize();
    const bend=pole.clone().sub(start);bend.addScaledVector(dir,-bend.dot(dir)).normalize();
    const along=(l1*l1-l2*l2+d*d)/(2*d),height=Math.sqrt(Math.max(0,l1*l1-along*along));
    const joint=start.clone().addScaledVector(dir,along).addScaledVector(bend,height);
    aim(a,b,joint);aim(b,c,target);
  }
  function reset(){for(const [n,b] of Object.entries(bones)){b.position.copy(rest[n].p);b.quaternion.copy(rest[n].q)}model.updateMatrixWorld(true)}
  function root(p,angle){const b=bone('Root');b.position.copy(b.parent.worldToLocal(p.clone()));tilt('Root',angle);}
  const clips=[];const ids=['squat','pompes','gainage','fentes','jumpingjacks','mountainclimber','etirementdos','mobiliteepaules'];
  const durations=[4,4,6,6,2.4,3,8,6];
  for(let ci=0;ci<ids.length;ci++){
    const id=ids[ci],duration=durations[ci],steps=Math.round(duration*30),times=[],tracks={};
    for(const n of Object.keys(bones))tracks[n]={p:[],q:[]};
    for(let frame=0;frame<=steps;frame++){
      reset();const u=frame/steps,cycle=(1-Math.cos(u*2*Math.PI))/2,breathe=Math.sin(u*2*Math.PI)*.003;
      const floor=['pompes','gainage','mountainclimber'].includes(id);
      let height=.895,z=0,lean=0,spread=.15,handY=.94,handZ=.03;
      if(id==='squat'){height-=cycle*.26;z=-cycle*.18;lean=cycle*.30;handY=1.03+cycle*.15;handZ=.12+cycle*.30;}
      if(id==='fentes'){height-=cycle*.23;lean=.06;handY=1.04;handZ=.16;}
      if(id==='jumpingjacks'){height+=Math.sin(Math.PI*cycle)*.07;spread=.13+cycle*.22;handY=.94+cycle*1.02;handZ=.025;}
      if(id==='etirementdos'){lean=.14+cycle*.26;height-=cycle*.04;handY=1.63;handZ=.38+cycle*.08;}
      if(floor){const slope=id==='pompes'?.23-cycle*.16:id==='gainage'?.11:.23;height=.17+.795*Math.sin(slope)+breathe;z=-.96+.795*Math.cos(slope);lean=Math.PI/2-slope;}
      root(v(0,height,z),lean);
      // Separate pelvis/spine/neck orientations, no whole-character exercise shortcut.
      tilt('Pelvis',lean);tilt('Spine',lean);tilt('Spine1',lean+(id==='etirementdos'?cycle*.10:0));tilt('Spine2',lean+(id==='etirementdos'?cycle*.16:0));tilt('Neck',floor?lean-.10:lean*.5);tilt('Head',floor?lean-.12:lean*.25);
      for(const side of ['L','R']){
        const sign=side==='L'?1:-1;
        let foot=v(sign*spread,.102,0),hand=v(sign*.28,handY,handZ);
        let legPole=v(sign*.20,.45,1),armPole=v(sign*.60,1.1,-.18);
        if(id==='fentes'){foot.z=side==='L'?.30:-.39;foot.y=side==='R'?.13:.102;legPole.z=1;}
        if(id==='jumpingjacks'){hand.x=sign*(.28+Math.sin(cycle*Math.PI)*.48);armPole=v(sign*.8,1.5,.03);}
        if(id==='mobiliteepaules'){const a=u*2*Math.PI;hand=v(sign*(.32+.08*Math.sin(a)),1.40+.37*Math.sin(a),.34*Math.cos(a));armPole=v(sign*.65,1.5,.1);}
        if(id==='etirementdos'){hand.x=sign*.24;armPole=v(sign*.55,1.65,.35);}
        if(floor){
          foot=v(sign*.117,.17,-.96);hand=v(sign*.29,.075,.43);
          legPole=v(sign*.12,-.2,-.3);armPole=v(sign*.65,.30,.10);
          if(id==='mountainclimber'){
            const wave=Math.max(0,Math.sin(u*2*Math.PI+(side==='L'?0:Math.PI)));
            foot.z+=wave*.60;foot.y+=wave*.13;legPole=v(sign*.20,.03,.25);
          }
          if(id==='gainage'){hand=v(sign*.20,.085,.68);armPole=v(sign*.20,-1,.26);}
        }
        ik(side+'_Thigh',side+'_Calf',side+'_Foot',foot,legPole);
        tilt(side+'_Foot',floor?.93:(id==='fentes'&&side==='R'?.55:0));
        ik(side+'_UpperArm',side+'_Forearm',side+'_Hand',hand,armPole);
        // Wrist follows the forearm in standing exercises; palms face the floor in supports.
        if(floor){
          const forward=R(side+'_Finger2').point.clone().sub(R(side+'_Hand').point).normalize();
          const lateral=R(side+'_Finger1').point.clone().sub(R(side+'_Finger4').point);lateral.addScaledVector(forward,-lateral.dot(forward)).normalize();
          const normal=lateral.clone().cross(forward).normalize();
          const basis=new T.Matrix4().makeBasis(lateral,forward,normal);
          const targetForward=v(0,-.03,1).normalize(),targetLateral=v(-sign,0,0);
          const targetBasis=new T.Matrix4().makeBasis(targetLateral,targetForward,targetLateral.clone().cross(targetForward));
          const rotation=new T.Quaternion().setFromRotationMatrix(targetBasis.multiply(basis.invert()));
          worldQ(side+'_Hand',rotation.multiply(R(side+'_Hand').world));
        }else{
          const parent=bone(side+'_Forearm').getWorldQuaternion(new T.Quaternion());
          const relative=R(side+'_Forearm').world.clone().invert().multiply(R(side+'_Hand').world);
          worldQ(side+'_Hand',parent.multiply(relative));
        }
      }
      model.updateMatrixWorld(true);times.push(u*duration);
      for(const [n,b] of Object.entries(bones)){tracks[n].p.push(...b.position.toArray());tracks[n].q.push(...b.quaternion.toArray());}
    }
    const keyframes=[];
    for(const [n,t] of Object.entries(tracks)){
      keyframes.push(new T.QuaternionKeyframeTrack(n+'.quaternion',times,t.q));
      if(n==='Bip01')keyframes.push(new T.VectorKeyframeTrack(n+'.position',times,t.p));
    }
    clips.push(new T.AnimationClip(id,duration,keyframes).optimize());
  }
  reset();return clips;
}
