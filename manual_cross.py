from itertools import product, islice,chain
import pandas as pd
from collections import Counter

def crossover_gametes(l):
    c=[]
    k = list(product(*l))
    for i in k:
        c.append(list(i))
    return c
def gamete_isolate(x):
    if x.isalpha()==True:
        temp=[]
        output2 = list(x)
        temp.append(output2[:int(len(output2)/2)])
        temp.append(output2[int(len(output2)/2):])
        return sorted(temp)
    elif x.isalnum() == True:
        temp=[]
        res=[]
        c=[]
        temp.append(x[:int(len(x)/2)])
        temp.append(x[int(len(x)/2):])
        for i in temp:
            for k in range(0, len(i)-1,2):
                res.append(i[k:k+2])
            c.append(res)
            res=[]
        return sorted(c)
def arrange_traits(x):
    x1=x[0]
    x2=x[1]
    temp=[]
    x3=[]
    for i in range(0, len(x1)):
        temp.append(x1[i])
        temp.append(x2[i])
        x3.append(temp)
        temp=[]
    return sorted(x3)
def progeny(k):
    c=[]
    for i in k:
        for j in k:
            c.append(''.join(sorted(i+j)))
    return c
def occurence(h):
    temp = dict(Counter(i for i in h))
    lf=[]
    for i in range(1, len(list(temp.keys()))+1):
        lf.append(i)
    data = pd.DataFrame(data = {'Offsprings': list(temp.keys()), 'Occurence': list(temp.values())}, index = lf)
    return data
def self_cross(k):
    return occurence(progeny(crossover_gametes(arrange_traits(gamete_isolate(k)))))
def parental_cross(a,b):
    #print(a,b)
    p1 = arrange_traits(gamete_isolate(a))
    p2 = arrange_traits(gamete_isolate(b))
    #print(p1,p2)
    gam = list(product(*p1))
    gam1 = []
    for i in gam:
        gam1.append(i)
    gam=[]
    gam = list(product(*p2))
    gam2 = []
    for i in gam:
        gam2.append(i)
    t = []
    for i in gam1:
        for j in gam2:
            t.append(''.join(i+j))
    return t
c = []
population = ['ABCDEFGHIabcdefghi']
fr = []
f = []
for i in population:
    fr.append(list(i))
f = list(chain(*fr))
k1 = 0
k2 = 0
k=0
for i in f:
    if i == 'B':
        k1+=1
        k+=1
    if i == 'b':
        k2+=1
        k+=1
print((k1/k)+(k2/k))
for i in population:
    for j in population:
        #print(parental_cross(i,j))
        for k in parental_cross(i,j):
            #print(self_cross(k))
            c.append(progeny(crossover_gametes(arrange_traits(gamete_isolate(k)))))
#print(c)
t1=0
t2=0
t3=0
t4=0
for i in c:
    for j in i:
        t4+=1
        if ('B' in j) & ('b' not in j):
            t1+=1
        if ('B' in j) & ('b' in j):
            t2+=1
        if ('b' in j) & ('B' not in j):
            t3+=1
#print(t1, t2, t3)
print((t1/t4)+(t2/t4)+(t3/t4))
