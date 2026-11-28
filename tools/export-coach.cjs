const {chromium}=require('@playwright/test');
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||undefined,args:['--no-sandbox']});
 try{
  const context=await browser.newContext({acceptDownloads:true,serviceWorkers:'block'});const page=await context.newPage();page.on('pageerror',console.error);
  await page.goto((process.env.BASE_URL||'http://localhost:3000')+'/tools/convert-coach.html');
  await page.waitForFunction(()=>window.ready||window.failure,{},{timeout:180000});
  const failure=await page.evaluate(()=>window.failure);if(failure)throw Error(failure);
  const download=page.waitForEvent('download');await page.evaluate(()=>{const a=document.createElement('a');a.href=window.assetURL;a.download='coach.glb';a.click()});
  await (await download).saveAs('assets/coach/coach.glb');console.log('GLB exported',await page.evaluate(()=>window.assetBytes));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
