import xml.etree.ElementTree as ET
import sys
import numpy as np


def parseNwd(inpath,Nep):
    maxminute = 0
    for i in range(Nep):
        tree = ET.parse(inpath.split('*')[0]+str(i+1)+inpath.split('*')[1])
        root = tree.getroot()

        for child in root.iter('chat'):
            try:      minute = int(child.get('leaf'))
            except:   minute = 0
            if minute>maxminute:
                maxminute = minute



    Nd = maxminute+1
    Nw = [0 for i in range(Nep)]
    Nwd = [[] for i in range(Nep)]
    idx2user = [[] for i in range(Nep)]


    for i in range(Nep):
        tree = ET.parse(inpath.split('*')[0]+str(i+1)+inpath.split('*')[1])
        root = tree.getroot()
        user_id = {}
        for child in root.iter('chat'):
            user_id[child.get('user_id')] = []
        Nw[i] = len(user_id)
        Nwd[i] = np.zeros([Nw[i],Nd])

        
        for child in root.iter('chat'):
            idx2user[i] += child.get('user_id'),
        idx2user[i] = list(set(idx2user[i]))

        spike = []
        spikeval ={}
        for child in root.iter('chat'):
            comment = child.text
            if not comment:
                lenval = 0
            else:
                lenval = len(comment)
                counts = dict((x, comment.count(x)) for x in comment)
            userid = idx2user[i].index(child.get('user_id'))
            try:
                minutes = int(child.get('leaf'))
            except:
                minutes = 0
            Nwd[i][userid][minutes] = lenval
    return Nwd,Nw,Nd,idx2user
'''
inpath = 'comment/nagi_comment (*).xml'
Nep = 26
Nwd,Nw,Nd,user_name = parseNdw(inpath,Nep)
print Nw,Nd,sum(Nw)
print np.shape(Nwd[0]),np.shape(Nwd[-1])
'''
