import numpy as np
import cPickle as pickle
from numpy.random import rand
f = open('nagi', "r")
Md = pickle.load(f)
Mu = pickle.load(f)
Mw = pickle.load(f)
Mud = pickle.load(f)
Mwd = pickle.load(f)
actor_name = pickle.load(f)
f.close()

print Md,Mu,Mw



def ksum(A,dim):
    try:    return np.sum(A,dim,keepdims=True)
    except: return np.expand_dims(np.sum(A,dim),dim)

def plsa_assym(Nwd,Nz,iteration):
    #dimension order Nw->Nz->Nd
    [Nw,Nd] = np.shape(Nwd)
    b = 1.0/Nw/Nd

    #Initialization
    Pwd    = np.expand_dims(Nwd,1)+b
    Pz_wd  = rand(Nw,Nz,Nd)+b
    Pd     = rand( 1, 1,Nd)+b
    Pz_d   = rand( 1,Nz,Nd)+b
    Pw_z   = rand(Nw,Nz, 1)+b

    #Normalization
    Pwd   /= ksum(ksum(Pwd,0),2)
    Pz_wd /= ksum(Pz_wd,1) 
    Pd    /= ksum(Pd,2) 
    Pz_d  /= ksum(Pz_d,1) 
    Pw_z  /= ksum(Pw_z,0) 
    for i in range(iteration):
        #Expectaion
        Pz_wd  = Pw_z * Pz_d * Pd
        Pz_wd /= ksum(Pz_wd,1) 

        #Maximization
        Pwzd = Pwd*Pz_wd
        Pzd  = ksum(Pwzd,0)
        Pwz  = ksum(Pwzd,2)
        Pd   = ksum(Pzd,1)
        Pz   = ksum(Pzd,2)
        Pz_d = Pzd/Pd
        Pw_z = Pwz/Pz
    return Pd, Pz_d, Pw_z

iteration = 1000
Nz = 5

#Nwd = Mud[0] 
Nwd = np.concatenate((Mud[0:26]), axis=1)
#print np.sum(np.sum(Mud[0]))
#print list(Nwd.T)
Pd, Pz_d, Pw_z = plsa_assym(Nwd,Nz,iteration)
print np.shape(Nwd)
from pylab import *
#ax = plot(np.sum(Pz_d,0).T)
#ax = plot(np.sum(Pz_d,0).T)
ax = plot(np.sum(Pw_z,2).T)

legend(ax,actor_name)
show()
