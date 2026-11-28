// No localStorage/query/admin override. Registry and evidence are release-controlled.
export const LOCK_MESSAGE='La démonstration animée de cet exercice est temporairement indisponible dans l’attente d’une validation biomécanique professionnelle.';
export function admission(registry, clipId, actualFileSHA256){
 const deny=reason=>Object.freeze({allowed:false,reason});
 if(!registry||registry.schemaVersion!==1||!Array.isArray(registry.clips))return deny('registry-unavailable');
 const records=registry.clips?.filter(x=>x&&x.clipId===clipId);
 if(!records||records.length!==1)return deny('unknown-or-duplicate-clip');
 const r=records[0];
 if(r.status!=='validée')return deny('professional-validation-missing');
 if(!/^[a-f0-9]{64}$/.test(actualFileSHA256||'')||r.fileSHA256!==actualFileSHA256||registry.assetSHA256!==actualFileSHA256)return deny('asset-version-mismatch');
 if(!r.fileVersion||!r.reviewer?.identity||!r.reviewer?.qualification||!/^\d{4}-\d{2}-\d{2}$/.test(r.validationDate||'')||!r.report?.reference||!r.report?.sha256?.match(/^[a-f0-9]{64}$/)||!r.scope||!r.conditions?.length||!r.limits?.length)return deny('incomplete-professional-evidence');
 return Object.freeze({allowed:true,reason:'versioned-professional-record'});
}
export async function readRegistry(){
 try{const response=await fetch('./animation-validation-registry.json',{cache:'no-store'});if(!response.ok)throw Error('registry');return freeze(await response.json());}catch{return null;}
}
function freeze(value){if(value&&typeof value==='object'){Object.values(value).forEach(freeze);Object.freeze(value);}return value;}
export async function sha256(bytes){return [...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(x=>x.toString(16).padStart(2,'0')).join('');}
