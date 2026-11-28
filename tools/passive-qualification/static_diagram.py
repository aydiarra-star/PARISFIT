"""Static marker-only diagram. No body fitting or motion export."""
import c3d,numpy as np,csv,html,warnings
from pathlib import Path
D=Path('docs/coach/phase17')
def main():
 with open('.cache/phase17/source/AB01/Static/1/Data/static.c3d','rb') as f,warnings.catch_warnings():
  warnings.simplefilter('ignore');r=c3d.Reader(f);labels=[x.strip() for x in r.point_labels];p=next(r.read_frames(check_nan=False))[1][:,:3]
 # Only the first existing static frame; no averaging, transforms or correspondence fitting.
 svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 1050" role="img" aria-label="57 marqueurs mesurés de la première frame statique, projections XZ et YZ originales"><rect width="1180" height="1050" fill="#fff"/><g font-family="sans-serif" fill="#173f33"><text x="24" y="30" font-size="22">AB01 / Static / 1 · frame 0 · 57 marqueurs, aucun squelette estimé</text><text x="24" y="56" font-size="15">Projections C3D originales XZ et YZ ; numéros dans la légende. Points parfois superposés.</text>'
 for panel,(a,b) in enumerate([(0,2),(1,2)]):
  q=p[:,[a,b]];lo=q.min(axis=0);hi=q.max(axis=0);scale=min(480/(hi[0]-lo[0]),560/(hi[1]-lo[1]));xoff=35+panel*580
  svg+=f'<text x="{xoff}" y="85" font-size="17">{"XYZ"[a]} / {"XYZ"[b]} · m (orientation non anatomique)</text>'
  for i,xy in enumerate(q):
   x=xoff+20+(xy[0]-lo[0])*scale;y=675-(xy[1]-lo[1])*scale;svg+=f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4" fill="#176e50"/><text x="{x+5:.2f}" y="{y-3:.2f}" font-size="10">{i+1}</text>'
 for i,label in enumerate(labels):
  x=30+(i//15)*285;y=720+(i%15)*20;svg+=f'<text x="{x}" y="{y}" font-size="14">{i+1} · {html.escape(label)}</text>'
 svg+='</g></svg>'; (D/'static-marker-projections.svg').write_text(svg)
if __name__=='__main__':main()
