"""Synthetic rigid-frame contract; NOT Michaud calibration or IK execution."""
import numpy as np
def transform(p,F,M,R,t,documented=False):
 if not documented:raise ValueError('EXPERIMENTAL_FRAME_PROVENANCE_REQUIRED')
 R=np.asarray(R);t=np.asarray(t)
 if R.shape!=(3,3) or t.shape!=(3,) or not np.isfinite(R).all() or not np.isfinite(t).all():raise ValueError('INVALID_FRAME')
 if not np.allclose(R.T@R,np.eye(3),atol=1e-10,rtol=0) or not np.isclose(np.linalg.det(R),1,atol=1e-10,rtol=0):raise ValueError('NOT_PROPER_ROTATION')
 f=np.asarray(F)@R.T
 return np.asarray(p)@R.T+t,f,np.asarray(M)@R.T+np.cross(t,f)
def ik_gate(rows,frame_documented,scaling_documented):
 # Deliberately no solver; admission requires an explicit reviewed protocol too.
 if not rows or any(r['status']!='CONFIRMÉE PAR DOCUMENTATION' or not r.get('authoritativePairSource') for r in rows):return False
 return bool(frame_documented and scaling_documented)
