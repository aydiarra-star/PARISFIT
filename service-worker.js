const CACHE="parisfit-shell-v6";
const FILES=["./","./index.html","./styles.css?v=20261127-6","./app.js?v=20261127-6","./coach-3d.js?v=20261127-6","./demo-data.js?v=20261127-6","./assets/coach-welcome.jpg","./assets/workout.jpg","./vendor/three/three.module.js","./vendor/three/loaders/GLTFLoader.js","./vendor/three/utils/BufferGeometryUtils.js","./vendor/three/controls/OrbitControls.js","./assets/coach/previews/squat.jpg","./assets/coach/previews/pompes.jpg","./assets/coach/previews/gainage.jpg","./assets/coach/previews/fentes.jpg","./assets/coach/previews/jumpingjacks.jpg","./assets/coach/previews/mountainclimber.jpg","./assets/coach/previews/etirementdos.jpg","./assets/coach/previews/mobiliteepaules.jpg","./manifest.webmanifest","./assets/icon.svg"];

self.addEventListener("install",event=>{
  event.waitUntil(
    caches.open(CACHE)
      .then(cache=>cache.addAll(FILES))
      .then(()=>self.skipWaiting())
  );
});

self.addEventListener("activate",event=>{
  event.waitUntil(
    caches.keys()
      .then(keys=>Promise.all(keys.filter(key=>key.startsWith("parisfit-shell-")&&key!==CACHE).map(key=>caches.delete(key))))
      .then(()=>self.clients.claim())
  );
});

self.addEventListener("fetch",event=>{
  const request=event.request;
  if(request.method!=="GET")return;
  const url=new URL(request.url);
  if(url.origin!==self.location.origin)return;

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
