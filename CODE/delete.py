import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import os
from os import listdir

input = np.genfromtxt('C:/Users/USER/Desktop/OUTPUT/OUTPUT4/all.csv')
input = np.reshape(input,(1000,27))
#fo = open("C:/Users/USER/Desktop//OUTPUT/OUTPUT3/nor.txt", "w" )

data = []
#print(-input[:,14])
for i in range(0,27):
    mean = np.mean(input[:,i])
    #print(mean)
    std = np.std(input[:,i])
    #print(std)
    nor = (-input[:,i] - mean)/std
    nor = (nor - np.min(nor))/(np.max(nor) - np.min(nor))
    #print(nor[21])
    data.append(nor)
data = np.reshape(data,(1000,27))
#data = list(data)
#fo.write( str(data) )
#print(data[:,0])
disout = 0.175*data[:,0]+0.175*data[:,1]+0.15*data[:,2]+0.175*data[:,3]+0.175*data[:,4]+0.15*data[:,5]
disin = 0.7*data[:,6]+0.15*data[:,7]+0.15*data[:,8]
cosout = 0.175*data[:,9]+0.175*data[:,10]+0.15*data[:,11]+0.175*data[:,12]+0.175*data[:,13]+ 0.15*data[:,14]
cosin = 0.7*data[:,15]+0.15*data[:,16]+0.15*data[:,17]
curout = 0.175*data[:,18]+0.175*data[:,19]+0.15*data[:,20]+0.175*data[:,21]+0.175*data[:,22]+0.15*data[:,23]
curin = 0.7*data[:,24]+0.15*data[:,25]+0.15*data[:,26]
list = []
list.extend([disout,disin,cosout,cosin,curout,curin])
list = np.array(list)
for m in range(0,6):
    for n in range(0,1000):
        if list[m,n]>=0.9:
            list[m,n] = 0

for ii in range(0,1000):
    sum = np.sum(list[:,ii])
    if sum == 0:
        print(str(ii))
#np.savetxt('sum.csv', total, delimiter=",")
