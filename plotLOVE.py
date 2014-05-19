import numpy as np
import cPickle as pickle
from numpy.random import rand
from inferMULT import plsa_multi

f = open('nagi_evi', "r")
Nd = pickle.load(f)
Nu = pickle.load(f)
Nw = pickle.load(f)
Nud = pickle.load(f)
Nwd = pickle.load(f)
actor_name = pickle.load(f)
user_name = pickle.load(f)
f.close()

'''
f = open('nagi_inf', "r")
Pz_d = pickle.load(f)
Pu_z = pickle.load(f)
Pw_z = pickle.load(f)
Pd   = pickle.load(f)
Pz_u = pickle.load(f)
f.close()
'''

iteration = 200
Nz = 5
Nep =26
alpha = [10   for _ in range(Nep)]
beta  = [1    for _ in range(Nep)]
Pz_d,Pu_z,Pw_z,Pd,Pz_u = plsa_multi([Nd,Nu,Nw,Nud,Nwd,Nep],[alpha,beta],Nz,iteration)

from pylab import *
print np.shape(Pz_u)

Puz = np.sum(Pz_u,2)
pcolor(Puz.dot(Puz.T))
#pcolor(Puz)
print np.sum(Puz,1)
colorbar()
show()