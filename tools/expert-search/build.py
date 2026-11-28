"""Build a public-source candidate register. No network requests, messages or source processing."""
from pathlib import Path
import json,csv
D=Path('docs/coach/phase22');D.mkdir(exist_ok=True)
DATE='2026-11-27'
REF='7a301e0f61b1328b70192b3514fdae26eaaad183'
sources=[
('S01','ZHAW — projet74439, direction, publications et contact','https://www.zhaw.ch/en/research/project/74439','Key data / Publications / Contact, chunks0–1','Silvio Lorenzetti, School of Engineering ; projet force training terminé05/2026 ; silvio.lorenzetti@zhaw.ch ; +41(0)589344164. Pas de tarif de revue publié sur cette page.'),
('S02','Lorenzetti et al.2018 — How to squat?','https://pmc.ncbi.nlm.nih.gov/articles/PMC6050697/','Methods, chunks1–2 ; auteurs dans correction S03','Squats, Vicon100Hz synchronisé aux forces Kistler2000Hz, marqueurs et centres fonctionnels. Coautorat Lorenzetti/Taylor. Preuve de travaux collectifs, pas exécution personnelle de chaque mesure.'),
('S03','Correction2020 de How to squat?','https://pmc.ncbi.nlm.nih.gov/articles/PMC6990583/','chunks0–1','DOI10.1186/s13102-020-0160-6 ; correction du signe de ΔD* dans une phrase. Ne pas masquer cette correction ni transférer ses seuils à AB01.'),
('S04','Jaeggi, Achermann, Lorenzetti2024 — Female Lower Body Muscle Forces','https://www.mdpi.com/2411-5142/9/2/68','Authors, Data Collection, Modeling Simulation et Scaling, chunks0–1','DOI10.3390/jfmk9020068 ; Vicon200Hz,42 marqueurs, forces1000Hz, OpenSim4.3 et scaling sur essai statique. Démonstration directe du domaine squat/OpenSim.'),
('S05','ETH — William R. Taylor','https://hest.ethz.ch/en/studies/health-sciences-and-technology/master-hst/tutors/tutors-a-z/william-r-taylor.html','Contact et Research projects','Professeur, ETH Zurich / Institute for Biomechanics ; mouvement, sports, capture et fluoroscopie ; bt@ethz.ch ; +41446330595. Aucun tarif de revue affiché.'),
('S06','ETH — CAMS-Knee Project','https://movement.ethz.ch/data-repository/cams-knee-project.html','Comprehensive Assessment / Publications / Contact','Laboratoire de Taylor, données synchrones de cinématique à marqueurs, forces sol, EMG et implants ; DOI10.1016/j.jbiomech.2017.09.022. Population implantée distincte de AB01 ; contact bt@ethz.ch.'),
('S07','KU Leuven — Friedl De Groote, HMB','https://gbiomed.kuleuven.be/english/research/50000737/research/HMB/People/People/00046458','Annuaire et publications, chunk0','Affiliation Human Movement Biomechanics Research Group ; téléphone+3216372682. Travaux sur modèle patellofémoral pour grandes flexions incluant squats,2026, LIRIAS4437961 : notice institutionnelle examinée, article complet non examiné.'),
('S08','OpenSim — Fellows','https://opensimconfluence.atlassian.net/wiki/spaces/OpenSim/pages/53088743/OpenSim+Fellows','Introduction chunk0 ; Friedl De Groote chunk1','Programme expert, possibilité générale de consulter les Fellows ; rémunération à négocier individuellement, aucun tarif. De Groote : modèles individualisés, API C++, Kalman smoothing implémenté. Notice mêle grades/biographie historiques : ne pas en déduire un grade actuel exact.'),
('S09','UBC — profil Friedl De Groote','https://balancefalls.ubc.ca/about-us/researchers/friedl-de-groote','Biography / Contact','Affiliation déclarée KU Leuven (pas UBC comme employeur), approche expérimentale/computationnelle ; friedl.degroote@kuleuven.be. Grade historique possible, non utilisé pour classer.'),
('S10','Rennes2/M2S — Franck Multon','https://m2s.recherche.univ-rennes2.fr/user/franck-multon','Member profile','Affiliation affichée Inria ; axe analyse/modélisation/simulation du mouvement ; franck.multon@inria.fr. Aucun tarif publié sur la fiche.'),
('S11','Liu, Mucherino, Hoyet, Multon2018 — Surface based motion retargeting','https://inria.hal.science/hal-01919065v1/file/Surface_based_Motion_Retargeting_by_Preserving_Spatial_Relationship-hal.pdf','Première page / Abstract / Introduction, chunk0','MIG2018, DOI10.1145/3274247.3274507, HAL01919065 ; transfert préservant relations entre surfaces. Ne prouve pas compétence OpenSim ou validation physiologique.'),
('S12','LLS Biomechanics GmbH — présentation et conseil','https://llsbiomechanics.ch/','Home / about us / Purpose','Conseil en biomécanique théorique et expérimentale ; Renate List CEO, Silvio Lorenzetti présenté ; formulaire public et adresse professionnelle Rhiweg22,8260Stein am Rhein. Pas de prix publié sur cette page ; formulaire non rempli.'),
]
(D/'sources.json').write_text(json.dumps([{'id':i,'title':t,'url':u,'consulted':DATE,'section':sec,'observed':o,'retrieval':'fetch_page, selected sections only; no full copyrighted page copy'} for i,t,u,sec,o in sources],ensure_ascii=False,indent=2)+'\n')
S={i:(t,u,sec,o) for i,t,u,sec,o in sources}
def cite(*ids):return ' '.join(f'[{int(i[1:])}]({S[i][1]})' for i in ids)
H=f'> Phase22 — recherche publique seulement. Consultation : **{DATE}** (date de session). Référence `{REF}`. Aucun contact, devis demandé, document transmis ou engagement.\n\n'
def put(n,t):(D/n).write_text(H+t)
put('expertise-criteria.md','''# Critères de qualification et portée de la recherche

## Niveaux de preuve

- **Démontré dans un travail publié** : méthode ou projet pertinent décrit précisément. Le coautorat prouve une participation scientifique, pas que la personne a posé les marqueurs ou configuré le trigger elle-même.
- **Déclaré institutionnellement** : affiliation, domaine, coordonnées professionnelles ; consulter la source récente plutôt qu'une ancienne adresse d'article.
- **Adéquation inférée par PARISFIT** : capacité plausible de critique documentaire au vu des travaux, pas une offre acceptée ni une disponibilité.
- **Non démontré dans les sources inspectées** : ne signifie pas absence de compétence.

## Priorités et sélection

P1 : biomécanique expérimentale, squat/mouvements de force, capture optique, marqueurs, appuis et mesures cinétiques. P2 : modèles musculosquelettiques individualisés, OpenSim/scaling, incertitudes méthodologiques. P3 : animation/retargeting, complément uniquement. Un expertP3 ne remplace pas un biomécanicien.

Critères indispensables du responsable ou de l'équipe : anatomie/centres, capture, modèle/scaling, forces, synchronisation et capacité de contradiction. Le dossier AB01 ne requiert pas une nouvelle exécution logicielle. Aucun score numérique artificiel : classement argumenté par preuves, lacunes et complémentarité. Aucun candidat n'est déclaré certifié sur tous les critères.

## Indépendance : appréciation limitée

Les trois finalistes ne figurent pas parmi les trois auteurs identifiés du dataset AB01 (Alizadeh Noghani, Green, Bolívar-Nieto ; sources21). Aucune relation directe au dataset établie dans les sources examinées ; recherche nominative ciblée non concluante. **Cela ne certifie ni absence de collaboration, ni absence d'intérêt financier.** Faire déclarer les liens après autorisation. Lorenzetti/Taylor sont co-auteurs ; De Groote participe à la communauté OpenSim ; Lorenzetti est présenté par une société de conseil. Ces faits sont signalés, non transformés en accusations.

## Méthode et limites

Recherche ciblée de noms/domaines, vérification sur institutions, documentation officielle et publications. Corpus de12 sources, sections réellement consultées dans [sources.json](sources.json). Pas d'annuaire exhaustif, pas d'évaluation de disponibilité. Les pages anciennes servent de preuve historique de travaux, pas d'affiliation actuelle. Les contacts sont publics/professionnels, non testés par email/appel et non enrichis avec données privées. Aucune publication complète, portrait ou CV privé redistribué.

Tarifs : recherche des pages de présentation/conseil et requêtes nom+consulting/fees/rates ; aucune grille applicable à la revue AB01 retrouvée. Un financement de recherche, un tarif de cours ou de dîner de workshop n'est pas un prix d'expertise. « devis nécessaire » ne signifie ni gratuit ni devis demandé. Voir [recherche tarifaire](cost-search.json).
''')
profiles=[
{'id':'C01','name':'Silvio Lorenzetti','affiliation':'ZHAW, School of Engineering ; présentation également chez LLS Biomechanics','priority':'1','rank':1,'contact':'silvio.lorenzetti@zhaw.ch','contact_source':'S01','sources':['S01','S02','S03','S04','S12'],'fit':'Très forte pour une revue squat/capture/forces et scaling ; premier choix documentaire proposé','experimental':'Squat et exercices de force, capture Vicon, marqueurs, plateformes Kistler : travaux2018/2024','opensim':'Démontré en coautorat : OpenSim4.3, scaling statique et modèle Gait2392 adapté dans étude2024','sync':'Acquisition cinématique/forces explicitement synchronisée dans étude2018 ; contribution personnelle au montage non isolée','independence':'Pas auteur AB01 identifié ; co-auteur de Taylor ; activité LLS déclarée, éventuels intérêts commerciaux à déclarer','limits':'Protocoles chargés/IfB/Plug-in Gait distincts de Biomech57 AB01 ; pas de compétence Motive3.0.3 spécifiquement établie','availability':'inconnue ; service de conseil apparent via LLS, acceptation du cas non établie'},
{'id':'C02','name':'William R. Taylor','affiliation':'ETH Zurich, Institute for Biomechanics / Laboratory for Movement Biomechanics','priority':'1','rank':2,'contact':'bt@ethz.ch','contact_source':'S05','sources':['S02','S03','S05','S06'],'fit':'Très forte pour instrumentation, centres, appuis, synchronisation et critique des mesures','experimental':'Co-auteur How to squat? ; laboratoire capture/fluoroscopie ; CAMS-Knee marqueurs, forces, EMG et implants','opensim':'Modélisation musculosquelettique pertinente ; usage personnel OpenSim/scaling non démontré par les sections retenues','sync':'CAMS-Knee décrit données synchrones multimodales ; étude squat2018 synchronisée','independence':'Pas auteur AB01 identifié ; co-auteur Lorenzetti, donc pas un deuxième avis totalement indépendant de celui-ci','limits':'CAMS-Knee inclut prothèses, non transférable à sujet sain AB01 ; disponibilité et prise en charge documentaire inconnues','availability':'inconnue ; adéquation inférée des travaux, pas de service de revue documentaire garanti'},
{'id':'C03','name':'Friedl De Groote','affiliation':'KU Leuven, Department of Movement Sciences / Human Movement Biomechanics Research Group','priority':'2','rank':3,'contact':'friedl.degroote@kuleuven.be','contact_source':'S09','sources':['S07','S08','S09'],'fit':'Très forte en critique modèle/scaling, centres, identifiabilité et limites de reconstruction ; complément méthodologique','experimental':'Approche computationnelle et expérimentale déclarée ; travaux grandes flexions/squats listés KU2026','opensim':'OpenSim Fellow ; API C++, modèles individualisés et algorithme Kalman implémenté attestés','sync':'Compétence spécifique de configuration matériel de synchronisation et plateforme du squat non démontrée dans le corpus consulté','independence':'Pas auteur AB01 identifié ; lien scientifique déclaré à OpenSim, à prendre en compte pour évaluer cet outil','limits':'Expertise sportive squat moins directement documentée que C01/C02 ; ne pas attribuer automatiquement chaque compétence expérimentale ; grades discordants/anciens dans notices','availability':'inconnue ; programme Fellows encourage les consultations sans garantir acceptation ni tarif individuel'},
{'id':'C04','name':'Franck Multon','affiliation':'Inria ; fiche au laboratoire M2S, Rennes2','priority':'3','rank':None,'contact':'franck.multon@inria.fr','contact_source':'S10','sources':['S10','S11'],'fit':'Complément pour contraintes morphologiques et préservation des contacts lors d’un éventuel transfert, pas responsable biomécanique unique','experimental':'Analyse du mouvement déclarée ; expérience instrumentale squat/marqueurs anatomiques/plateformes non qualifiée ici','opensim':'Non démontré dans les sources inspectées','sync':'Non démontré dans les sources inspectées','independence':'Pas auteur AB01 identifié ; liens projets3D à déclarer ; aucune indépendance financière certifiée','limits':'Retargeting de surfaces ne valide ni anatomie, ni forces, ni OpenSim ; ne remplace pas P1/P2','availability':'inconnue ; publications pertinentes, pas de prestation acceptée'},
]
for p in profiles:p.update({'consulted':DATE,'public_cost':'devis nécessaire','contacted':False,'documents_sent':False,'quote_requested':False})
(D/'candidates.json').write_text(json.dumps(profiles,ensure_ascii=False,indent=2)+'\n')
text='# Spécialistes vérifiés — classement documentaire, pas engagement\n\nLes trois finalistes sontC01,C02,C03 ; C04 est un complémentP3. Coordonnées copiées de sources publiques, pas de message envoyé. Le classement est notre appréciation à partir des preuves citées, **pas un avis de l’expert sur AB01**.\n\n'
for p in profiles:
 text+=f"## {p['id']} — {p['name']} · priorité{p['priority']}\n\n- **Affiliation publique :** {p['affiliation']}. {cite(p['contact_source'])}\n- **Travaux et expérience :** {p['experimental']}. {cite(*p['sources'][:4])}\n- **OpenSim/scaling :** {p['opensim']}. {cite(*(['S04'] if p['id']=='C01' else ['S08'] if p['id']=='C03' else p['sources'][-1:]))}\n- **Synchronisation :** {p['sync']}. {cite(*(['S02'] if p['id']=='C01' else ['S02','S06'] if p['id']=='C02' else p['sources'][-2:]))}\n- **Adéquation proposée :** {p['fit']}. Il s'agit d'une inférence PARISFIT.\n- **Contact professionnel public :** `{p['contact']}`. {cite(p['contact_source'])}\n- **Possibilité de mission :** {p['availability']}.\n- **Indépendance / liens :** {p['independence']}. {cite(*p['sources'])}\n- **Limites à confirmer :** {p['limits']}.\n- **Coût : devis nécessaire.** Aucun tarif applicable trouvé dans le périmètre consulté ; ni demande ni engagement.\n\n"
