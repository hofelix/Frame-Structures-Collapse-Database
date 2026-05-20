import numpy as np
import math
from sympy import sin,cos,pi
from numpy import dot
from numpy.linalg import norm
import pandas as pd
import csv

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
input2 = np.genfromtxt ('C:/Users/USER/Desktop/inform250.csv', delimiter=",")
d2 = np.array(input2[:,4:7])
a = [0,0,1]
data = []
for i in range(0,132):
    theta = d2[i]
    r = R(theta)[:,2]
    cos = np.dot(a,r)/np.sqrt(r[0]*r[0] + r[1]*r[1] + r[2]*r[2])
    data.append(cos)
data = np.reshape(data,(132,1))
print(data)
fo = open("C:/Users/USER/Desktop/test.csv", "w" )
fo.write( str(data) )
