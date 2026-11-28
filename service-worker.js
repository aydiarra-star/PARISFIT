const CACHE="parisfit-shell-v30";
const FILES=["./vendor/three/LICENSE.txt","./app-state.js?v=20261127-30","./animation-validation.js","./animation-validation-registry.json","./assets/coach/coach-static.glb","./","./index.html","./styles.css?v=20261127-30","./app.js?v=20261127-30","./coach-3d.js?v=20261127-30","./coach-content.js","./coach-transition-gate.js","./demo-data.js?v=20261127-30","./assets/coach-welcome.jpg","./assets/workout.jpg","./vendor/three/three.module.js","./vendor/three/loaders/GLTFLoader.js","./vendor/three/utils/BufferGeometryUtils.js","./vendor/three/controls/OrbitControls.js","./assets/coach/previews/squat.jpg","./assets/coach/previews/pompes.jpg","./assets/coach/previews/gainage.jpg","./assets/coach/previews/fentes.jpg","./assets/coach/previews/jumpingjacks.jpg","./assets/coach/previews/mountainclimber.jpg","./assets/coach/previews/etirementdos.jpg","./assets/coach/previews/mobiliteepaules.jpg","./manifest.webmanifest","./assets/icon.svg"];

self.addEventListener("install",event=>{
  event.waitUntil(
    caches.open(CACHE)
      .then(cache=>cache.addAll(FILES))
      .then(()=>self.skipWaiting())
  );
});

self.addEventListener("activate",event=>{
  let migrating=false;
  event.waitUntil(
    caches.keys()
      .then(keys=>{const old=keys.filter(key=>key.startsWith("parisfit-shell-")&&key!==CACHE);migrating=old.length>0;return Promise.all(old.map(key=>caches.delete(key)));})
      .then(()=>self.clients.claim())
      .then(()=>migrating?self.clients.matchAll({type:'window'}):[])
      // Do not await navigations inside activation: their fetch can wait for activation.
      .then(clients=>{for(const client of clients)client.navigate(client.url).catch(()=>{});})
  );
});

self.addEventListener("fetch",event=>{
  const request=event.request;
  if(request.method!=="GET")return;
  // Browser video range requests must not be stored as partial Cache API responses.

  const url=new URL(request.url);
  if(url.origin!==self.location.origin)return;

  let path;try{path=decodeURIComponent(url.pathname);}catch{event.respondWith(Promise.resolve(new Response('Malformed URL',{status:400})));return;}
  if(path.includes('/tools/')||path.includes('/docs/')||path.endsWith('/assets/coach/coach.glb')||path.includes('/assets/coach/transitions/')){event.respondWith(Promise.resolve(new Response('Resource not published',{status:404})));return;}

  if(request.headers.has("range"))return;

  if(request.mode==="navigate"){
    event.respondWith(
      fetch(new Request(request,{cache:"no-store"}))
        .then(response=>{
          if(response.ok){
            const copy=response.clone();
            caches.open(CACHE).then(cache=>cache.put("./index.html",copy));
          }
          return response;
        })
        .catch(()=>caches.match("./index.html"))
    );
    return;
  }

  event.respondWith(
    caches.match(request).then(cached=>cached||fetch(request).then(async response=>{
      if(response.ok){const cache=await caches.open(CACHE);await cache.put(request,response.clone());}
      return response;
    }))
  );
});
