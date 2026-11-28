"""Self-contained documentary page and integrity manifest, no application changes."""
from pathlib import Path
import html,json,hashlib,csv,re
D=Path('docs/coach/phase17')
def inline(s):
 s=html.escape(s);s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s);s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
def md(s):
 out=[];table=[];code=False
 def flush():
  if table:
   out.append('<div class="table-wrap"><table>'+''.join('<tr>'+''.join('<'+('th' if i==0 else 'td')+'>'+inline(v.strip())+'</'+('th' if i==0 else 'td')+'>' for v in row.strip('|').split('|'))+'</tr>' for i,row in enumerate(table) if not re.match(r'^\|[ :|\-]+\|$',row))+'</table></div>');table.clear()
 for line in s.splitlines():
  if line.startswith('```'):
   flush();out.append('</pre>' if code else '<pre>');code=not code;continue
  if code:out.append(html.escape(line)+'\n');continue
  if line.startswith('|'):table.append(line);continue
  flush()
  if line.startswith('#'):
   n=min(len(line)-len(line.lstrip('#'))+1,6);out.append(f'<h{n}>'+inline(line.lstrip('# '))+f'</h{n}>')
  elif line.strip():out.append('<p>'+inline(line)+'</p>')
 flush();return ''.join(out)
def main():
 docs=[('selected-squat-trial.md','1 · Essai et empreintes'),('scaling-ik-configuration-audit.md','3 · Scaling et IK — lecture seule'),('ground-reaction-forces-audit.md','4 · Forces et synchronisation'),('rms-scaling-error-analysis.md','5 · Interpréter les 4,21 cm'),('professional-review-dossier.md','6 · Dossier de revue indépendante'),('decision-report.md','7 · Décision argumentée')]
 page='''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PARISFIT · Phase17 · Qualification passive</title><style>*{box-sizing:border-box}body{margin:0;background:#edf5ef;color:#173f33;font:16px/1.65 system-ui;overflow-wrap:anywhere}main{max-width:1100px;margin:auto;padding:24px}h1{font-size:clamp(30px,5vw,48px);line-height:1.15}h2,h3{line-height:1.35}section,details{background:white;border-radius:16px;padding:24px;margin:20px 0;min-width:0}summary{font-weight:700;cursor:pointer}a{color:#176e50}code{font-size:.9em}pre{white-space:pre-wrap}.tag{display:inline-block;background:#f8d6c9;border-radius:30px;padding:8px 18px}.table-wrap{overflow-x:auto;max-width:100%}table{border-collapse:collapse;min-width:650px;width:100%;font-size:14px}th,td{border-bottom:1px solid #d9e7dd;text-align:left;vertical-align:top;padding:10px}img{max-width:100%;height:auto}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px}.metric{background:#fff;padding:20px;border-radius:12px}.metric b{display:block;font-size:32px}footer{padding:25px 0}details details{padding:12px}.notice{border-left:4px solid #df775e;padding-left:16px}</style><main><a href="../phase16/index.html">← Phase16</a><p>PARISFIT / COACH / PHASE17</p><h1>Un squat documenté.<br>Pas encore une référence admise.</h1><p class="tag">B — Qualification partielle</p><p>AB01 · Squat · prise1 + statique AB01/Static/1. Inspection passive uniquement.</p><div class="grid"><div class="metric"><b>57 / 49</b>marqueurs statiques / dynamiques</div><div class="metric"><b>44 + 13</b>définitions documentaires confirmées / plausibles</div><div class="metric"><b>0</b>centre articulaire ou mapping Rocketbox confirmé</div></div><section><h2>Ce qui bloque encore</h2><p>Ambiguïtés du protocole de placement, dépendances de traitement modifiées absentes de l’arbre Git, conventions de repères à vérifier, borne C3D incohérente et absence d’un résidu individuel AB01 identifié.</p><p class="notice">4,21 cm est une moyenne publiée des erreurs de marqueurs des modèles statiques. Ce n’est pas l’erreur mesurée de ce squat.</p><p>Aucune IK, aucun scaling exécuté, aucune correction, aucun retargeting ni animation créée. Les forces continues ne prouvent pas un contact de toute la plante du pied. Revue professionnelle non obtenue.</p></section><section><h2>Voir les données sans reconstruire un corps</h2><p>Diagrammes statiques, jamais des animations. Les projections utilisent la première frame statique existante, sans ajustement anatomique.</p><a href="static-marker-projections.svg"><img src="static-marker-projections.svg" alt="57 marqueurs statiques mesurés, projections XZ et YZ originales, sans squelette estimé"></a><p><a href="markerset-schematic.svg">Schéma documentaire des marqueurs par région et légende des ambiguïtés</a></p><a href="trial-diagnostics.svg"><img src="trial-diagnostics.svg" alt="Courbes diagnostiques de RIAS et des forces Fz locales négatives, sans filtre ajouté"></a></section><h2>Les sept livrables</h2>'''
 for name,title in docs:
  page+='<details><summary>'+title+'</summary><p><a href="'+name+'">Document Markdown</a></p>'+md((D/name).read_text())+'</details>'
 rows=list(csv.DictReader((D/'marker-anatomical-mapping.csv').read_text().splitlines()));page+='<details><summary>2 · Correspondances des 57 marqueurs</summary><p>Confirmé porte sur la proposition documentaire, pas sur la palpation individuelle. Aucune équivalence marqueur–centre articulaire ou Rocketbox admise.</p><a href="marker-anatomical-mapping.csv">Télécharger le CSV complet</a><div class="table-wrap"><table><tr><th>Label</th><th>Site documenté</th><th>Statut anatomique</th><th>Parent OpenSim</th><th>Limite / source</th></tr>'
 for r in rows:page+='<tr>'+''.join('<td>'+html.escape(r[k])+'</td>' for k in ['original_name','documented_anatomical_location','anatomical_status','opensim_parent_frame','justification'])+'</tr>'
 page+='</table></div></details><section><h2>Traçabilité et reproduction</h2><ul>'
 for n in ['verification-notes.md','source-manifest.json','c3d-inspection.json','configuration-inspection.json','source-excerpts.md','mapping-status.json','rocketbox-readonly.json','REPRODUCE.md','protected-baseline.json','browser-report.json','manifest.json']:page+='<li><a href="'+n+'">'+n+'</a></li>'
 page+='</ul><p>24 fichiers acquis, deux C3D seulement, 8 237 085 octets. Aucune archive complète téléchargée. Licences et attributions précisées dans la fiche d’essai.</p></section><footer>Rocketbox et les huit exercices préservés. Aucun contact auteur, achat, fusion ou déploiement. PR11 en brouillon. PASS technique ≠ validation scientifique.</footer></main></html>'
 (D/'index.html').write_text(page)
 (D/'manifest.json').write_text(json.dumps({'scope':'documentary integrity, not scientific admission','files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(D.iterdir()) if p.is_file() and p.name!='manifest.json'}},indent=2)+'\n')
if __name__=='__main__':main()
