from parseSUB import parseNud
from parseXML import parseNwd
import cPickle as pickle
import parseEQU
import numpy as np

def save_evi(outname):
	f = open(outname, "w")
	pickle.dump(Nd, f)
	pickle.dump(Nu, f)
	pickle.dump(Nw, f)
	pickle.dump(Nud, f)
	pickle.dump(Nwd, f)
	pickle.dump(actor_name, f)
	f.close()

def load_evi(inname):
	f = open(inname, "r")
	Nd = pickle.load(f)
	Nu = pickle.load(f)
	Nw = pickle.load(f)
	Nud = pickle.load(f)
	Nwd = pickle.load(f)
	actor_name = pickle.load(f)
	f.close()


inpath='subinfo/nagi_*.srt'
Nep = 26
Equ = parseEQU.nagi
Nud,Nu,Nd, actor_name= parseNud(inpath,Nep,Equ)
print Nu,Nd
print actor_name
print np.shape(Nud[0]),np.shape(Nud[-1])



inpath = 'comment/nagi_comment (*).xml'
Nep = 26
Nwd,Nw,Nd,user_name = parseNwd(inpath,Nep)
print Nw,Nd,sum(Nw)
print np.shape(Nwd[0]),np.shape(Nwd[-1])


save_evi('nagi')
load_evi('nagi')

