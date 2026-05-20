import numpy as np


input = np.genfromtxt ('C:/Users/USER/Desktop/inform250.csv', delimiter=",")
xy = np.array(input[20:24,1:3])
xz = np.array(input[20:24,2:4])
#print(xz)

x_t = np.gradient(xy[:, 0])
y_t = np.gradient(xy[:, 1])

u_t = np.gradient(xz[:,0])
v_t = np.gradient(xz[:,1])
vel = np.array([ [x_t[i], y_t[i]] for i in range(x_t.size)])
vel2 = np.array([ [u_t[j], v_t[j]] for j in range(u_t.size)])
#print(vel)
speed = np.sqrt(x_t * x_t + y_t * y_t)
speed2 = np.sqrt(u_t * u_t + v_t * v_t)
#print(speed)
tangent = np.array([1/speed] * 2).transpose() * vel
tangent2 = np.array([1/speed2] * 2).transpose() * vel2
#print(tangent)
ss_t = np.gradient(speed)
xx_t = np.gradient(x_t)
yy_t = np.gradient(y_t)

ss2_t = np.gradient(speed2)
xx2_t = np.gradient(u_t)
yy2_t = np.gradient(v_t)
curvature_val = np.abs(xx_t * y_t - x_t * yy_t) / (x_t * x_t + y_t * y_t)**1.5
curvature_val2 = np.abs(xx2_t * v_t - u_t * yy2_t) / (u_t * u_t + v_t * v_t)**1.5
print(np.argmax(curvature_val),np.argmax(curvature_val2))
