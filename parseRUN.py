from parseSUB import parseNud
from parseXML import parseNwd
from inferMULT import plsa_multi
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
	pickle.dump(user_name, f)
	f.close()

def load_evi(inname):
	f = open(inname, "r")
	Nd = pickle.load(f)
	Nu = pickle.load(f)
	Nw = pickle.load(f)
	Nud = pickle.load(f)
	Nwd = pickle.load(f)
	actor_name = pickle.load(f)
	user_name = pickle.load(f)
	f.close()

def save_inf(outname):
	f = open(outname, "w")
	pickle.dump(Pz_d, f)
	pickle.dump(Pu_z, f)
	pickle.dump(Pw_z, f)
	pickle.dump(Pd,   f)
	pickle.dump(Pz_u, f)
	f.close()

def load_inf(inname):
	f = open(inname, "r")
	Pz_d = pickle.load(f)
	Pu_z = pickle.load(f)
	Pw_z = pickle.load(f)
	Pd   = pickle.load(f)
	Pz_u = pickle.load(f)
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


save_evi('nagi_evi')
load_evi('nagi_evi')

iteration = 200
Nz = 20
Nep =26
alpha = [10   for _ in range(Nep)]
beta  = [1    for _ in range(Nep)]

Pz_d,Pu_z,Pw_z,Pd,Pz_u = plsa_multi([Nd,Nu,Nw,Nud,Nwd,Nep],[alpha,beta],Nz,iteration)

save_inf('nagi_inf')
load_inf('nagi_inf')

from pylab import *
print np.shape(Pu_z)
ax = plot(np.sum(Pu_z,2).T)
legend(ax,actor_name)
show()
