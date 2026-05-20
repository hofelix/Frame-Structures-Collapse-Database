import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def R(x_value: np.ndarray, y_value: np.ndarray, z_value: np.ndarray):
    xt = np.gradient(x_value)
    yt = np.gradient(y_value)
    zt = np.gradient(z_value)
    xxt = np.gradient(xt)
    yyt = np.gradient(yt)
    zzt = np.gradient(zt)
    r1 = np.sqrt((xxt * xxt + yyt * yyt + zzt * zzt) * (xt*xt+yt*yt+zt*zt)-np.square(xt*xxt+yt*yyt+zt*zzt)) /((np.sqrt(xt * xt + yt * yt+zt*zt)) ** 3)
    return r
def R2(x_value: np.ndarray, y_value: np.ndarray, z_value: np.ndarray):
    xt = np.gradient(x_value)
    yt = np.gradient(y_value)
    zt = np.gradient(z_value)
    xxt = np.gradient(xt)
    yyt = np.gradient(yt)
    zzt = np.gradient(zt)
    r2 = np.sqrt(np.square(yt * zzt - zt * yyt) +np.square(zt*xxt-xt*zzt)+np.square(xt*yyt-xxt*yt)) /((np.sqrt(xt * xt + yt * yt+zt*zt)) ** 3)
    return r2

input = np.genfromtxt ('C:/Users/USER/Desktop/inform250.csv', delimiter=",")

if __name__ == '__main__':
    x = np.array(input[:,1])
    y = np.array(input[:,2])
    z = np.array(input[:,3])
    #print(x[1],x)
    wcur1 = (R1(x[4:8], y[4:8], z[4:8])+R1(x[8:12], y[8:12], z[8:12])+R1(x[12:16], y[12:16], z[12:16])+R1(x[16:20], y[16:20], z[16:20]))/4

    bcur1 = (R1(x[20:24],y[20:24],z[20:24])+R1(x[24:28],y[24:28],z[24:28])+R1(x[28:32],y[28:32],z[28:32])+R1(x[32:36],y[32:36],z[32:36]))/4

    ccur1 = R1(x[36:39],y[36:39],z[36:39])+R1(x[43:46],y[43:46],z[43:46])/2

    scur1 =  R1(x[52:132],y[52:132],z[52:132])

    print(np.argmax(wcur1),np.argmax(wcur2),np.argmax(bcur1),np.argmax(bcur2),np.argmax(ccur1),np.argmax(ccur2),np.argmax(scur1),np.argmax(scur2))
