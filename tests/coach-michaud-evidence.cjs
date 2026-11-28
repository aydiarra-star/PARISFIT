const fs=require('fs'),assert=require('assert/strict'),crypto=require('crypto'),D='docs/coach/phase13/',read=n=>JSON.parse(fs.readFileSync(D+n)),sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
for(const [n,h]of Object.entries(read('evidence.json').files))assert.equal(sha(D+n),h,n);
const r=read('reconstruction-report.json');assert.equal(r.status,'REFUSÉ');assert.equal(r.runtimeEnabled,false);assert.equal(r.Rocketbox.status,'NON TESTÉ');assert.equal(r.frames,150);for(const m of Object.values(r.models))assert.equal(m.status,'REFUSÉ');
const m=read('markers-report.json');assert.equal(m.frames,3350);assert.equal(m.markers.length,37);assert(m.markers.every(x=>x.kind==='skin marker, not joint centre'));
const p=read('model-probe.json');assert.equal(p.status,'VALIDÉ');assert.equal(p.subjectReconstruction,'NON TESTÉ');assert.equal(p.modelMarkers,66);assert.equal(p.dataMarkers,37);assert.deepEqual(p.exactNameMatches,[]);
for(const v of read('local-render-report.json').videos){assert.equal(v.frames,150);assert.equal(sha(D+'previews/'+v.file),v.sha256)}
const b=read('browser-report.json');assert.deepEqual(b.widths,[320,390,768,1200]);assert.equal(b.videos.length,3);assert(b.videos.every(v=>v.currentTime>.5&&!v.error));assert.equal(read('filter-sensitivity.json').usedInReconstruction,false);
assert.equal(sha('assets/coach/coach.glb'),'1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb');console.log('PASS phase13 evidence hashes, limited scope, rejected anatomy, model probe, video playback and unchanged runtime');
