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
function render(){
 const sample=PARISFIT_DEMO.dashboard;
 const labels={low:["Douce","Un peu de récupération fait du bien."],medium:["Modérée","Avance à ton rythme."],high:["Pleine","Ton ressenti, enregistré sur cet appareil."]};
 const feeling=labels[data.energy];
 $("#energy").textContent=feeling?feeling[0]:sample.energy;
 $("#energy-note").textContent=feeling?feeling[1]:"Exemple · évalue ton énergie";
 $("#score").innerHTML=sample.score+'<small>/100</small>';
 $(".score-ring-progress").style.setProperty("--pct",sample.score);
 $("#score-note").textContent="Démonstration · score non mesuré";
 $("#vitality-delta").textContent=sample.delta;
 $("#vitality-streak").textContent=sample.streak+" jours d’affilée";
 $("#water-count").textContent=data.water;
 $("#glasses").innerHTML=Array.from({length:8},(_,i)=>'<span class="glass '+(i<data.water?"filled":"")+'"></span>').join("");
 $("#water-progress").value=data.water;
 $("#water-percent").textContent=Math.round(data.water/8*100)+"%";
 $("#water-desc").textContent=data.water>=8?"Objectif atteint · bravo !":"Encore "+((8-data.water)*0.25).toLocaleString("fr-FR")+" L · "+data.water+"/8 verres";
 const n=feeling?({low:2,medium:4,high:6}[data.energy]):6;
 $("#energy-dots").innerHTML=Array.from({length:6},(_,i)=>'<span class="edot '+(i<n?"filled":"")+'"></span>').join("");
 $("#greeting").textContent="Bonjour"+(data.name?", "+data.name:" ")+" 👋";
 const h=$("#habits");h.innerHTML=data.habits.length?data.habits.map(x=>'<div class="habit"><button data-check="'+x.id+'">'+(x.done?"✓":"○")+'</button><div><b>'+escape(x.title)+'</b><small>'+(x.frequency||"À mon rythme")+'</small></div><button class="delete" data-delete="'+x.id+'">×</button></div>').join(""):'<div class="empty"><b>Ton espace est prêt.</b><p>Ajoute une première habitude qui te ferait du bien.</p><button class="outline" id="empty-add">Créer une habitude</button></div>';const add=$("#empty-add");if(add)add.onclick=habitDialog}
