import numpy as np
import math
from sympy import sin,cos,pi
from numpy import dot
from numpy.linalg import norm
import pandas as pd
import csv

input1 = np.genfromtxt ('C:/Users/user/Downloads/blender-2.79b-windows64/22.csv', delimiter=",")
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
for i in range(0,744):
    theta1 = cos1[i]
    theta2 = cos2[i]
    r1 = R(theta1)[:,2]
    r2 = R(theta2)[:,2]
    cos = np.dot(r1,r2)/np.sqrt((r1[0]*r1[0] + r1[1]*r1[1] + r1[2]*r1[2])*(r2[0]*r2[0] + r2[1]*r2[1] + r2[2]*r2[2]))
    data.append(cos)
data = np.reshape(data,(744,1))
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

str_list =    str(np.sum(dis[242:260])/18) +'\n' +str((np.sum(dis[102:114])+np.sum(dis[118:130])+np.sum(dis[362:374])+np.sum(dis[378:390])+np.sum(dis[614:626])+np.sum(dis[630:642]))/72)+'\n'\
            + str((np.sum(dis[90:102])+np.sum(dis[130:146])+np.sum(dis[350:362])+np.sum(dis[394:406])+np.sum(dis[598:610])+np.sum(dis[642:654]))/76) +'\n'\
            + str((np.sum(dis[345:350])+np.sum(dis[406:416])+np.sum(dis[420:422]))/21)+'\n'\
            + str((np.sum(dis[582:584])+np.sum(dis[588:598])+np.sum(dis[654:659]))/21)+'\n'\
            + str((np.sum(dis[85:90])+np.sum(dis[146:156])+np.sum(dis[160:162]))/21)+'\n'\
            + str((np.sum(dis[0:85])+np.sum(dis[156:242]))/160)+'\n'\
            + str((np.sum(dis[114:118])+np.sum(dis[374:378])+np.sum(dis[626:630]))/12)+'\n'\
            + str((np.sum(dis[390:394])+np.sum(dis[610:614]))/8)+'\n'\
            + str((np.sum(dis[260:345])+np.sum(dis[416:588])+np.sum(dis[659:744]))/320)+'\n'\
\
            + str(np.sum(data[242:260])/18) +'\n' +str((np.sum(data[102:114])+np.sum(data[118:130])+np.sum(data[362:374])+np.sum(data[378:390])+np.sum(data[614:626])+np.sum(data[630:642]))/72)+'\n'\
            + str((np.sum(data[90:102])+np.sum(data[130:146])+np.sum(data[350:362])+np.sum(data[394:406])+np.sum(data[598:610])+np.sum(data[642:654]))/76) +'\n'\
            + str((np.sum(data[345:350])+np.sum(data[406:416])+np.sum(data[420:422]))/21)+'\n'\
            + str((np.sum(data[582:584])+np.sum(data[588:598])+np.sum(data[654:659]))/21)+'\n'\
            + str((np.sum(data[85:90])+np.sum(data[146:156])+np.sum(data[160:162]))/21)+'\n'\
            + str((np.sum(data[0:85])+np.sum(data[156:242]))/160)+'\n'\
            + str((np.sum(data[114:118])+np.sum(data[374:378])+np.sum(data[626:630]))/12)+'\n'\
            + str((np.sum(data[390:394])+np.sum(data[610:614]))/8)+'\n'\
            + str((np.sum(data[260:345])+np.sum(data[416:588])+np.sum(data[659:744]))/320)+'\n'\
\
            + str(np.sum(cur[242:260])/18) +'\n' +str((np.sum(cur[102:114])+np.sum(cur[118:130])+np.sum(cur[362:374])+np.sum(cur[378:390])+np.sum(cur[614:626])+np.sum(cur[630:642]))/72)+'\n'\
            + str((np.sum(cur[90:102])+np.sum(cur[130:146])+np.sum(cur[350:362])+np.sum(cur[394:406])+np.sum(cur[598:610])+np.sum(cur[642:654]))/76) +'\n'\
            + str((np.sum(cur[345:350])+np.sum(cur[406:416])+np.sum(cur[420:422]))/21)+'\n'\
            + str((np.sum(cur[582:584])+np.sum(cur[588:598])+np.sum(cur[654:659]))/21)+'\n'\
            + str((np.sum(cur[85:90])+np.sum(cur[146:156])+np.sum(cur[160:162]))/21)+'\n'\
            + str((np.sum(cur[0:85])+np.sum(cur[156:242]))/160)+'\n'\
            + str((np.sum(cur[114:118])+np.sum(cur[374:378])+np.sum(cur[626:630]))/12)+'\n'\
            + str((np.sum(cur[390:394])+np.sum(cur[610:614]))/8)+'\n'\
            + str((np.sum(cur[260:345])+np.sum(cur[416:588])+np.sum(cur[659:744]))/320)+'\n'

fo = open("C:/Users/USER/Desktop/OUTPUT/OUTPUT6/999.csv", "w" )
fo.write( str_list )
