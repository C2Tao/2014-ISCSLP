import numpy as np
import cPickle as pickle
from numpy.random import rand
f = open('nagi', "r")
Nd = pickle.load(f)
Nu = pickle.load(f)
Nw = pickle.load(f)
Nud = pickle.load(f)
Nwd = pickle.load(f)
actor_name = pickle.load(f)
f.close()


print Nd,Nu,Nw

import numpy as np
def ksum(A,dim):
    try:    return np.sum(A,dim,keepdims=True)
    except: return np.expand_dims(np.sum(A,dim),dim)


iteration = 100
Nz = 20
Nep = 26

#dimension order Nw->Nz->Nd
#dimension order Nu->Nz->Nd

b = 0.00001
alpha = [10 for _ in range(Nep)]
beta  = [1  for _ in range(Nep)]

#Initialization
Pud    = [np.expand_dims(Nud[i],1)+b for i in range(Nep)]
Pwd    = [np.expand_dims(Nwd[i],1)+b for i in range(Nep)]
Pz_ud  = [rand(Nu   ,Nz,Nd)+b        for i in range(Nep)]
Pz_wd  = [rand(Nw[i],Nz,Nd)+b        for i in range(Nep)]

Pz_d   = [rand(1,Nz,Nd)+b            for i in range(Nep)]
Pu_z   = rand(Nu,Nz, 1)+b
Pw_z   = [rand(Nw[i],Nz, 1)+b        for i in range(Nep)]
Pd     = [rand( 1, 1,Nd)+b           for i in range(Nep)]

#Normalization
for i in range(Nep):
    Pud[i]   /= ksum(ksum(Pud[i],0),2)
    Pwd[i]   /= ksum(ksum(Pwd[i],0),2)
    Pz_ud[i] /= ksum(Pz_ud[i],1) 
    Pz_wd[i] /= ksum(Pz_wd[i],1) 

    Pz_d[i]  /= ksum(Pz_d[i],1) 
    Pu_z     /= ksum(Pu_z   ,0) 
    Pw_z[i]  /= ksum(Pw_z[i],0) 
    Pd[i]    /= ksum(Pd[i],2) 

for __ in range(iteration):
    print __
    #Expectaion
    for i in range(Nep):
        Pz_ud[i]  = Pu_z    * Pz_d[i] * Pd[i]
        Pz_wd[i]  = Pw_z[i] * Pz_d[i] * Pd[i]
        Pz_ud[i] /= ksum(Pz_ud[i],1) 
        Pz_wd[i] /= ksum(Pz_wd[i],1) 
    #Maximization


    Puzd = [Pud[i]*Pz_ud[i]*alpha[i] for i in range(Nep)]
    Pwzd = [Pwd[i]*Pz_wd[i]*beta [i] for i in range(Nep)]   
    #Puzd = [[] for i in range(Nep)]
    #Pwzd = [[] for i in range(Nep)]
    #for i in range(Nep):
    #    Puzd[i] = Pud[i]*Pz_ud[i]*alpha[i]
    #    Pwzd[i] = Pwd[i]*Pz_wd[i]*beta [i]


    Pz_d = [ksum(Puzd[i],0)+ksum(Pwzd[i],0) for i in range(Nep)]
    Pz_d = [Pz_d[i]/ksum(Pz_d[i],1)         for i in range(Nep)]
    #Pz_d = [np.zeros(np.shape(Pz_d[i])) for i in range(Nep)]    
    #for i in range(Nep):
    #    Pz_d[i]  += ksum(Puzd[i],0)
    #    Pz_d[i]  += ksum(Pwzd[i],0)
    #    Pz_d[i]  /= ksum(Pz_d[i],1)         
    

    Pu_z = ksum(Puzd[i],2)
    Pu_z /= ksum(Pu_z,0) 
    #Pu_z = np.zeros(np.shape(Pu_z))    
    #for i in range(Nep):
    #    Pu_z     += ksum(Puzd[i],2)
    #Pu_z     /= ksum(Pu_z   ,0) 
    

    Pw_z = [ksum(Pwzd[i],2)          for i in range(Nep)]
    Pw_z = [Pw_z[i]/ksum(Pw_z[i],0)  for i in range(Nep)]
    #for i in range(Nep):
    #    Pw_z[i] = ksum(Pwzd[i],2)
    #    Pw_z[i]/= ksum(Pw_z[i],0)


from pylab import *
print np.shape(Pu_z)
ax = plot(np.sum(Pu_z,2).T)
legend(ax,actor_name)
show()
