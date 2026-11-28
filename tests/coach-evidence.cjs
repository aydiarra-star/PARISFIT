const assert=require('node:assert/strict'),fs=require('node:fs'),crypto=require('node:crypto');
const root='docs/coach/phase2/',sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const report=JSON.parse(fs.readFileSync(root+'video-report.json'));assert.equal(report.files.length,64);
for(const file of report.files){const b=fs.readFileSync(root+file.path);assert.equal(b.length,file.bytes);assert.equal(sha(b),file.sha256);assert.equal(b.toString('ascii',4,8),'ftyp');assert.equal(file.status,'PASS');assert(file.decodedFrames>30);}
const model=sha(fs.readFileSync('assets/coach/coach.glb'));
assert.equal(JSON.parse(fs.readFileSync(root+'after/capture-manifest.json')).modelSHA256,model);
assert.equal(JSON.parse(fs.readFileSync(root+'trajectory-report.json')).modelSHA256,model);
console.log('PASS: 64 evidence videos, checksums and current-model provenance');
