// Browser emulations only. These measurements do not establish iPhone/Android device performance.
const {chromium}=require('@playwright/test'),assert=require('node:assert/strict'),fs=require('node:fs');
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||undefined,args:['--no-sandbox','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const results={environment:'Headless Chromium + software WebGL, local server, mobile viewport emulation; no physical devices',physicalIPhone:false,physicalAndroid:false,thermal:null,gpuMemoryBytes:null,cases:[]};
 try{for(const width of [390,412]){
  const context=await browser.newContext({viewport:{width,height:844},deviceScaleFactor:3,isMobile:true,hasTouch:true,serviceWorkers:'block'});const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(process.env.BASE_URL||'http://localhost:3000');await page.locator('#workout-rec').click();const begin=Date.now();await page.locator('#coach-stage-visual').scrollIntoViewIfNeeded();await page.waitForFunction(()=>document.querySelector('#coach-stage-visual').dataset.state==='ready');
  const inspect=()=>page.evaluate(async()=>(await import('/coach-3d.js?v=20261127-9')).inspectCoach());const loadMs=Date.now()-begin;
  await page.locator('#coach-stage-reset').click();await page.locator('#coach-stage-toggle').click();await page.locator('#coach-stage-visual').scrollIntoViewIfNeeded();const first=await inspect();const t=Date.now();await page.waitForTimeout(3000);const second=await inspect();const seconds=(Date.now()-t)/1000;
  assert(second.time>first.time);await page.locator('#coach-stage-toggle').click();const stopped=await inspect();await page.waitForTimeout(250);assert.equal((await inspect()).render.frames,stopped.render.frames,'paused viewer must stop drawing');
  await page.locator('#coach-stage-toggle').click();await page.locator('.mobile-nav [data-view="nutrition"]').click();await page.waitForTimeout(200);const hidden=await inspect();await page.waitForTimeout(250);assert.equal((await inspect()).render.frames,hidden.render.frames,'offscreen viewer must stop drawing');
  await page.locator('.mobile-nav [data-view="today"]').click();await page.locator('#workout-rec').click();await page.locator('#coach-stage-visual').scrollIntoViewIfNeeded();await page.waitForTimeout(200);
  // Real WebGL context loss/restoration, not a mocked success flag.
  const canLose=await page.evaluate(()=>{window.lossExtension=document.querySelector('#coach-stage-visual canvas').getContext('webgl2').getExtension('WEBGL_lose_context');return !!window.lossExtension});
  if(canLose){await page.evaluate(()=>window.lossExtension.loseContext());await page.locator('.coach-retry').waitFor({state:'visible'});await page.evaluate(()=>window.lossExtension.restoreContext());await page.waitForFunction(()=>document.querySelector('#coach-stage-visual').dataset.state==='ready');}
  const cdp=await context.newCDPSession(page);const heap=await cdp.send('Runtime.getHeapUsage');
  assert.deepEqual(errors,[]);results.cases.push({width,dprRequested:3,dprUsed:second.render.pixelRatio,localLoadMs:loadMs,softwareRenderedFPS:+((second.render.frames-first.render.frames)/seconds).toFixed(1),rendererAllocations:second.render.memory,jsHeapUsedBytes:heap.usedSize,pausedRenderingStopped:true,offscreenRenderingStopped:true,contextRestored:canLose,errors});await context.close();
 }}finally{await browser.close()}
 fs.mkdirSync('docs/coach/phase2',{recursive:true});fs.writeFileSync('docs/coach/phase2/mobile-report.json',JSON.stringify(results,null,2)+'\n');console.log(JSON.stringify(results,null,2));
})().catch(e=>{console.error(e);process.exitCode=1});
