"""Numbered read-only excerpts and documentary illustrations, not motion generation."""
from pathlib import Path
import json,hashlib,html
D=Path('docs/coach/phase17');R=Path('.cache/phase17/source')
RANGES={'MATLAB tools/trial_class.m':[(35,39),(127,144),(191,218),(264,286),(317,382),(444,463),(484,496),(616,640),(770,790)],'AB01/Squat/1/Processing/process_trial_data.m':[(1,22)],'AB01/Squat/1/Processing/process_force_data.m':[(1,100)],'AB01/Static/1/Setup/Setup_Scale.xml':[(1,25),(544,574),(910,934)],'AB01/Static/1/Setup/Setup_Scale_GUI.xml':[(1,25),(544,574),(910,934)],'AB01/Squat/1/Setup/Setup_IK.xml':[(1,22),(310,340)],'AB01/Squat/1/Setup/Setup_External_Forces.xml':[(1,52)],'All subjects processing/save_data_info.m':[(1,24)],'All subjects processing/add_to_path.m':[(1,8)],'Model/Biomech57.osim':[(29,35),(5759,5792)]}
def main():
 s='# Extraits officiels numérotés — lecture seule\n\nRéférence Git `a26fe4852a78f30c5e8a437b158847031cb8dc3c`. Numéros de lignes dans les fichiers originaux, empreintes dans source-manifest.json. Citations limitées à l’audit ; aucun code exécuté.\n'
 for p,rs in RANGES.items():
  lines=(R/p).read_text().splitlines();s+='\n## '+p+'\n'
  for a,b in rs:s+='\n```text\n'+'\n'.join(f'{i}: {lines[i-1]}' for i in range(a,min(b,len(lines))+1))+'\n```\n'
 (D/'source-excerpts.md').write_text(s)
 d=json.loads((D/'c3d-inspection.json').read_text())['dynamic'];series=d['diagnosticSeries'];svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 580" role="img" aria-label="Échantillons de diagnostic, forces Fz locales négatives et hauteur RIAS dans le repère original"><rect width="900" height="580" fill="#fff"/><g font-family="sans-serif" fill="#173f33"><text x="30" y="32" font-size="22">AB01 / Squat / 1 — mesures originales, aucune IK</text>'
 for n,(key,title) in enumerate([('RIAS_original_z_m','RIAS · coordonnée Z C3D originale (m), pas centre de hanche'),('Fz1_local_N','Fz local (N) · plate 1 en vert, plate 2 en corail')]):
  y=75+n*240;keys=[key] if n==0 else ['Fz1_local_N','Fz2_local_N'];vals=[v[k] for v in series for k in keys];lo=min(vals);hi=max(vals);svg+=f'<text x="30" y="{y}" font-size="17">{title}</text><text x="30" y="{y+24}" font-size="13">{lo:.3f} à {hi:.3f} ; 0 à {d["relativePointSeconds"][1]:.3f} s ; un échantillon affiché sur 10</text>'
  for i,k in enumerate(keys):
   points=' '.join(f'{55+v["t"]/15*800:.2f},{y+185-(v[k]-lo)/(hi-lo)*125:.2f}' for v in series);svg+=f'<polyline points="{points}" fill="none" stroke="{["#176e50","#df775e"][i]}" stroke-width="2"/>'
 svg+='<text x="30" y="565" font-size="14">Courbes diagnostiques uniquement ; seuils et vérifications calculés sur tous les échantillons.</text></g></svg>'
 (D/'trial-diagnostics.svg').write_text(svg)
if __name__=='__main__':main()