text+='## Précisions qui changent la lecture\n\nL’adresseZHAW de Lorenzetti est privilégiée à ses anciennes affiliations SFISM/ETH des articles. Le grade exact de De Groote n’est pas tranché entre notices historiques : affiliation KU et travaux sont vérifiés, pas une promotion supposée. Pour Taylor, le contact ETH actuellement affiché est `bt@ethz.ch`, sans déduire une adresse du nom. Le travail How to squat? possède une correction2020 du signeΔD* : elle est incluse, sans reprendre de recommandations cliniques pour AB01. '+cite('S01','S03','S05','S07','S08','S09')+'\n\nTous les liens, sections et dates : [registre des sources](sources.md). Aucun candidat n’a examiné le dossier.\n'
put('expert-candidates.md',text)
labs=[
('L01','ZHAW — School of Engineering, projet force training74439','C01','1','Projet universitaire de modélisation personnalisée et force training, projet terminé05/2026 ; ne pas présenter ce projet comme laboratoire autonome disponible','S01','silvio.lorenzetti@zhaw.ch'),
('L02','ETH Zurich — Laboratory for Movement Biomechanics','C02','1','Laboratoire expérimental, capture/forces et projet CAMS-Knee synchronisé ; population et objectif distincts de AB01','S06','bt@ethz.ch'),
('L03','KU Leuven — Human Movement Biomechanics Research Group','C03','2','Groupe universitaire, modèles individualisés et projets/notice de grandes flexions ; services externes et responsable de mission à confirmer','S07','page institutionnelle et +32 16 37 26 82'),
('L04','M2S / Inria — axe analyse, modélisation et simulation du mouvement','C04','3','Piste complémentaire3D via Franck Multon ; ne pas attribuer automatiquement ses travaux à tous les membres ou garantir une prestation','S10','franck.multon@inria.fr'),
('L05','LLS Biomechanics GmbH','C01','1','Société de conseil, pas un laboratoire universitaire ; prestation biomécanique publiquement annoncée ; même réseau queC01, pas un avis indépendant supplémentaire','S12','formulaire public https://llsbiomechanics.ch/ (non rempli)'),
]
text='# Laboratoires et structures — voies possibles, non contactées\n\nLes structures ne sont pas cinq nouveaux experts indépendants : elles recoupent les profils. Aucun plateau technique réservé, aucune collecte proposée.\n\n'
for i,n,c,p,desc,s,contact in labs:text+=f'## {i} — {n}\n\nPriorité{p} ; lien au candidat{c}. {desc}. {cite(s)}\n\nCoordonnée publiée : {contact}. {cite(s)}\n\nCoût de revue : **devis nécessaire** ; pas de grille applicable retrouvée dans cette source. Disponibilité, personne réalisant la revue, statut contractuel et conflits : à confirmer après autorisation.\n\n'
put('laboratories.md',text)
with (D/'candidate-comparison.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','type','nom','affiliation_ou_structure','priorite','rang_finaliste','pertinence_scientifique','experience_demontree','opensim_scaling','synchronisation','adequation_AB01','independance_apparente','contact_public','source_contact','cout_public','a_confirmer','sources','date_consultation','contact_effectue'])
 for p in profiles:w.writerow([p['id'],'personne',p['name'],p['affiliation'],p['priority'],p['rank'] or '',p['fit'],p['experimental'],p['opensim'],p['sync'],p['fit'],p['independence'],p['contact'],S[p['contact_source']][1],p['public_cost'],p['limits']+' ; '+p['availability'],' ; '.join(S[i][1] for i in p['sources']),DATE,'non'])
 for i,n,c,p,desc,s,contact in labs:w.writerow([i,'structure liée, non candidat indépendant supplémentaire',n,n,p,'',desc,'Voir '+c,'Voir '+c,'Voir '+c,desc,'Recoupe '+c+' ; indépendance non certifiée',contact,S[s][1],'devis nécessaire','Disponibilité ; contrat ; responsable ; conflits ; tarif',S[s][1],DATE,'non'])
