import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

input = np.genfromtxt('C:/Users/USER/Desktop/OUTPUT/OUTPUT1/all.csv')
input = np.reshape(input,(1000,15))
#fo = open("C:/Users/USER/Desktop//OUTPUT/OUTPUT3/nor.txt", "w" )

data = []
#print(-input[:,14])
for i in range(0,15):
    mean = np.mean(input[:,i])
    #print(mean)
    std = np.std(input[:,i])
    #print(std)
    nor = (-input[:,i] - mean)/std
    nor = (nor - np.min(nor))/(np.max(nor) - np.min(nor))
#print(nor)
    data.append(nor)
data = np.reshape(data,(1000,15))
#data = list(data)
#fo.write( str(data) )
#print(data[:,0])
sum1 = data[:,0]+data[:,1]+data[:,2]+data[:,3]+data[:,4]
sum2 = data[:,5]+data[:,6]+data[:,7]+data[:,8]+data[:,9]
sum3 = data[:,10]+data[:,11]+data[:,12]+data[:,13]+data[:,14]
#print(sum2)

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure()
x0 = np.arange(1,1000)
x1 = np.arange(5)
def reg(x,y):
    coefficients = np.polyfit(x,y,1) # 利用 polyfit 幫我們算出資料 一階擬合的 a, b 參數
    p = np.poly1d(coefficients) # 做出公式, print 的結果是 coefficients[0] * X + coefficients[1]
    #coefficient_of_dermination = r2_score(y, p(x)) # 計算相關係數用，這裡沒有用到
    return coefficients, p

(arg1, arg2), text1 = reg(sum2,sum3)
#print(text2)
trend_line = arg1*x1 + arg2
#print(y)#圖表的設定散佈圖
#plt.title("餘弦相似度")
#ax.legend('beam column','wall')
plt.xlabel('餘弦相似度')
plt.ylabel('曲率相似度')
#plt.xlim(left=-0, right=1)
#plt.ylim(bottom=-0, top=1)
plt.text( 0.7,0.7,text1, fontsize=12)
plt.scatter(sum2, sum3,color = 'red')
plt.plot(trend_line)
#plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
#plt.legend([plot1],['beam column'])
#plt.show()

list = []
list.extend([sum1,sum2,sum3])
list = np.array(list)
for m in range(0,3):
    for n in range(0,1000):
        if list[m,n]>=0.9:
            list[m,n] = 0

for ii in range(0,1000):
    sum = np.sum(list[:,ii])
    if sum == 0:
        print(str(ii))
