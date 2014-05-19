import numpy as np
import cPickle as pickle
from numpy.random import rand

def ksum(A,dim):
    try:    return np.sum(A,dim,keepdims=True)
    except: return np.expand_dims(np.sum(A,dim),dim)

def plsa_multi(Nall,scale,Nz,iteration):
    #dimension order Nw->Nz->Nd
    #dimension order Nu->Nz->Nd
    Nd,Nu,Nw,Nud,Nwd,Nep = Nall
    alpha,beta = scale

    b = 1.0/Nd/Nu/Nep

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
        Puzd  = [Pud[i]*Pz_ud[i]*alpha[i] for i in range(Nep)]
        Pwzd  = [Pwd[i]*Pz_wd[i]*beta [i] for i in range(Nep)]   

        Pz_d  = [ksum(Puzd[i],0)+ksum(Pwzd[i],0) for i in range(Nep)]
        Pd    = [ksum(Pz_d[i],1)                 for i in range(Nep)]
        Pz_d  = [Pz_d[i]/Pd[i]                   for i in range(Nep)]

        Pu_z  = ksum(Puzd[i],2)
        Pu_z /= ksum(Pu_z,0) 

        Pw_z  = [ksum(Pwzd[i],2)          for i in range(Nep)]
        Pw_z  = [Pw_z[i]/ksum(Pw_z[i],0)  for i in range(Nep)]
    Pz_u  = ksum(Puzd[i],2)
    Pz_u /= ksum(Pz_u,1) 
    return Pz_d,Pu_z,Pw_z,Pd,Pz_u
