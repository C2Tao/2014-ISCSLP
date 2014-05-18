from parseSUB import parseNdu
from parseXML import parseNdw
import cPickle as pickle
import parseEQU

def save_evi(outname):
	f = open(outname, "w")
	pickle.dump(Nd, f)
	pickle.dump(Nu, f)
	pickle.dump(Nw, f)
	pickle.dump(Ndu, f)
	pickle.dump(Ndw, f)
	pickle.dump(actor_name, f)
	f.close()

def load_evi(inname):
	f = open(inname, "r")
	Nd = pickle.load(f)
	Nu = pickle.load(f)
	Nw = pickle.load(f)
	Ndu = pickle.load(f)
	Ndw = pickle.load(f)
	actor_name = pickle.load(f)
	f.close()


inpath='subinfo/nagi_*.srt'
Nep = 26
Equ = parseEQU.nagi
Ndu,Nd,Nu, actor_name= parseNdu(inpath,Nep,Equ)

inpath = 'comment/nagi_comment (*).xml'
Nep = 26
Ndw,Nd,Nw,user_name = parseNdw(inpath,Nep)

save_evi('nagi')
load_evi('nagi')

