// Explicit authorized runtime/publication changes, NOT a rewrite of historical evidence.
const fs=require('fs'),assert=require('node:assert/strict'),crypto=require('crypto');
const authorized=new Set(['.gitignore','.github/workflows/deploy-pages.yml','.github/workflows/validate.yml','app.js','coach-3d.js','index.html','package.json','service-worker.js','styles.css','tests/coach-passive-qualification.cjs','tests/coach-independent-review.cjs']);
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
exports.assertHistorical=(p,h)=>{if(!authorized.has(p))assert.equal(sha(p),h,'Historical protected file: '+p);};
if(require.main===module){const b=JSON.parse(fs.readFileSync('docs/coach/phase24/baseline.json'));let unchanged=0,changes=[];for(const [p,h]of Object.entries(b.files)){if(sha(p)===h)unchanged++;else{assert(authorized.has(p),'Unauthorized change: '+p);changes.push(p);}}console.log(JSON.stringify({reference:b.reference,unchanged,authorizedChanges:changes,priorEvidenceUnchanged:true},null,2));}
