const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)],KEY="parisfit.v1";
const defaults={habits:[],water:0,energy:null,journal:"",name:""};let data;try{data={...defaults,...JSON.parse(localStorage.getItem(KEY)||"{}")}}catch{data={...defaults}}
const save=()=>localStorage.setItem(KEY,JSON.stringify(data));
function toast(t){const e=$("#toast");e.textContent=t;e.classList.add("show");clearTimeout(toast.timer);toast.timer=setTimeout(()=>e.classList.remove("show"),2200)}
function view(n){$$(".view").forEach(x=>x.classList.toggle("active",x.id==="view-"+n));$$("[data-view]").forEach(x=>x.classList.toggle("active",x.dataset.view===n));window.scrollTo({top:0,behavior:"smooth"})}
$$("[data-view]").forEach(x=>x.addEventListener("click",()=>view(x.dataset.view)));
$("#date").textContent=new Intl.DateTimeFormat("fr-FR",{weekday:"long",day:"numeric",month:"long"}).format(new Date());
function dialog(html){$("#modal-content").innerHTML=html;$("#modal").showModal()}
$("#modal").addEventListener("click",e=>{if(e.target===$("#modal"))$("#modal").close()});
function energy(){dialog('<p class="eyebrow">MON RESSENTI</p><h2>Comment est ton énergie aujourd’hui ?</h2><p>Il n’y a pas de bonne ou de mauvaise réponse.</p><div class="choices"><button data-e="low">🌿<br>Douce</button><button data-e="medium">☁<br>Modérée</button><button data-e="high">☀<br>Bonne</button></div>');$$("[data-e]").forEach(b=>b.onclick=()=>{data.energy=b.dataset.e;save();render();$("#modal").close();toast("Ressenti enregistré.")})}
$$("[data-energy]").forEach(b=>b.onclick=energy);
function render(){const labels={low:["Énergie douce","Aujourd’hui, privilégie la récupération."],medium:["Énergie modérée","Un rythme adapté peut te convenir."],high:["Bonne énergie","Choisis une activité qui te fait plaisir."]};$("#energy").textContent=data.energy?labels[data.energy][0]:"À renseigner";$("#energy-note").textContent=data.energy?labels[data.energy][1]:"Comment te sens-tu aujourd’hui ?";$("#score").innerHTML=data.energy?"✓<small> noté</small>":"—<small>/100</small>";$("#score-note").textContent=data.energy?"Ressenti déclaré par toi, pas une mesure médicale.":"Complète ton ressenti pour démarrer";$("#water-count").textContent=data.water;$("#glasses").innerHTML=Array.from({length:8},(_,i)=>'<span class="glass '+(i<data.water?"filled":"")+'"></span>').join("");const ed=$("#energy-dots");if(ed){const n=data.energy==="low"?2:data.energy==="medium"?5:data.energy==="high"?8:0;ed.innerHTML=Array.from({length:8},(_,i)=>'<span class="edot '+(i<n?"filled":"")+'"></span>').join("");}const h=$("#habits");h.innerHTML=data.habits.length?data.habits.map(x=>'<div class="habit"><button data-check="'+x.id+'">'+(x.done?"✓":"○")+'</button><div><b>'+escape(x.title)+'</b><small>'+(x.frequency||"À mon rythme")+'</small></div><button class="delete" data-delete="'+x.id+'">×</button></div>').join(""):'<div class="empty"><b>Ton espace est prêt.</b><p>Ajoute une première habitude qui te ferait du bien.</p><button class="outline" id="empty-add">Créer une habitude</button></div>';if(data.name)$("#greeting").innerHTML="Bonjour "+escape(data.name)+" ! <i>✦</i>";const add=$("#empty-add");if(add)add.onclick=habitDialog}
function escape(s){return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}
function habitDialog(){dialog('<p class="eyebrow">NOUVELLE HABITUDE</p><h2>Un petit pas qui te fait du bien.</h2><div class="field"><label>Mon habitude</label><input id="habit-title" maxlength="70" placeholder="Ex. Lire quelques pages"></div><div class="field"><label>Mon rythme</label><select id="habit-frequency"><option>Chaque jour</option><option>Quelques fois par semaine</option><option>À mon rythme</option></select></div><button class="primary" id="habit-save">Ajouter cette habitude</button>');$("#habit-save").onclick=()=>{const title=$("#habit-title").value.trim();if(!title)return toast("Donne un nom à ton habitude.");data.habits.push({id:Date.now().toString(),title,frequency:$("#habit-frequency").value,done:false});save();render();$("#modal").close();toast("Habitude créée.")}}
$("#add-habit").onclick=habitDialog;
$("#habits").addEventListener("click",e=>{if(e.target.dataset.check){const h=data.habits.find(x=>x.id===e.target.dataset.check);h.done=!h.done;save();render()}if(e.target.dataset.delete){data.habits=data.habits.filter(x=>x.id!==e.target.dataset.delete);save();render()}});
$("#water-add").onclick=()=>{data.water=Math.min(8,data.water+1);save();render();toast("Verre ajouté.")};$("#water-reset").onclick=()=>{data.water=0;save();render()};
$("#meal-ideas").onclick=()=>dialog('<p class="eyebrow">IDÉES DE REPAS</p><h2>Composer simplement</h2><ul><li>Riz, légumes de saison et lentilles.</li><li>Omelette, salade et pain complet.</li><li>Poisson ou tofu, patate douce et légumes.</li><li>Yaourt nature, fruit et flocons d’avoine.</li></ul><p>Vérifie les allergènes et adapte les portions à tes besoins.</p>');
function breath(){dialog('<div style="text-align:center"><p class="eyebrow">PAUSE RESPIRATION</p><h2>Respire tranquillement</h2><div class="breath-orb" id="breath-label">INSPIRE</div><p>Inspire doucement, puis expire sans forcer. Arrête si tu ressens un inconfort.</p><button class="outline" id="breath-stop">Terminer</button></div>');let phase=false;clearInterval(breath.timer);breath.timer=setInterval(()=>{const el=$("#breath-label");if(!el){clearInterval(breath.timer);return}phase=!phase;el.textContent=phase?"INSPIRE":"EXPIRE"},4000);$("#breath-stop").onclick=()=>{$("#modal").close();clearInterval(breath.timer)}}
$("#breath").onclick=breath;$("#breath2").onclick=breath;
$("#journal").onclick=()=>{dialog('<p class="eyebrow">MON JOURNAL</p><h2>Qu’as-tu envie de déposer ici ?</h2><div class="field"><textarea id="journal-entry" rows="5" placeholder="Écris librement. Ce texte reste sur cet appareil.">'+escape(data.journal)+'</textarea></div><button class="primary" id="journal-save">Enregistrer</button>');$("#journal-save").onclick=()=>{data.journal=$("#journal-entry").value;save();$("#modal").close();toast("Journal enregistré sur cet appareil.")}};
$("#rest").onclick=()=>dialog('<div style="text-align:center"><div class="breath-orb">PAUSE</div><h2>Tu as le droit de ne rien faire.</h2><p>Profite d’une musique, d’un moment calme ou ferme simplement les yeux.</p></div>');
$("#sos").onclick=()=>dialog('<p class="eyebrow">SOS CRAQUAGE</p><h2>On fait une pause ensemble.</h2><p>Tu n’as rien raté. Pose les épaules, relâche la mâchoire. Tu peux prendre ton temps.</p><div class="actions"><button class="primary" id="sos-breath">Faire trois respirations</button><button class="outline" id="sos-kind">Me parler avec douceur</button></div>');
$("#modal-content").addEventListener("click",e=>{if(e.target.id==="sos-breath")breath();if(e.target.id==="sos-kind")dialog('<div style="text-align:center"><div class="breath-orb">TU FAIS DE TON MIEUX</div><h2>Et c’est déjà important.</h2><p>Tu peux choisir une petite action, appeler quelqu’un ou simplement te reposer. Rien ne presse.</p></div>')});
$("#workout").onclick=()=>{dialog('<p class="eyebrow">SÉANCE DÉCOUVERTE · 8 À 10 MIN</p><h2>Mobilité en douceur</h2><p>Cette fiche est une proposition de découverte, pas un programme médical. Va lentement et arrête si tu ressens une douleur.</p><ol><li>Respiration calme — 1 min.</li><li>Mobilisation douce des épaules — 2 min.</li><li>Mobilité du haut du dos sans forcer — 2 min.</li><li>Marche tranquille sur place ou repos — 2 min.</li><li>Retour au calme — 1 min.</li></ol><button class="primary" id="workout-done">J’ai terminé</button>');$("#workout-done").onclick=()=>{$("#modal").close();toast("Séance notée. Merci d’avoir pris ce temps.")}};
function settings(){dialog('<p class="eyebrow">MON ESPACE</p><h2>Préférences PARISFIT</h2><div class="field"><label>Comment veux-tu qu’on t’appelle ?</label><input id="name" maxlength="40" value="'+escape(data.name)+'" placeholder="Prénom facultatif"></div><p>Dans cette première version, tes données sont conservées localement dans ce navigateur, sans synchronisation.</p><div class="actions"><button class="primary" id="save-profile">Enregistrer</button><button class="outline" id="clear-data">Effacer mes données</button></div>')}
$("#settings").onclick=settings;$("#profile").onclick=settings;
$("#modal-content").addEventListener("click",e=>{if(e.target.id==="save-profile"){data.name=$("#name").value.trim();save();render();$("#modal").close();toast("Préférences enregistrées.")}if(e.target.id==="clear-data"&&confirm("Effacer les données PARISFIT sur cet appareil ?")){localStorage.removeItem(KEY);data={...defaults};render();$("#modal").close();toast("Données locales effacées.")}});
render();
/* ===== COACH IA PARISFIT — ajout premium, interface existante préservée ===== */
const coachExercises=[
{id:"squat",title:"Squat",cat:"renforcement",level:"Débutant",time:"12 répétitions",muscles:"Quadriceps, fessiers",desc:"Descends lentement les hanches comme pour t'asseoir, puis remonte. Garde le dos droit et le regard devant toi.",noMateriel:true,anim:"squat"},
{id:"pompes",title:"Pompes",cat:"renforcement",level:"Intermédiaire",time:"8 à 12 répétitions",muscles:"Pectoraux, triceps, épaules",desc:"Pose les mains au sol, baisse le corps jusqu'à ce que la poitrine effleure le sol, puis remonte en poussant.",noMateriel:true,anim:"pushup"},
{id:"gainage",title:"Gainage (plank)",cat:"renforcement",level:"Débutant",time:"30 à 60 secondes",muscles:"Abdos, gainage",desc:"Tiens la position sur les avant-bras et les pointes de pieds, corps bien gainé, sans creuser le dos ni lever les fesses.",noMateriel:true,anim:"plank"},
{id:"fentes",title:"Fentes",cat:"renforcement",level:"Débutant",time:"10 par jambe",muscles:"Quadriceps, fessiers",desc:"Fais un pas en avant, descends le genou arrière vers le sol sans le toucher, puis remonte. Dos droit.",noMateriel:true,anim:"lunge"},
{id:"jumpingjacks",title:"Jumping Jacks",cat:"cardio",level:"Débutant",time:"30 à 60 secondes",muscles:"Cardio, corps entier",desc:"Saute en écartant bras et jambes, puis ramène les pieds et les bras. Maintiens un rythme régulier.",noMateriel:true,anim:"jumpingjack"},
{id:"mountainclimber",title:"Mountain Climbers",cat:"cardio",level:"Intermédiaire",time:"30 secondes",muscles:"Cardio, abdos, épaules",desc:"En position de pompes, amène alternativement les genoux vers la poitrine rapidement, comme si tu courais au sol.",noMateriel:true,anim:"mountain"},
{id:"etirementdos",title:"Étirement du dos",cat:"etirement",level:"Débutant",time:"30 à 60 secondes",muscles:"Dos, lombaires",desc:"Assis ou debout, étire doucement les bras vers le haut, puis penche-toi en avant sans forcer, dos arrondi.",noMateriel:true,anim:"stretch"},
{id:"mobiliteepaules",title:"Mobilité épaules",cat:"mobilite",level:"Débutant",time:"1 à 2 minutes",muscles:"Épaules, haut du dos",desc:"Fais des cercles lents et amples avec les épaules, dans un sens puis dans l'autre.",noMateriel:true,anim:"shoulders"}
];
const coachAnim={squat:"coach-squat",pushup:"coach-pushup",plank:"coach-plank",lunge:"coach-lunge",jumpingjack:"coach-jumpingjack",mountainclimber:"coach-mountain",stretch:"coach-stretch",shoulders:"coach-shoulders"};
function coachInit(){
  if(!$("#view-coach"))return;
  if(data.name)$("#coach-greeting-text").innerHTML="Bonjour "+escape(data.name)+" ! <i>✦</i>";
  renderCoachStats();
  renderCoachExercises("all");
  $("#coach-start-session").onclick=coachStartSession;
  $("#coach-chat-send").onclick=coachChatSend;
  $("#coach-chat-input").addEventListener("keydown",e=>{if(e.key==="Enter")coachChatSend();});
  $("#coach-settings").onclick=settings;
  $$("[data-view='coach']").forEach(b=>b.addEventListener("click",renderCoachStats));
  $$("[data-q]").forEach(b=>b.onclick=()=>coachQuick(b.dataset.q));
  $$("[data-filter]").forEach(b=>b.onclick=function(){$$("[data-filter]").forEach(x=>x.classList.toggle("active",x===this));renderCoachExercises(this.dataset.filter);});
}
function renderCoachStats(){
  const labels={low:["Énergie douce","Privilégie la récupération aujourd'hui."],medium:["Énergie modérée","Un rythme adapté peut te convenir."],high:["Bonne énergie","Choisis une activité qui te fait plaisir."]};
  const el=$("#coach-score"),note=$("#coach-score-note"),energy=$("#coach-energy");
  if(data.energy){el.innerHTML="✓<small> noté</small>";note.textContent=labels[data.energy]?labels[data.energy][1]:"Ressenti déclaré par toi.";energy.textContent=labels[data.energy]?labels[data.energy][0]:"À renseigner";}
  else{el.innerHTML="—<small>/100</small>";note.textContent="Complète ton ressenti pour démarrer";energy.textContent="À renseigner";}
}
function renderCoachExercises(filter){
  const grid=$("#coach-exercises"),list=filter==="all"?coachExercises:coachExercises.filter(x=>x.cat===filter);
  grid.innerHTML=list.map(x=>`
    <article class="coach-exercise-card" data-ex="${x.id}">
      <div class="coach-exercise-demo"><div class="anim-part" style="animation:${coachAnim[x.anim]||"coach-pulse"} 2s ease-in-out infinite">▲</div></div>
      <h4>${escape(x.title)}</h4>
      <div class="ex-meta">${escape(x.level)} · ${escape(x.time)}</div>
      <p>${escape(x.desc)}</p>
      <div class="ex-foot">${escape(x.muscles)}${x.noMateriel?" · Sans matériel":""}</div>
    </article>
  `).join("");
  $$("[data-ex]").forEach(card=>{card.onclick=function(){coachOpenExercise(this.dataset.ex);}});
}
function coachOpenExercise(id){
  const x=coachExercises.find(e=>e.id===id);
  if(!x)return;
  dialog('<div style="max-width:420px"><p class="eyebrow">EXERCICE · '+escape(x.cat)+'</p><h2 style="margin:4px 0 6px">'+escape(x.title)+'</h2><div style="height:150px;border-radius:12px;border:1px solid #164533;background:#061b14;display:flex;align-items:center;justify-content:center;color:#64748b;font-size:11px;margin-bottom:10px">▶ Démonstration animée de l\'exercice</div><p style="font-size:11.5px;color:#cbd5e1;margin:0 0 10px">'+escape(x.desc)+'</p><div style="font-size:9px;color:#94a3b2;margin-bottom:6px"><b>Muscles :</b> '+escape(x.muscles)+' · <b>Niveau :</b> '+escape(x.level)+' · <b>Temps :</b> '+escape(x.time)+'</div><p style="font-size:10px;color:#94a3b2;margin:0 0 12px"><b>Précaution :</b> va à ton rythme et arrête-toi en cas de douleur. Ce contenu est indicatif, pas un avis médical.</p><button class="coach-primary" id="coach-ex-done">J’ai terminé</button></div>');
  $("#coach-ex-done").onclick=()=>{$("#modal").close();toast("Exercice noté. Bien joué !");};
}

