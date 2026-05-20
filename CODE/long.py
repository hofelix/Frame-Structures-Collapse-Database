import numpy as np



input1 = np.genfromtxt ('C:/Users/USER/Desktop/inform1.csv', delimiter=",")
input2 = np.genfromtxt ('C:/Users/USER/Desktop/inform250.csv', delimiter=",")
d1 = np.array(input1[:,1:4])
d2 = np.array(input2[:,1:4])
#print(d1,d2)
delta = d2-d1
#print(delta)
dis = np.sqrt(np.square(delta[:,0]) + np.square(delta[:,1]) + np.square(delta[:,2]))
print(dis)

str_list = 'BC' + str(dis[0:4]) +'\n' + 'W' + str(dis[4:20])  +'\n' + 'B' + str(dis[20:36]) +'\n'+ 'C' + str(dis[36:46]) +'\n'+ 'S' + str(dis[52:132])
fo = open("C:/Users/USER/Desktop/test.csv", "w" )
fo.write( str_list )
