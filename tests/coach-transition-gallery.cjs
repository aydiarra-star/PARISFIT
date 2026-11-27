const {chromium}=require('@playwright/test'),assert=require('node:assert/strict');
(async()=>{const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||undefined,args:['--no-sandbox']});try{
 const page=await browser.newPage();const base=process.env.BASE_URL||'http://localhost:3000';const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(base);await page.evaluate(()=>navigator.serviceWorker.ready);await page.goto(base+'/docs/coach/phase3/index.html');let decoded=0;
 for(const id of ['stand-to-crouch','crouch-to-stand'])for(const view of ['face','profil','trois-quarts','slow']){
  await page.locator('#exercise').selectOption(id);await page.locator('#angle').selectOption(view);
  await page.evaluate(()=>{for(const v of document.querySelectorAll('video')){v.preload='auto';v.muted=true;v.load();}});
  await page.waitForFunction(()=>[...document.querySelectorAll('video')].every(v=>v.readyState>=2||v.error));
  const states=await page.evaluate(()=>[...document.querySelectorAll('video')].map(v=>({error:v.error?.message,width:v.videoWidth,height:v.videoHeight,duration:v.duration})));
  for(const state of states){assert(!state.error,state.error);assert.equal(state.width,400);assert.equal(state.height,512);assert(state.duration>2);decoded++;}
 }
 await page.locator('#angle').selectOption('profil');await page.evaluate(async()=>{const v=document.getElementById('after');v.muted=true;await v.play();});await page.waitForFunction(()=>document.getElementById('after').currentTime>.2);await page.locator('#restart').click();assert(await page.locator('#after').evaluate(v=>v.paused&&v.currentTime===0));assert.deepEqual(errors,[]);console.log(`PASS: ${decoded} browser-decoded MP4 files, playback and gallery reset (service worker active)`);
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