function escape(s){return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}
function habitDialog(){dialog('<p class="eyebrow">NOUVELLE HABITUDE</p><h2>Un petit pas qui te fait du bien.</h2><div class="field"><label>Mon habitude</label><input id="habit-title" maxlength="70" placeholder="Ex. Lire quelques pages"></div><div class="field"><label>Mon rythme</label><select id="habit-frequency"><option>Chaque jour</option><option>Quelques fois par semaine</option><option>À mon rythme</option></select></div><button class="primary" id="habit-save">Ajouter cette habitude</button>');$("#habit-save").onclick=()=>{const title=$("#habit-title").value.trim();if(!title)return toast("Donne un nom à ton habitude.");data.habits.push({id:Date.now().toString(),title,frequency:$("#habit-frequency").value,done:false});save();render();$("#modal").close();toast("Habitude créée.")}}
$("#add-habit").onclick=habitDialog;
$("#habits").addEventListener("click",e=>{if(e.target.dataset.check){const h=data.habits.find(x=>x.id===e.target.dataset.check);h.done=!h.done;save();render()}if(e.target.dataset.delete){data.habits=data.habits.filter(x=>x.id!==e.target.dataset.delete);save();render()}});
$("#water-add").onclick=()=>{data.water=Math.min(8,data.water+1);save();render();toast("Verre ajouté.")};$("#water-reset").onclick=()=>{data.water=0;save();render()};
$("#meal-ideas").onclick=()=>dialog('<p class="eyebrow">IDÉES DE REPAS</p><h2>Composer simplement</h2><ul>'+PARISFIT_DEMO.meals.map(t=>'<li>'+escape(t)+'</li>').join('')+'</ul><p>Vérifie les allergènes et adapte les portions à tes besoins.</p>');
function breath(){dialog('<div style="text-align:center"><p class="eyebrow">PAUSE RESPIRATION</p><h2>Respire tranquillement</h2><div class="breath-orb" id="breath-label">INSPIRE</div><p>Inspire doucement, puis expire sans forcer. Arrête si tu ressens un inconfort.</p><button class="outline" id="breath-stop">Terminer</button></div>');let phase=false;clearInterval(breath.timer);breath.timer=setInterval(()=>{const el=$("#breath-label");if(!el){clearInterval(breath.timer);return}phase=!phase;el.textContent=phase?"INSPIRE":"EXPIRE"},4000);$("#breath-stop").onclick=()=>{$("#modal").close();clearInterval(breath.timer)}}
$("#breath").onclick=breath;$("#breath2").onclick=breath;
$("#journal").onclick=()=>{dialog('<p class="eyebrow">MON JOURNAL</p><h2>Qu’as-tu envie de déposer ici ?</h2><div class="field"><textarea id="journal-entry" rows="5" placeholder="Écris librement. Ce texte reste sur cet appareil.">'+escape(data.journal)+'</textarea></div><button class="primary" id="journal-save">Enregistrer</button>');$("#journal-save").onclick=()=>{data.journal=$("#journal-entry").value;save();$("#modal").close();toast("Journal enregistré sur cet appareil.")}};
$("#rest").onclick=()=>dialog('<div style="text-align:center"><div class="breath-orb">PAUSE</div><h2>Tu as le droit de ne rien faire.</h2><p>Profite d’une musique, d’un moment calme ou ferme simplement les yeux.</p></div>');
$("#sos").onclick=()=>dialog('<p class="eyebrow">SOS CRAQUAGE</p><h2>On fait une pause ensemble.</h2><p>Tu n’as rien raté. Pose les épaules, relâche la mâchoire. Tu peux prendre ton temps.</p><div class="actions"><button class="primary" id="sos-breath">Faire trois respirations</button><button class="outline" id="sos-kind">Me parler avec douceur</button></div>');
$("#modal-content").addEventListener("click",e=>{if(e.target.id==="sos-breath")breath();if(e.target.id==="sos-kind")dialog('<div style="text-align:center"><div class="breath-orb">TU FAIS DE TON MIEUX</div><h2>Et c’est déjà important.</h2><p>Tu peux choisir une petite action, appeler quelqu’un ou simplement te reposer. Rien ne presse.</p></div>')});
function settings(){dialog('<p class="eyebrow">MON ESPACE</p><h2>Préférences PARISFIT</h2><div class="field"><label>Comment veux-tu qu’on t’appelle ?</label><input id="name" maxlength="40" value="'+escape(data.name)+'" placeholder="Prénom facultatif"></div><p>Dans cette première version, tes données sont conservées localement dans ce navigateur, sans synchronisation.</p><div class="actions"><button class="primary" id="save-profile">Enregistrer</button><button class="outline" id="clear-data">Effacer mes données</button></div>')}
$("#settings").onclick=settings;$("#profile").onclick=settings;
$("#modal-content").addEventListener("click",e=>{if(e.target.id==="save-profile"){data.name=$("#name").value.trim();save();render();$("#modal").close();toast("Préférences enregistrées.")}if(e.target.id==="clear-data"&&confirm("Effacer les données PARISFIT sur cet appareil ?")){localStorage.removeItem(KEY);data={...defaults};render();$("#modal").close();toast("Données locales effacées.")}});
render();
/* ===== COACH IA PARISFIT — ajout premium, interface existante préservée ===== */
const coachExercises=PARISFIT_DEMO.exercises;
const coachAnim={squat:"coach-squat",pushup:"coach-pushup",plank:"coach-plank",lunge:"coach-lunge",jumpingjack:"coach-jumpingjack",mountainclimber:"coach-mountain",stretch:"coach-stretch",shoulders:"coach-shoulders"};
function coachInit(){
  if(!$("#view-coach"))return;
  if(data.name)$("#coach-greeting-text").innerHTML="Bonjour "+escape(data.name)+" ! <i>✦</i>";
  renderCoachStats();renderCoachStage("squat");renderCoachExercises("all");
  $("#coach-stage-prev").onclick=()=>{const i=coachExercises.findIndex(x=>x.id===window.parisfitCoachExercise);renderCoachStage(coachExercises[(i-1+coachExercises.length)%coachExercises.length].id);};
  $("#coach-stage-next").onclick=()=>{const i=coachExercises.findIndex(x=>x.id===window.parisfitCoachExercise);renderCoachStage(coachExercises[(i+1)%coachExercises.length].id);};
  $("#coach-stage-toggle").onclick=()=>{const v=$("#coach-stage-visual");v.classList.toggle("is-paused");$("#coach-stage-toggle").textContent=v.classList.contains("is-paused")?"▶ Reprendre":"Ⅱ Pause animation";};
  $("#coach-stage-start").onclick=coachStartSingleExercise;$("#coach-start-session").onclick=coachStartSession;
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
function coachFigure(anim){
 return '<svg class="coach-figure pose-'+anim+'" viewBox="0 0 200 220" role="img" aria-label="Coach sportif illustrant '+escape(anim)+'"><defs><linearGradient id="coachSuit" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#36c98b"/><stop offset="1" stop-color="#14734f"/></linearGradient></defs><ellipse cx="100" cy="205" rx="62" ry="8" fill="#153f3218"/><g class="figure-body"><circle class="figure-head" cx="100" cy="31" r="17" fill="#d99a72"/><path d="M94 46h12v12H94z" fill="#c98560"/><path class="figure-torso" d="M76 58Q100 48 124 58L132 116Q100 128 68 116Z" fill="url(#coachSuit)"/><path class="figure-arm figure-arm-left" d="M77 64Q62 75 54 100" fill="none" stroke="#d99a72" stroke-width="13" stroke-linecap="round"/><path class="figure-arm figure-arm-right" d="M123 64Q138 75 146 100" fill="none" stroke="#d99a72" stroke-width="13" stroke-linecap="round"/><path class="figure-leg figure-leg-left" d="M82 115Q77 145 70 177" fill="none" stroke="#244b3b" stroke-width="17" stroke-linecap="round"/><path class="figure-leg figure-leg-right" d="M118 115Q123 145 130 177" fill="none" stroke="#244b3b" stroke-width="17" stroke-linecap="round"/><path d="M70 179l-12 5M130 179l12 5" stroke="#d99a72" stroke-width="10" stroke-linecap="round"/></g><path d="M28 195h144" stroke="#9bb9a5" stroke-width="2" stroke-linecap="round" opacity=".45"/></svg>';
}
function renderCoachStage(id){
 const x=coachExercises.find(e=>e.id===id)||coachExercises[0],index=coachExercises.findIndex(e=>e.id===x.id);
 $("#coach-stage-title").textContent=x.title;$("#coach-stage-subtitle").textContent="Démonstration du mouvement · vue de face";
 $("#coach-stage-visual").innerHTML=coachFigure(x.anim);$("#coach-stage-desc").textContent=x.desc;
 $("#coach-stage-muscles").textContent=x.muscles;$("#coach-stage-level").textContent=x.level+" · "+x.time;
 $("#coach-stage-index").textContent="EXERCICE "+(index+1)+" / "+coachExercises.length;
 $("#coach-stage-visual").classList.remove("is-paused");$("#coach-stage-toggle").textContent="Ⅱ Pause animation";window.parisfitCoachExercise=x.id;
}
function renderCoachExercises(filter){
 const grid=$("#coach-exercises"),list=filter==="all"?coachExercises:coachExercises.filter(x=>x.cat===filter);
 grid.innerHTML=list.map(x=>`<article class="coach-exercise-card" data-ex="${x.id}"><div class="coach-exercise-demo">${coachFigure(x.anim)}</div><h4>${escape(x.title)}</h4><div class="ex-meta">${escape(x.level)} · ${escape(x.time)}</div><p>${escape(x.desc)}</p><div class="ex-foot">${escape(x.muscles)}${x.noMateriel?" · Sans matériel":""}</div></article>`).join("");
 $$("[data-ex]").forEach(card=>card.onclick=function(){renderCoachStage(this.dataset.ex);$("#coach-stage-visual").scrollIntoView({behavior:"smooth",block:"center"});});
}
$("#workout-rec").onclick=()=>view("coach");
let coachSessionIndex=-1;
function coachStartSingleExercise(){const id=window.parisfitCoachExercise||"squat";renderCoachStage(id);toast("Démonstration lancée. Suis le mouvement à ton rythme.");}
function coachStartSession(){
 coachSessionIndex=0;renderCoachStage(coachExercises[0].id);$("#coach-stage-index").textContent="SÉANCE GUIDÉE · 1 / 5";
 $("#coach-stage-start").textContent="Exercice suivant →";
 $("#coach-stage-start").onclick=()=>{coachSessionIndex++;if(coachSessionIndex>=5){coachSessionIndex=-1;$("#coach-stage-start").textContent="Commencer cette séance";$("#coach-stage-start").onclick=coachStartSession;toast("Séance terminée. Merci d'avoir pris ce temps.");return;}renderCoachStage(coachExercises[coachSessionIndex].id);$("#coach-stage-index").textContent="SÉANCE GUIDÉE · "+(coachSessionIndex+1)+" / 5";};
 $("#coach-stage-visual").scrollIntoView({behavior:"smooth",block:"center"});toast("Séance guidée démarrée. Premier exercice : "+coachExercises[0].title+".");
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
if("serviceWorker"in navigator&&location.protocol.startsWith("http"))addEventListener("load",()=>navigator.serviceWorker.register("./service-worker.js?v=20261127-4",{updateViaCache:"none"}).catch(()=>{}));
// Reuse existing journeys; no duplicate pages or persisted illustrative measurements.
$("#water-quick").onclick=()=>$("#water-add").click();
$("#workout").onclick=()=>view("coach");
function reading(){dialog('<p class="eyebrow">MOMENT INTELLIGENT · LECTURE</p><h2>5 principes de discipline</h2><ol>'+PARISFIT_DEMO.reading.map(t=>'<li>'+escape(t)+'</li>').join('')+'</ol><p>Un petit pas suffit pour commencer.</p>');}
$("#read-discipline").onclick=reading;$("#moment").onclick=reading;
$("#balance").onclick=()=>$("#rest").click();
$("#challenges").onclick=()=>{dialog('<p class="eyebrow">DÉFI 30 JOURS · PROPOSITION</p><h2>Moins de scroll, plus de présence.</h2><p>Chaque jour, remplace dix minutes d’écran par une activité qui te fait du bien. Ajoute cette intention à tes habitudes pour la suivre localement.</p><button type="button" class="primary" id="challenge-add">Créer mon habitude</button>');$("#challenge-add").onclick=()=>{habitDialog();$("#habit-title").value=PARISFIT_DEMO.challenge;};};
$(".mobile-brand").onclick=e=>{e.preventDefault();view("today");};
