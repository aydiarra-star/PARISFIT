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
  function extendFingers(side,pitch=.10){
    const sign=side==='L'?1:-1;
    for(let finger=0;finger<5;finger++){
      const start=side+'_Finger'+finger,dir=v(finger===0?-sign*.60:0,pitch,finger===0?.8:1).normalize();
      aim(start,start+'1',pos(bone(start)).add(dir));
      aim(start+'1',start+'2',pos(bone(start+'1')).add(dir));
      const original=R(start+'2').point.clone().sub(R(start+'1').point).normalize();
      worldQ(start+'2',new T.Quaternion().setFromUnitVectors(original,dir).multiply(R(start+'2').world));
    }
  }
  const clips=[];const ids=['squat','pompes','gainage','fentes','jumpingjacks','mountainclimber','etirementdos','mobiliteepaules'];
  const durations=[5,5,6,10,3.2,4,8,6];
  const smooth=x=>{x=Math.max(0,Math.min(1,x));return x*x*x*(x*(x*6-15)+10)};
  const ramp=(u,a,b)=>smooth((u-a)/(b-a));
  const pulse=(u,a,b,c,d)=>ramp(u,a,b)*(1-ramp(u,c,d));
  // All significantly weighted support vertices are used to anchor the SKIN, not bone pivots.
  const contactVertices={};const meshes=[];
  model.traverse(o=>{if(o.isSkinnedMesh){meshes.push(o);const g=o.geometry,seen=new Set();for(let i=0;i<g.attributes.position.count;i++){
    let best=-1,name='';for(let k=0;k<4;k++){const w=g.attributes.skinWeight.getComponent(i,k);if(w>best){best=w;name=o.skeleton.bones[g.attributes.skinIndex.getComponent(i,k)]?.name||'';}}
    const m=name.match(/Bip01_([LR])_(Foot|Toe\d*|Hand|Finger\d*)/);if(!m)continue;
    const key=m[1]+'_'+(m[2].startsWith('Foot')||m[2].startsWith('Toe')?'Foot':'Hand');
    const identity=key+':'+[0,1,2].map(k=>g.attributes.position.getComponent(i,k).toFixed(5)).join(',');if(seen.has(identity))continue;seen.add(identity);
    (contactVertices[key]??=[]).push([o,i]);if(m[2]==='Hand')(contactVertices[m[1]+'_Palm']??=[]).push([o,i]);if(m[2].startsWith('Finger'))(contactVertices[m[1]+'_Digits']??=[]).push([o,i]);
  }}});
  function skinFloor(part){model.updateMatrixWorld(true);meshes.forEach(m=>m.skeleton.update());let min=Infinity;const point=v();for(const [m,i] of contactVertices[part]){m.getVertexPosition(i,point);point.applyMatrix4(m.matrixWorld);min=Math.min(min,point.y);}return min;}

  for(let ci=0;ci<ids.length;ci++){
    const id=ids[ci],duration=durations[ci],steps=Math.round(duration*30),times=[],tracks={};
    for(const n of Object.keys(bones))tracks[n]={p:[],q:[]};
    for(let frame=0;frame<=steps;frame++){
      reset();const u=frame/steps;
      let cycle=pulse(u,.10,.46,.56,.94);
      const floor=['pompes','gainage','mountainclimber'].includes(id);
      let height=.875,z=0,lean=0,spread=.15,handY=.94,handZ=.08;
      let stride=0,lungeBend=0,lungeHalf=u<.5?0:1,lungeLocal=(u*2)%1,flight=0,landing=0,spreadCycle=0;
      if(id==='squat'){height-=cycle*.235;z=-cycle*.16;lean=cycle*.28;handY=1.00+cycle*.16;handZ=.13+cycle*.30;}
      if(id==='fentes'){
        stride=pulse(lungeLocal,0,.18,.78,1);lungeBend=pulse(lungeLocal,.22,.44,.52,.76);
        height-=stride*.075+lungeBend*.18;z=-stride*.12;lean=.04;handY=1.04;handZ=.20;
      }
      if(id==='jumpingjacks'){
        const half=(u<.5||u>=1)?0:1,s=u>=1?0:(u*2)%1,air=ramp(s,.18,.76);
        spreadCycle=half===0?air:1-air;
        const at=(s-.18)/(.76-.18);flight=at>0&&at<1?.075*Math.sin(Math.PI*at)**2:0;
        landing=.035*(pulse(s,0,.09,.09,.18)+pulse(s,.76,.84,.84,.97));
        spread=.13+spreadCycle*.18;height=.86-spreadCycle*.055+flight-landing;
      }
      if(id==='etirementdos'){
        cycle=pulse(u,.08,.35,.65,.95);lean=.04+cycle*.10;height-=.015*cycle;z=-.025*cycle;
        handY=.96+cycle*.31;handZ=.12+cycle*.39;
      }
      if(floor){
        const slope=id==='pompes'?.23-cycle*.13:id==='gainage'?.070:.23;
        height=.218+.792*Math.sin(slope)+(id==='mountainclimber'?.03:0);z=-.96+.792*Math.cos(slope);lean=Math.PI/2-slope;
      }
      root(v(0,height,z),lean);
      // Separate pelvis/spine/neck orientations, no whole-character exercise shortcut.
      tilt('Pelvis',lean);tilt('Spine',lean);tilt('Spine1',lean+(id==='etirementdos'?cycle*.05:0));tilt('Spine2',lean+(id==='etirementdos'?cycle*.10:0)+(id==='gainage'?Math.sin(u*2*Math.PI)*.0015:0));tilt('Neck',floor?lean-.025:lean*.7);tilt('Head',floor?lean-.025:lean*.6);
      for(const side of ['L','R']){
        const sign=side==='L'?1:-1;
        let foot=v(sign*spread,.102,0),hand=v(sign*.28,handY,handZ),clearance=0,footPitch=0;
        let legPole=v(sign*spread,.45,1),armPole=v(sign*.47,1.1,-.10);
        if(id==='fentes'){
          const rear=side===(lungeHalf===0?'R':'L');
          if(rear){foot.z=-.50*stride;footPitch=.65*stride;
            if(lungeLocal<.18)clearance=.07*Math.sin(Math.PI*lungeLocal/.18)**2;
            if(lungeLocal>.78)clearance=.07*Math.sin(Math.PI*(lungeLocal-.78)/.22)**2;
          }
        }
        if(id==='jumpingjacks'){
          clearance=flight;const angle=.08+spreadCycle*2.85;
          hand=v(sign*(.22+.52*Math.sin(angle)),1.42-.52*Math.cos(angle),.035);
          armPole=v(sign*.8,1.4,.7);
        }
        if(id==='mobiliteepaules'){
          const a=u*2*Math.PI;hand=v(sign*.48,1.17+.14*Math.sin(a),.10+.14*Math.cos(a));armPole=v(sign*.85,1.15,-.50);
        }
        if(id==='etirementdos'){hand.x=sign*(.28-.09*cycle);armPole=v(sign*.40,1.18,.24);}
        if(floor){
          foot=v(sign*.117,.218,-.96);footPitch=.93;hand=v(sign*.27,.066,.44);
          legPole=v(sign*.12,-.2,-.3);armPole=v(sign*.46,.24,.10);
          if(id==='mountainclimber'){
            const local=(u*2+(side==='L'?0:1))%2;
            const wave=local<1?Math.sin(Math.PI*local)**2:0;
            foot.z+=wave*.55;clearance=wave*.06;legPole=v(sign*.33,.20,.70);
          }
          if(id==='gainage'){hand=v(sign*.20,.066,.68);armPole=v(sign*.20,-1,.28);}
        }
        ik(side+'_Thigh',side+'_Calf',side+'_Foot',foot,legPole);
        tilt(side+'_Foot',footPitch);
        for(let iteration=0;iteration<3;iteration++){
          foot.y+=.002+clearance-skinFloor(side+'_Foot');
          ik(side+'_Thigh',side+'_Calf',side+'_Foot',foot,legPole);tilt(side+'_Foot',footPitch);
        }
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
          const palmOrientation=rotation.multiply(R(side+'_Hand').world);
          worldQ(side+'_Hand',palmOrientation);
          extendFingers(side);
          for(let iteration=0;iteration<2;iteration++){
            hand.y+=.002-skinFloor(side+'_Palm');
            ik(side+'_UpperArm',side+'_Forearm',side+'_Hand',hand,armPole);worldQ(side+'_Hand',palmOrientation);
          }
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
