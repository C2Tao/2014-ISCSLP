import sys
import parseEQU
import numpy as np

def parseNdu(inpath,Nep,Equ):
    maincast = []
    allcount = []
    maxminute = 0
    for i in range(Nep):
        actorid = []
        counts = {}
        intext = inpath.split('*')[0]+"{:02}".format(i+1)+inpath.split('*')[1]
        lines = open(intext).readlines()
        for line in lines:
            if line.split(':')[0]=='Dialogue'\
            and len(line.split()[1].split(','))>=5:
                actor = line.split()[1].split(',')[4]
                actorid += actor,
                mints = int(line.split()[1].split(',')[1].split(':')[1])
                if mints>maxminute:
                    maxminute = mints
        counts = dict((x, actorid.count(x)) for x in actorid)
        allcount += actorid
        actorid = list(set(actorid))
    counts = dict((x, allcount.count(x)) for x in allcount)
    actorid = sorted(counts.keys(), key=lambda x: counts[x],reverse=True)
    #print len(actorid),actorid

    actoreq={}
    i=0
    for ls in Equ: 
        for ac in ls:
            actoreq[ac]=i
        i+=1
    Nw = i    
    Nd = maxminute+1

    #print actoreq
    #print Nd,Nw

    Ndw = [np.zeros([Nd,Nw]) for i in range(Nep)]
    for i in range(Nep):
        intext = inpath.split('*')[0]+"{:02}".format(i+1)+inpath.split('*')[1]
        lines = open(intext).readlines()
        for line in lines:
            if line.split(':')[0]=='Dialogue' and len(line.split()[1].split(','))>=5 \
            and line.split()[1].split(',')[4] in actorid:
                actor = line.split()[1].split(',')[4]
                aid = actoreq[actor]


                wdlen = len(line.split()[1:])
                mints = int(line.split()[1].split(',')[1].split(':')[1])
                Ndw[i][mints][aid]=wdlen
    return Ndw,Nd,Nw,[eq[0] for eq in Equ]

inpath='subinfo/nagi_*.srt'
Nep = 26
Equ = parseEQU.nagi
Ndu,Nd,Nu, actor_name= parseNdu(inpath,Nep,Equ)
print Nd,Nu
print actor_name
print np.shape(Ndu[0]),np.shape(Ndu[-1])