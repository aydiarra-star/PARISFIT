"""Analytical two-segment geometry. No floor projection or temporal filtering."""
import math
def solve(hip,goal,pole,l1,l2):
 if not all(math.isfinite(x) for x in [*hip,*goal,*pole,l1,l2]) or min(l1,l2)<=1e-6:raise ValueError('INVALID_IK_LENGTH_OR_DATA')
 v=[g-h for g,h in zip(goal,hip)];distance=math.sqrt(sum(x*x for x in v))
 if distance<1e-6:raise ValueError('DEGENERATE_IK_DIRECTION')
 axis=[x/distance for x in v];dot=sum(x*y for x,y in zip(pole,axis));orthogonal=[x-dot*y for x,y in zip(pole,axis)];length=math.sqrt(sum(x*x for x in orthogonal))
 if length<1e-6:raise ValueError('DEGENERATE_IK_POLE')
 d=max(abs(l1-l2)+1e-5,min(l1+l2-1e-5,distance));x=(l1*l1-l2*l2+d*d)/(2*d);height=math.sqrt(max(0,l1*l1-x*x))
 knee=[h+a*x+p/length*height for h,a,p in zip(hip,axis,orthogonal)];ankle=[h+a*d for h,a in zip(hip,axis)]
 return knee,ankle,abs(distance-d)
