const assert=require('node:assert/strict'),S=require('../app-state.js');
const a=S.fresh();a.habits.push({id:'a',title:'Test',done:false});assert.equal(S.fresh().habits.length,0);
for(const raw of ['{','null','[]','{"water":-1}','{"water":"1"}','{"habits":null}','{"energy":"invented"}','{"habits":[{}]}'])assert.equal(S.decode(raw).issue,'invalid-data',raw);
const real={habits:[{id:'x',title:'Lire',done:true,frequency:'Chaque jour'}],water:3,energy:'low',journal:'Mon texte',name:'Moi',unknownFutureField:{keep:true}};assert.deepEqual(S.decode(JSON.stringify(real)).data,real);assert.equal(S.decode('{}').issue,null);
const storage={getItem:()=>JSON.stringify(real),setItem:(k,v)=>{storage.value=v},removeItem:()=>{storage.value=null}};assert.deepEqual(S.load(storage).data,real);assert(S.persist(storage,real));assert.deepEqual(JSON.parse(storage.value),real);assert(S.clear(storage));assert.equal(storage.value,null);
const denied={getItem(){throw Error('denied')},setItem(){throw Error('quota')},removeItem(){throw Error('denied')}};assert.equal(S.load(denied).issue,'storage-unavailable');assert.equal(S.persist(denied,real),false);assert.equal(S.clear(denied),false);
console.log('PASS: independent defaults, invalid data fail-closed, no silent overwrite, valid/unknown fields preserved, denied storage, reset');
