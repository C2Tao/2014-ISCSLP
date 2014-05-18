import numpy as np
import cPickle as pickle

f = open('nagi', "r")
Nd = pickle.load(f)
Nu = pickle.load(f)
Nw = pickle.load(f)
Ndu = pickle.load(f)
Ndw = pickle.load(f)
actor_name = pickle.load(f)
f.close()

print Nw, actor_name

import numpy as np
def ksum(A,dim):
    try:
        return np.sum(A,dim,keepdims=True)
    except:
        return np.expand_dims(np.sum(A,dim),dim)


'''
iteration = 100
Nz = 3

Nab = Ndu[0]
#dimension order Nz->Nd->Nw


[Na,Nb] = np.shape(Nab)
Nab = np.expand_dims(Nab,0)
Pa_z  = np.random.rand(Nz,Na, 1)
Pb_z  = np.random.rand(Nz, 1,Nb)
Pz    = np.random.rand(Nz, 1, 1)
Pz_ab = np.random.rand(Nz,Na,Nb)

for i in range(iteration):
    Pz_ab = Pa_z * Pb_z * Pz
    Pz_ab = Pz_ab/ksum(Pz_ab,0)

    Pzab = Nab*Pz_ab
    Pz   = ksum(ksum(Pzab,2),1)
    Pa_z = ksum(Pzab,2)/Pz
    Pb_z = ksum(Pzab,1)/Pz
    Pz   = Pz/ksum(Pz,0)

from pylab import *

plot(Pz)

show()

#print Nd,Nu
#print actor_name
#print np.shape(Ndu[0]),np.shape(Ndu[-1])
'''