import numpy as np
import cPickle as pickle
from numpy.random import rand
from inferMULT import plsa_multi
from inferMULT import ksum
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

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
redo = 3
sigma = 6
weight = 1

mean1 = 6#6
mean2 = 20#20

love1 = np.zeros([7,7])
love2 = np.zeros([7,7])

for i in range(redo):
	alpha1 = [weight*mlab.normpdf(j,mean1,sigma) for j in range(Nep)]
	beta1  = [       mlab.normpdf(j,mean1,sigma) for j in range(Nep)]
	Pz_d,Pu_z,Pw_z,Pd,Pz_u = plsa_multi([Nd,Nu,Nw,Nud,Nwd,Nep],[alpha1,beta1],Nz,iteration)
	Puz = np.sum(Pz_u,2)
	love1 += Puz.dot(Puz.T)



for i in range(redo):
	alpha2 = [weight*mlab.normpdf(j,mean2,sigma) for j in range(Nep)]
	beta2  = [       mlab.normpdf(j,mean2,sigma) for j in range(Nep)]
	Pz_d,Pu_z,Pw_z,Pd,Pz_u = plsa_multi([Nd,Nu,Nw,Nud,Nwd,Nep],[alpha2,beta2],Nz,iteration)
	Puz = np.sum(Pz_u,2)
	love2 += Puz.dot(Puz.T)
plt.figure(1)

plt.subplot(131)
plt.pcolor(love1/redo)
plt.colorbar()

plt.subplot(132)
plt.pcolor(love2/redo)
plt.colorbar()

plt.subplot(133)
plt.plot(np.array([alpha1,alpha2]).T)


plt.show()



