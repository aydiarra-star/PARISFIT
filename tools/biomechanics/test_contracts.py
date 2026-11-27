import unittest,json,struct,copy,sys
from pathlib import Path
from contracts import bvh_contract,glb_contract,compare_positions,Invalid,REQUIRED
from validate import validate
C=json.loads(Path('tools/biomechanics/criteria.json').read_text())
def bvh(names=REQUIRED):
 h='HIERARCHY\nROOT '+names[0]+'\n{\nOFFSET 0 0 0\nCHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation\n'
 for n in names[1:]:h+='JOINT '+n+'\n{\nOFFSET 0 1 0\nCHANNELS 3 Zrotation Xrotation Yrotation\n}\n'
 return h+'}\nMOTION\nFrames: 2\nFrame Time: 0.0166666667\n'+('\n'.join([' '.join(['0']*(6+3*(len(names)-1)))]*2))+'\n'
def glb(change=lambda d:None):
 binary=struct.pack('<10f',0,2.4,0,0,0,1,0,0,0,1)
 d={'asset':{'version':'2.0'},'nodes':[{'name':str(i)} for i in range(80)],'skins':[{'joints':list(range(80))}],'buffers':[{'byteLength':40}],'bufferViews':[{'buffer':0,'byteOffset':0,'byteLength':8},{'buffer':0,'byteOffset':8,'byteLength':32}],'accessors':[{'bufferView':0,'componentType':5126,'type':'SCALAR','count':2},{'bufferView':1,'componentType':5126,'type':'VEC4','count':2}],'animations':[{'name':'phase9-cmu-control','channels':[{'sampler':0,'target':{'node':0,'path':'rotation'}}],'samplers':[{'input':0,'output':1}]}]}
 change(d);js=json.dumps(d).encode();js+=b' '*(-len(js)%4);return struct.pack('<III',0x46546c67,2,28+len(js)+len(binary))+struct.pack('<II',len(js),0x4e4f534a)+js+struct.pack('<II',len(binary),0x004e4942)+binary
class Contracts(unittest.TestCase):
 def test_valid_bvh(self):self.assertEqual(bvh_contract(bvh())['mappedRequired'],22)
 def test_bone_order(self):self.assertEqual(bvh_contract(bvh([REQUIRED[0]]+list(reversed(REQUIRED[1:]))))['joints'],22)
 def test_bvh_truncated(self):self.assertRaises(Invalid,bvh_contract,bvh().rsplit('\n',2)[0])
 def test_bvh_corrupt(self):self.assertRaises(Invalid,bvh_contract,bvh().replace('Frame Time:','Broken:'))
 def test_missing_joint(self):self.assertRaises(Invalid,bvh_contract,bvh(REQUIRED[:-1]))
 def test_units(self):self.assertRaises(Invalid,bvh_contract,bvh(),'cm')
 def test_outlier(self):self.assertRaises(Invalid,bvh_contract,bvh().replace('OFFSET 0 1 0','OFFSET 0 999999 0'))
 def test_nan(self):self.assertRaises(Invalid,bvh_contract,bvh().replace('OFFSET 0 1 0','OFFSET 0 nan 0'))
 def test_valid_glb(self):self.assertEqual(glb_contract(glb())['bones'],80)
 def test_glb_truncated(self):self.assertRaises(Invalid,glb_contract,glb()[:-4])
 def test_source_action(self):self.assertRaises(Invalid,glb_contract,glb(lambda d:d['animations'].append({'name':'source-14_06'})))
 def test_empty_animation(self):self.assertRaises(Invalid,glb_contract,glb(lambda d:d['animations'][0].update(channels=[])))
 def test_incompatible_rig(self):self.assertRaises(Invalid,glb_contract,glb(lambda d:d['skins'][0].update(joints=[0])))
 def test_accessor_incomplete(self):self.assertRaises(Invalid,glb_contract,glb(lambda d:d['accessors'][1].update(count=100)))
 def test_difference(self):self.assertRaises(Invalid,compare_positions,[{'a':[0,0,0]}],[{'a':[0,.1,0]}])
 def test_order_invariance(self):self.assertEqual(compare_positions([{'a':[0,0,0],'b':[1,0,0]}],[{'b':[1,0,0],'a':[0,0,0]}]),0)
 def test_no_input(self):self.assertRaises(Invalid,validate,{'units':'m','up':'Y','frames':[]},C)
 def test_wrong_axes(self):self.assertRaises(Invalid,validate,{'units':'cm','up':'Z'},C)
if __name__=='__main__':unittest.main()
