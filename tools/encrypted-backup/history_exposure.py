"""Read-only per-path/version/ref inventory. No ref mutation or history rewriting."""
import subprocess,json,collections
from pathlib import Path
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase27'
def git(*a):return subprocess.check_output(['git',*a],cwd=R)
def tree(ref):
 out=set()
 for line in git('ls-tree','-rz',ref).split(b'\0'):
  if not line:continue
  h,p=line.split(b'\t',1);mode,typ,oid=h.decode().split()
  if typ=='blob':out.add((p.decode(),oid))
 return out
old=json.loads((R/'docs/coach/phase25/history-inventory.json').read_text());commits=git('rev-list','--all').decode().splitlines();pairs=set().union(*(tree(c) for c in commits));assert pairs=={(r['path'],r['gitBlob']) for r in old},'History changed: new full audit needed'
head=tree('HEAD');main=tree('refs/remotes/origin/main');refs={r:tree(r) for r in git('for-each-ref','--format=%(refname)').decode().splitlines()};alltips=set().union(*refs.values());headpaths={p for p,o in head};tipPaths={p for p,o in alltips}
rows=[]
for r in old:
 p=r['path'];oid=r['gitBlob'];pair=(p,oid)
 rows.append({**r,'atCurrentHEAD':pair in head,'atRemoteMain':pair in main,'worktreePathExists':(R/p).is_file(),'atRefTips':[ref for ref,t in refs.items() if pair in t],'historicalOnlyVersion':pair not in alltips,'pathAbsentFromCurrentHEAD':p not in headpaths,'pathAbsentFromEveryTip':p not in tipPaths})
removedPaths=sorted({r['path'] for r in rows if r['pathAbsentFromEveryTip']});historical=[r for r in rows if r['historicalOnlyVersion']];out={'commits':len(commits),'pathVersions':len(rows),'historicalOnlyVersions':len(historical),'pathsAbsentFromEveryTip':removedPaths,'pathsAbsentFromCurrentHEAD':sorted({r['path'] for r in rows if r['pathAbsentFromCurrentHEAD']}),'headResources':dict(collections.Counter(r['category'] for r in rows if r['atCurrentHEAD'])),'historicalOnlyCategories':dict(collections.Counter(r['category'] for r in historical))}
(D/'history-versions.json').write_text(json.dumps(rows,indent=2)+'\n');(D/'history-summary.json').write_text(json.dumps(out,indent=2)+'\n');(D/'historical-only-versions.json').write_text(json.dumps(historical,indent=2)+'\n');print(json.dumps(out,indent=2))
# No deletion inferred from an absent path alone: record actual git D events too.
events=git('log','--all','--diff-filter=D','--format=commit %H','--name-status').decode();(D/'deletion-events.txt').write_text(events)
