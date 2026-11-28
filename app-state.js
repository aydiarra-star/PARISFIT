// Local-only data boundary. Never overwrite malformed persisted data implicitly.
(function(root){
 const KEY='parisfit.v1';
 const fresh=()=>({habits:[],water:0,energy:null,journal:'',name:''});
 function decode(raw){
  if(raw===null)return {data:fresh(),issue:null};
  try{
   const x=JSON.parse(raw);if(!x||typeof x!=='object'||Array.isArray(x))throw Error('shape');
   const d={...fresh(),...x};
   if(!Array.isArray(d.habits)||!Number.isInteger(d.water)||d.water<0||d.water>8||![null,'low','medium','high'].includes(d.energy)||typeof d.name!=='string'||typeof d.journal!=='string')throw Error('values');
   const ids=new Set();
   for(const h of d.habits){if(!h||typeof h.id!=='string'||typeof h.title!=='string'||typeof h.done!=='boolean'||(h.frequency!==undefined&&typeof h.frequency!=='string')||ids.has(h.id))throw Error('habit');ids.add(h.id);}
   return {data:d,issue:null};
  }catch{return {data:fresh(),issue:'invalid-data'};}
 }
 function load(storage){try{return decode(storage.getItem(KEY));}catch{return {data:fresh(),issue:'storage-unavailable'};}}
 function persist(storage,data){try{storage.setItem(KEY,JSON.stringify(data));return true;}catch{return false;}}
 function clear(storage){try{storage.removeItem(KEY);return true;}catch{return false;}}
 function recordEnergy(data,value,now=new Date()){
  if(!['low','medium','high'].includes(value)||!Number.isFinite(now.getTime()))throw new TypeError('Invalid energy record');
  return {...data,energy:value,energyRecordedAt:now.toISOString()};
 }
 function energyNote(data,now=new Date()){
  if(!data.energy)return 'Aucun ressenti enregistré';
  const raw=data.energyRecordedAt;
  if(typeof raw!=='string'||!Number.isFinite(Date.parse(raw)))return 'Ressenti enregistré · date inconnue';
  const when=new Date(raw);
  if(when.getTime()>now.getTime()+300000)return 'Ressenti enregistré · date à vérifier';
  const sameDay=when.getFullYear()===now.getFullYear()&&when.getMonth()===now.getMonth()&&when.getDate()===now.getDate();
  return sameDay?'Ressenti saisi aujourd’hui · autoévaluation':'Ressenti du '+when.toLocaleDateString('fr-FR')+' · à actualiser';
 }
 const api={KEY,fresh,decode,load,persist,clear,recordEnergy,energyNote};
 if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.PARISFIT_STATE=Object.freeze(api);
})(globalThis);
