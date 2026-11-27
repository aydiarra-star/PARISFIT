const{chromium}=require('@playwright/test');
(async()=>{const b=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||undefined,args:['--no-sandbox']});try{const p=await b.newPage();await p.goto((process.env.BASE_URL||'http://localhost:3000')+'/docs/coach/phase3/professional-review.html');
// Portable PDF links: never export localhost URLs to an external reviewer.
await p.evaluate(()=>{for(const a of document.querySelectorAll('a[href]')){const u=new URL(a.href);a.href='https://github.com/aydiarra-star/PARISFIT/blob/arena/a03f64da-parisfit'+u.pathname;}});
await p.pdf({path:'docs/coach/phase3/professional-review.pdf',format:'A4',printBackground:true,margin:{top:'14mm',bottom:'14mm',left:'12mm',right:'12mm'}});}finally{await b.close()}})().catch(e=>{console.error(e);process.exitCode=1});
