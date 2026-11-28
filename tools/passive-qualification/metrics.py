"""Descriptive geometry/counting, never an anatomical reconstruction."""
import numpy as np
def project_to_plate(points,corners):
    c=np.asarray(corners,dtype=float);p=np.asarray(points,dtype=float)
    if c.shape!=(4,3) or p.ndim!=2 or p.shape[1]!=3 or not np.isfinite(c).all() or not np.isfinite(p).all():raise ValueError('finite XYZ required')
    u,v=c[1]-c[0],c[3]-c[0];basis=np.stack([u,v],axis=1)
    if np.linalg.matrix_rank(basis)!=2:raise ValueError('degenerate plate')
    normal=np.cross(u,v);normal/=np.linalg.norm(normal)
    uv=np.linalg.lstsq(basis,(p-c[0]).T,rcond=None)[0].T
    return uv,(p-c[0])@normal

def frame_inventory(file_bytes,data_block,frame_bytes,parameter_frames,first,last):
    assert data_block>=1 and frame_bytes>0
    data_bytes=file_bytes-(data_block-1)*512
    complete,remainder=divmod(data_bytes,frame_bytes)
    return {'completeFramesByBytes':complete,'trailingBytes':remainder,'matchesPointFrames':complete==parameter_frames,'matchesInclusiveHeader':complete==last-first+1}
