const assert=require('node:assert/strict'),fs=require('node:fs');const {chromium}=require('@playwright/test');
const base=process.env.BASE_URL||'http://localhost:3000';
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||undefined,args:['--no-sandbox','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const results=[];fs.mkdirSync('.cache/coach-review',{recursive:true});
 try{
  const context=await browser.newContext({viewport:{width:1200,height:1000}});const page=await context.newPage();const errors=[],missing=[],external=[],requestFailures=[];
  page.on('console',m=>{if(m.type()==='warning'||m.type()==='error')console.error('BROWSER',m.text())});page.on('requestfailed',r=>{if(r.failure()?.errorText!=='net::ERR_ABORTED')requestFailures.push(r.url())});page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.status()>=400)missing.push(r.url())});page.on('request',r=>{if(!r.url().startsWith(base)&&!r.url().startsWith('blob:'))external.push(r.url())});
  await page.goto(base);assert.equal(await page.locator('canvas').count(),0,'No GPU context on the home page');
  await page.locator('#workout-rec').click();await page.locator('#coach-stage-visual').scrollIntoViewIfNeeded();
  await page.waitForFunction(()=>document.querySelector('#coach-stage-visual').dataset.state==='ready',{},{timeout:60000});
  const inspect=()=>page.evaluate(async()=> (await import('/coach-3d.js?v=20261127-8')).inspectCoach());
  const initial=await inspect();assert.equal(initial.clips.length,8);assert(initial.skinnedMeshes>0);assert.equal(initial.textures,4);assert(Object.keys(initial.joints).length>=60);
  await page.evaluate(()=>window.originalCanvas=document.querySelector('canvas'));
  for(const id of initial.clips){
    await page.evaluate(id=>window.renderCoachStage(id),id);await page.locator('#coach-stage-reset').click();const first=await inspect();
    await page.locator('#coach-stage-timeline').fill(id==='fentes'?'0.22':'0.25');const middle=await inspect();assert(middle.time>0);assert.equal(await page.locator('#coach-stage-phase').textContent(),(await page.locator('#coach-phase-label').textContent())+' · '+(await page.locator('#coach-phase-cue').textContent()));assert.notDeepEqual(first.joints,middle.joints,id+' skeletal motion');await page.locator('#coach-stage-timeline').fill('0.5');
    for(let view=0;view<3;view++){
      await page.locator('#coach-stage-visual').screenshot({path:`.cache/coach-review/${id}-${view}.png`});await page.locator('#coach-stage-view').click();
    }
    assert(await page.evaluate(()=>document.querySelector('canvas')===window.originalCanvas));results.push({exercise:id,loaded:true,views:3});
  }
  await page.locator('#coach-stage-reset').click();await page.locator('#coach-stage-step').click();assert((await inspect()).paused);assert((await inspect()).time>0);
  await page.evaluate(()=>window.renderCoachStage('fentes'));await page.locator('#coach-stage-timeline').fill('0.62');assert.match(await page.locator('#coach-stage-phase').textContent(),/droite/);await page.evaluate(()=>window.renderCoachStage('mobiliteepaules'));assert((await inspect()).paused,'exercise cut must pause for setup');await page.locator('#coach-stage-step').click();await page.locator('#coach-stage-speed').selectOption('0.25');assert.equal((await inspect()).speed,.25);
  await page.locator('#coach-stage-toggle').click();await page.waitForFunction(()=>Number(document.querySelector('#coach-stage-visual').dataset.time)>2.1);await page.locator('#coach-stage-toggle').click();const stopped=(await inspect()).time;
  await page.locator('#coach-stage-view').click();assert.equal((await inspect()).time,stopped);assert((await inspect()).paused);
  await page.locator('#coach-stage-zoom').fill('0.85');
  for(const width of [320,390,430,768,1200]){
    await page.setViewportSize({width,height:900});await page.locator('#coach-stage-visual').scrollIntoViewIfNeeded();assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));const box=await page.locator('canvas').boundingBox();assert(box.width>100&&box.width<width);await page.locator('.coach-stage').screenshot({path:`.cache/coach-review/mobile-${width}.png`});
  }
  await page.evaluate(()=>navigator.serviceWorker.ready);await page.reload();await page.locator('#workout-rec').click();await page.locator('#coach-stage-visual').scrollIntoViewIfNeeded();await page.waitForFunction(()=>document.querySelector('#coach-stage-visual').dataset.state==='ready');
  await page.waitForFunction(async()=>!!(await caches.match(new URL('./assets/coach/coach.glb',location.href).href)));
  await context.setOffline(true);await page.reload();await page.locator('#workout-rec').click();await page.locator('#coach-stage-visual').scrollIntoViewIfNeeded();await page.waitForFunction(()=>document.querySelector('#coach-stage-visual').dataset.state==='ready');assert.equal((await inspect()).clips.length,8);
  assert.deepEqual(errors,[]);assert.deepEqual(missing,[]);assert.deepEqual(external,[]);assert.deepEqual(requestFailures,[]);await context.close();
  // Failed media request must not remove the rest of the app; retry must work.
  const fail=await browser.newContext({serviceWorkers:'block'});const p=await fail.newPage();await p.route('**/assets/coach/coach.glb',r=>r.abort());await p.goto(base);await p.locator('#workout-rec').click();await p.locator('#coach-stage-visual').scrollIntoViewIfNeeded();await p.locator('.coach-retry').waitFor({state:'visible'});await p.unroute('**/assets/coach/coach.glb');await p.locator('.coach-retry').click();await p.waitForFunction(()=>document.querySelector('#coach-stage-visual').dataset.state==='ready');await fail.close();
  const reduced=await browser.newContext({reducedMotion:'reduce',viewport:{width:390,height:844}});const r=await reduced.newPage();await r.goto(base);await r.locator('#workout-rec').click();await r.locator('#coach-stage-visual').scrollIntoViewIfNeeded();await r.waitForFunction(()=>document.querySelector('#coach-stage-visual').dataset.state==='ready');assert.equal(await r.locator('#coach-stage-visual').getAttribute('data-paused'),'true');await reduced.close();
  console.log(JSON.stringify({status:'PASS',results,widths:[320,390,430,768,1200],offline:true,retry:true,reducedMotion:true,errors,missing,external},null,2));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
