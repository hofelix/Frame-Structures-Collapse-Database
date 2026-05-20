import numpy as np
import math
from sympy import sin,cos,pi
from numpy import dot
from numpy.linalg import norm
import pandas as pd
import csv

input1 = np.genfromtxt ('C:/Users/user/Downloads/blender-2.79b-windows64/11.csv', delimiter=",")
input2 = np.genfromtxt ('C:/Users/user/Downloads/blender-2.79b-windows64/999.csv', delimiter=",")
d1 = np.array(input1[:,1:4])
d2 = np.array(input2[:,1:4])
#print(d1,d2)
delta = d2-d1
#print(delta)
dis = np.sqrt(np.square(delta[:,0]) + np.square(delta[:,1]) + np.square(delta[:,2]))
#print(dis)

def R(theta) :

    R_x = np.array([[1,         0,                  0                   ],
                    [0,         math.cos(theta[0]), -math.sin(theta[0]) ],
                    [0,         math.sin(theta[0]), math.cos(theta[0])  ]
                    ])



    R_y = np.array([[math.cos(theta[1]),    0,      math.sin(theta[1])  ],
                    [0,                     1,      0                   ],
                    [-math.sin(theta[1]),   0,      math.cos(theta[1])  ]
                    ])

    R_z = np.array([[math.cos(theta[2]),    -math.sin(theta[2]),    0],
                    [math.sin(theta[2]),    math.cos(theta[2]),     0],
                    [0,                     0,                      1]
                    ])


    R = np.dot(R_z, np.dot( R_y, R_x ))

    return R

cos1 = np.array(input1[:,4:7])
cos2 = np.array(input2[:,4:7])
a = [0,0,1]
data = []
for i in range(0,496):
    theta1 = cos1[i]
    theta2 = cos2[i]
    r1 = R(theta1)[:,2]
    r2 = R(theta2)[:,2]
    cos = np.dot(r1,r2)/np.sqrt((r1[0]*r1[0] + r1[1]*r1[1] + r1[2]*r1[2])*(r2[0]*r2[0] + r2[1]*r2[1] + r2[2]*r2[2]))
    data.append(cos)
data = np.reshape(data,(496,1))
#print(data)
x1_value = np.array(input1[:,1])
y1_value = np.array(input1[:,2])
z1_value = np.array(input1[:,3])
xt1 = np.gradient(x1_value)
yt1 = np.gradient(y1_value)
zt1 = np.gradient(z1_value)
xxt1 = np.gradient(xt1)
yyt1 = np.gradient(yt1)
zzt1 = np.gradient(zt1)
cur1 = np.sqrt((xxt1 * xxt1 + yyt1 * yyt1 + zzt1 * zzt1) * (xt1*xt1+yt1*yt1+zt1*zt1)-np.square(xt1*xxt1+yt1*yyt1+zt1*zzt1)) /((np.sqrt(xt1 * xt1 + yt1 * yt1+zt1*zt1)) ** 3)

x2_value = np.array(input2[:,1])
y2_value = np.array(input2[:,2])
z2_value = np.array(input2[:,3])
xt2 = np.gradient(x2_value)
yt2 = np.gradient(y2_value)
zt2 = np.gradient(z2_value)
xxt2 = np.gradient(xt2)
yyt2 = np.gradient(yt2)
zzt2 = np.gradient(zt2)
cur2 = np.sqrt((xxt2 * xxt2 + yyt2 * yyt2 + zzt2 * zzt2) * (xt2*xt2+yt2*yt2+zt2*zt2)-np.square(xt2*xxt2+yt2*yyt2+zt2*zzt2)) /((np.sqrt(xt2 * xt2 + yt2 * yt2+zt2*zt2)) ** 3)
cur = np.abs(cur2-cur1)

str_list =    str(np.sum(dis[0:12])/12) +'\n' +str((np.sum(dis[114:126])+np.sum(dis[130:142])+np.sum(dis[366:378])+np.sum(dis[382:394]))/48)+'\n'\
            + str((np.sum(dis[102:114])+np.sum(dis[146:158])+np.sum(dis[350:366])+np.sum(dis[394:406]))/72) +'\n'\
            + str((np.sum(dis[97:102])+np.sum(dis[158:168])+np.sum(dis[172:174])+dis[92])/18)+'\n'\
            + str((np.sum(dis[334:336])+np.sum(dis[340:350])+np.sum(dis[406:411])+dis[415])/18)+'\n'\
            + str((np.sum(dis[254:334])+np.sum(dis[336:340])+np.sum(dis[411:415])+np.sum(dis[416:496]))/160)+'\n'\
            + str((np.sum(dis[126:130])+np.sum(dis[378:382]))/8)+'\n'+str(np.sum(dis[142:146])/4)+'\n'\
            + str((np.sum(dis[12:92])+np.sum(dis[93:97])+np.sum(dis[168:172])+np.sum(dis[174:254]))/160)+'\n'\
            \
            + str(np.sum(data[0:12])/12) +'\n' +str((np.sum(data[114:126])+np.sum(data[130:142])+np.sum(data[366:378])+np.sum(data[382:394]))/48)+'\n'\
            + str((np.sum(data[102:114])+np.sum(data[146:158])+np.sum(data[350:366])+np.sum(data[394:406]))/72) +'\n'\
            + str((np.sum(data[97:102])+np.sum(data[158:168])+np.sum(data[172:174]))/18)+'\n'\
            + str((np.sum(data[334:336])+np.sum(data[340:350])+np.sum(data[406:411]))/18)+'\n'\
            + str((np.sum(data[254:334])+np.sum(data[336:340])+np.sum(data[411:415])+np.sum(data[416:496]))/160)+'\n'\
            + str((np.sum(data[126:130])+np.sum(data[378:382]))/8)+'\n'+str(np.sum(data[142:146])/4)+'\n'\
            + str((np.sum(data[12:92])+np.sum(data[93:97])+np.sum(data[168:172])+np.sum(data[174:254]))/160)+'\n'\
            \
            + str(np.sum(cur[0:12])/12) +'\n' +str((np.sum(cur[114:126])+np.sum(cur[130:142])+np.sum(cur[366:378])+np.sum(cur[382:394]))/48)+'\n'\
            + str((np.sum(cur[102:114])+np.sum(cur[146:158])+np.sum(cur[350:366])+np.sum(cur[394:406]))/72) +'\n'\
            + str((np.sum(cur[97:102])+np.sum(cur[158:168])+np.sum(cur[172:174])+cur[92])/18)+'\n'\
            + str((np.sum(cur[334:336])+np.sum(cur[340:350])+np.sum(cur[406:411])+cur[415])/18)+'\n'\
            + str((np.sum(cur[254:334])+np.sum(cur[336:340])+np.sum(cur[411:415])+np.sum(cur[416:496]))/160)+'\n'\
            + str((np.sum(cur[126:130])+np.sum(cur[378:382]))/8)+'\n'+str(np.sum(cur[142:146])/4)+'\n'\
            + str((np.sum(cur[12:92])+np.sum(cur[93:97])+np.sum(cur[168:172])+np.sum(cur[174:254]))/160)+'\n'

fo = open("C:/Users/USER/Desktop/OUTPUT/OUTPUT4/999.csv", "w" )
fo.write( str_list )
