const assert=require('node:assert/strict'),fs=require('node:fs'),crypto=require('node:crypto');
const data=fs.readFileSync('assets/coach/coach.glb');
assert.equal(data.toString('ascii',0,4),'glTF');assert.equal(data.readUInt32LE(4),2);assert.equal(data.readUInt32LE(8),data.length);
const size=data.readUInt32LE(12),doc=JSON.parse(data.subarray(20,20+size).toString());
const bin=data.subarray(28+size);assert.equal(doc.buffers.length,1);assert(!doc.buffers[0].uri);assert(doc.skins.length>0);assert(doc.skins[0].joints.length>=60);
const names=doc.nodes.map(n=>n.name);
for(const suffix of ['Spine','Spine1','Spine2','Neck','Head','L_Clavicle','R_Clavicle','L_Hand','R_Hand','L_Foot','R_Foot'])assert(names.includes('Bip01_'+suffix),suffix);
for(const side of ['L','R'])for(let f=0;f<5;f++)assert(names.includes(`Bip01_${side}_Finger${f}`));
assert.equal(doc.images.length,4);for(const image of doc.images){assert.equal(image.mimeType,'image/jpeg');const v=doc.bufferViews[image.bufferView];assert(v.byteLength>1000);assert.equal(bin[v.byteOffset],0xff);assert.equal(bin[v.byteOffset+1],0xd8);}
assert.equal(doc.animations.length,8);
function values(accessor){const a=doc.accessors[accessor],v=doc.bufferViews[a.bufferView];assert.equal(a.componentType,5126);return new Float32Array(bin.buffer.slice(bin.byteOffset+v.byteOffset+(a.byteOffset||0),bin.byteOffset+v.byteOffset+(a.byteOffset||0)+a.count*({SCALAR:1,VEC3:3,VEC4:4}[a.type])*4));}
for(const clip of doc.animations){const moving=new Set();for(const channel of clip.channels){const sampler=clip.samplers[channel.sampler],a=values(sampler.output);assert([...a].every(Number.isFinite));if(a.some((x,i)=>Math.abs(x-a[i%4])>.00001)&&channel.target.path==='rotation')moving.add(doc.nodes[channel.target.node].name);}
 assert(moving.size>=(clip.name==='mobiliteepaules'?4:8),clip.name+' must move a coordinated skeleton, not just the root');
 assert([...moving].some(n=>n.includes('Forearm')),clip.name);if(clip.name!=='mobiliteepaules')assert([...moving].some(n=>n.includes('Calf')),clip.name);
}
const hash=crypto.createHash('sha256').update(data).digest('hex');console.log(JSON.stringify({bytes:data.length,sha256:hash,joints:doc.skins[0].joints.length,textures:doc.images.length,clips:doc.animations.map(a=>a.name)},null,2));