$("#workout-rec").onclick=()=>view("coach");
function coachStartSession(){
  dialog('<div style="max-width:420px"><p class="eyebrow">SÉANCE — RENFORCEMENT &amp; CARDIO</p><h2 style="margin:4px 0 8px">20 min · Débutant</h2><p style="font-size:11px;color:#94a3b2;margin:0 0 12px">Ton coach te guide exercice par exercice. Va à ton rythme, repose-toi entre chaque mouvement.</p><div id="coach-session-list" style="display:flex;flex-direction:column;gap:8px"></div><p style="font-size:10px;color:#94a3b2;margin:8px 0 0">Indicatif : adapte ou saute tout exercice qui ne te convient pas.</p><button class="coach-primary" id="coach-session-done" style="margin-top:12px">J’ai terminé la séance</button></div>');
  const list=$("#coach-session-list");
  coachExercises.slice(0,5).forEach((x,i)=>{list.innerHTML+=`<div style="display:flex;gap:10px;align-items:center;font-size:11px;padding:6px 0;border-bottom:1px solid #164533"><div style="width:24px;height:24px;border-radius:6px;background:#10b981;color:#000;display:grid;place-items:center;font-weight:800">${i+1}</div><div><div style="color:#fff;font-weight:700">${escape(x.title)}</div><div style="color:#94a3b2;font-size:10px">${escape(x.time)} · ${escape(x.level)}</div></div></div>`;});
  $("#coach-session-done").onclick=()=>{$("#modal").close();toast("Séance terminée. Bravo pour ta régularité !");};
}
function coachChatSend(){
  const input=$("#coach-chat-input");const q=input.value.trim();if(!q)return;
  coachChatAdd(q,true);input.value="";
  setTimeout(()=>coachChatReply(q),500);
}
function coachChatAdd(text,me){
  const box=$("#coach-chat-box");const div=document.createElement("div");div.className="coach-message"+(me?" coach-message-me":" coach-message-coach");
  if(me){div.style.flexDirection="row-reverse";div.innerHTML='<div class="coach-message-bubble" style="background:#10b981;color:#000;border-bottom-right-radius:2px">'+escape(text)+'</div><div class="coach-message-avatar" style="background:#cbd5e1;color:#061b14">'+(data.name?data.name[0].toUpperCase():"A")+'</div>';}
  else{div.innerHTML='<div class="coach-message-avatar">🤖</div><div class="coach-message-bubble">'+escape(text)+'</div>';}
  box.appendChild(div);box.scrollTop=box.scrollHeight;
}
function coachChatReply(q){
  const lq=q.toLowerCase();
  let reply="Je suis là pour t'aider. Tu peux me demander une séance, un exercice ciblé ou un conseil selon ton énergie.";
  if(lq.match(/cardio|endurance|souffle/))reply="Je te suggère : Jumping Jacks 30 s, Mountain Climbers 30 s, puis 1 min de marche récupération. Répète 3 fois selon ton énergie. Hydrate-toi.";
  else if(lq.match(/renforcement|muscu|bras|pectoraux|fessiers|jambes/))reply="Essaie : Squat 12 reps, Pompes 8–12 reps, Gainage 30–60 s, Fentes 10 par jambe. Garde le dos droit et va à ton rythme.";
  else if(lq.match(/dos|lombaire/))reply="Privilégie l'étirement du dos et la mobilité épaules. Bouge lentement et ne force jamais sur une douleur.";
  else if(lq.match(/etir|soupl|récup|récupération|relax/))reply="Fais des étirements doux : dos, épaules, jambes. Respire calmement et reste dans chaque position 30–60 s.";
  else if(lq.match(/débutant|commencer|facile|reprendre/))reply="Commence par la séance « Renforcement & Cardio » 20 min niveau débutant, sans matériel. C'est idéal pour reprendre en douceur.";
  else if(lq.match(/énergie|fatigue|forme/))reply="Selon ton énergie déclarée, je te propose un rythme adapté : douce = récupération, modérée = séance légère, bonne = séance complète.";
  coachChatAdd(reply,false);
}
function coachQuick(q){
  const map={fullbody:"Je veux une séance Full Body 20 min",cardio:"Propose-moi un cardio débutant",dos:"Comment soulager le dos ?",etirement:"Une routine d'étirements"};
  coachChatAdd(map[q],true);coachChatReply(map[q]);
}
coachInit();
if("serviceWorker"in navigator&&location.protocol.startsWith("http"))addEventListener("load",()=>navigator.serviceWorker.register("./service-worker.js?v=20261127-2",{updateViaCache:"none"}).catch(()=>{}));