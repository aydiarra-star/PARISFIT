from pathlib import Path
import subprocess,json,hashlib
D=Path('docs/coach/phase23');D.mkdir(exist_ok=True)
def git(*a):return subprocess.check_output(['git',*a]).decode().strip()
head=git('rev-parse','HEAD');main=git('rev-parse','origin/main');ref=git('rev-parse','5379624')
j={'auditedHEAD':head,'branch':git('branch','--show-current'),'reference':ref,'referenceIsAncestor':subprocess.run(['git','merge-base','--is-ancestor',ref,head]).returncode==0,'mainFetched':main,'mergeBase':git('merge-base',main,head),'leftMainRightHeadCounts':git('rev-list','--left-right','--count',main+'...'+head),'initialWorktree':'clean observed before creating phase23','changedPaths':git('diff','--name-status',main,head).splitlines(),'runtimeHistory':git('log','-6','--format=%H %s','--','index.html','styles.css','app.js').splitlines(),'baseline':{}}
for p in git('ls-tree','-r','--name-only',ref).splitlines():j['baseline'][p]=hashlib.sha256(Path(p).read_bytes()).hexdigest()
(D/'git-evidence.json').write_text(json.dumps(j,indent=2)+'\n')
(D/'main-diff-stat.txt').write_text(git('diff','--stat',main,head)+'\n');(D/'main-diff-name-status.txt').write_text(git('diff','--name-status',main,head)+'\n');(D/'main-runtime.diff').write_text(git('diff',main,head,'--','index.html','styles.css','app.js','demo-data.js','service-worker.js','coach-3d.js','coach-transition-gate.js')+'\n')
print(head,main,j['leftMainRightHeadCounts'],len(j['baseline']))