put('contact-readiness.md','''# Préparation du choix — aucun contact autorisé

## Ce qui est prêt

Quatre personnes réelles vérifiées et cinq structures liées, trois finalistes proposés. Coordonnées professionnelles de pages publiques relevées uniquement pour un choix ultérieur. Aucun mailto activé, aucun formulaire rempli, aucune demande de devis ou de disponibilité. Il n'existe aucune confirmation de leur part.

## Ce que l'utilisateur doit décider avant une démarche

1. Choisir le candidat et le canal professionnel ; confirmer qu'il veut autoriser une sollicitation, pas simplement la recherche.
2. Approuver le message FR/EN préparé21, son expéditeur, le destinataire et la portée : revue documentaire, pas nouvelle acquisition ni reconstruction.
3. Approuver séparément les pièces. Aucun dossier ni accès global au dépôt avec le premier message sans accord explicite ; note21 sur licences indispensable.
4. Après autorisation seulement : faire confirmer expérience propre sur Biomech57/centres, OpenSim, synchronisation matérielle, disponibilité, rôle des collaborateurs et conflits avec PARISFIT/auteurs/fournisseurs.
5. Si mission rémunérée : demander puis examiner un devis uniquement après nouvelle autorisation ; **aucun budget, tarif ou durée accepté à ce stade**. L'estimation indicative21 n'est ni un tarif publié ni une estimation fournie par ces candidats.
6. Obtenir des conditions écrites d'indépendance, confidentialité et utilisation de l'avis ; aucune rémunération conditionnée à une conclusion favorable.

## Choix scientifique recommandé, non action

Commencer par examinerC01 pour la couverture squat+OpenSim. C02 offre une expertise instrumentale forte mais partage des publications avecC01 : ne pas compter leurs avis comme entièrement indépendants. C03 est un complément méthodologique intéressant pour éviter de dépendre d'un seul réseau expérimental, sans prétendre à l'indépendance absolue. C04 n'interviendrait qu'en complément d'un biomécanicien et d'une éventuelle phase3D séparément autorisée.

Liens locaux : [messages21](../phase21/expert-outreach-fr.md), [anglais](../phase21/expert-outreach-en.md), [confidentialité](../phase21/collaboration-and-confidentiality.md), [note de droits](../phase21/submission-addendum.md), [grille professionnelle](../phase21/professional-evaluation-grid.md).

Données du dataset CC BY4.0 ≠ article CC BY-NC-ND4.0 ; ne pas joindre automatiquement l'article, des figures, modèles, géométries ou archives. Les emails publics ne constituent ni consentement au partage ni relation contractuelle.
''')
put('decision-report.md','''# Phase22 — trois candidats qualifiés pour être examinés par l'utilisateur

## Sélection proposée

1. **Silvio Lorenzetti — ZHAW (P1).** Meilleure couverture directe identifiée du squat instrumenté, des forces, des marqueurs et d'OpenSim/scaling. Preuves expérimentales2018 et modélisation2024. Activité de conseil LLS à déclarer lors d'une future mission.
2. **William R. Taylor — ETH Zurich, Laboratory for Movement Biomechanics (P1).** Très pertinent pour centres/mesures expérimentales et synchronisation ; co-auteur squat et projet CAMS-Knee. Expérience OpenSim personnelle non conclue ici ; lien de coautorat avecC01 à considérer.
3. **Friedl De Groote — KU Leuven/HMB (P2).** OpenSim Fellow, modèles individualisés et méthodes numériques ; complément critique pertinent. Compétence exacte sur instrumentation/timing du squat à confirmer, pas déduite du titre.

Les preuves et sources publiques sont détaillées dans [fiches](expert-candidates.md), [structures](laboratories.md), [CSV comparatif](candidate-comparison.csv) et [sources](sources.md). Franck Multon (Inria/M2S,P3) est retenu seulement comme complément retargeting, pas substitut biomécanique.

## Coûts et limites

Pour chacun : **devis nécessaire**. Aucun prix de revueAB01 publié trouvé dans les pages/requêtes inspectées. Pas d'invention de prix, pas de demande envoyée. Disponibilité, acceptation, capacité contractuelle et indépendance complète inconnues. Les travaux publiés prouvent une pertinence, pas une évaluation déjà rendue ni la capacité personnelle de couvrir chaque instrument.

## Contrôles et préservation

[Tests et intégrité](verification.json), [CI de référence](ci-reference-runs.json). Recherches et lectures publiques seulement ; aucune exécution de pipeline source. Aucun scaling, IK, retargeting, COP, nouvelle animation, changement runtime/Rocketbox. Huit exercices et toutes les preuves antérieures conservés. Aucun achat, envoi, engagement, merge ou déploiement. PR11 demeure draft.

**La décision finale appartient à l'utilisateur.** Cette sélection ne donne aucune autorisation de contact. Prochaine étape : choisir quel profil envisager, puis autoriser explicitement une sollicitation et son périmètre, conformément à [contact-readiness.md](contact-readiness.md). Aucun candidat contacté ou dossier transmis.
''')
put('sources.md','# Sources publiques consultées\n\nConsultation de toutes les sources ci-dessous : **'+DATE+'**. Les notes sont des synthèses de sections, pas des copies complètes des sites. Les adresses CDN avec jetons et les photographies ne sont pas conservées.\n\n'+'\n\n'.join(f'## {i} — {t}\n\n[{int(i[1:])}]({u})\n\nSection : {sec}.\n\nFait relevé / portée : {o}' for i,t,u,sec,o in sources))
cost={'consulted':DATE,'method':'No quote request. Public profile/project/consulting pages and targeted search only.','queries':['"Silvio Lorenzetti" "consulting" fee','"William Taylor" "ETH" consulting fees biomechanics','"Friedl De Groote" consulting rates fees','"Franck Multon" "consulting" "price"'],'sources_inspected_for_rates':['S01','S05','S07','S08','S09','S10','S12'],'result':'No public fee applicable to documentary AB01 review identified in inspected scope; devis nécessaire for all. No claim that no tariff exists anywhere.','excluded_prices':'Workshop meals/course charges, research funding and software pricing are not expert-review rates.','engagement':False}
(D/'cost-search.json').write_text(json.dumps(cost,ensure_ascii=False,indent=2)+'\n')
print('6 deliverables and public evidence register written; no contact functionality')
