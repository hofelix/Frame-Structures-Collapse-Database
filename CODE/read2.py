import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

input = np.genfromtxt('C:/Users/USER/Desktop/OUTPUT/OUTPUT2/all.csv')
input = np.reshape(input,(1000,18))
#fo = open("C:/Users/USER/Desktop//OUTPUT/OUTPUT3/nor.txt", "w" )

data = []
#print(-input[:,14])
for i in range(0,18):
    mean = np.mean(input[:,i])
    #print(mean)
    std = np.std(input[:,i])
    #print(std)
    nor = (-input[:,i] - mean)/std
    nor = (nor - np.min(nor))/(np.max(nor) - np.min(nor))
    #print(nor[21])
    data.append(nor)
data = np.reshape(data,(1000,18))
#data = list(data)
#fo.write( str(data) )
#print(data[:,0])
disout = 0.233*data[:,0]+0.233*data[:,1]+0.15*data[:,2]+0.233*data[:,3]+0.15*data[:,4]
disin = data[:,5]
cosout = 0.233*data[:,6]+0.233*data[:,7]+0.15*data[:,8]+0.233*data[:,9]+0.15*data[:,10]
cosin = data[:,11]
curout = 0.233*data[:,12]+0.233*data[:,13]+0.15*data[:,14]+0.233*data[:,15]+0.15*data[:,16]
curin = data[:,17]
#print(cosin[1])
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure()
x0 = np.arange(1,1000)
x1 = np.arange(2)

def reg(x,y):
    coefficients = np.polyfit(x,y,1) # 利用 polyfit 幫我們算出資料 一階擬合的 a, b 參數
    p = np.poly1d(coefficients) # 做出公式, print 的結果是 coefficients[0] * X + coefficients[1]
    #r = r2_score(y, p(x)) # 計算相關係數用，這裡沒有用到
    r = np.corrcoef(x,y)
    return coefficients, p ,r[0,1]

(arg1, arg2), text1 ,coe = reg(curin,curout)
#print(coe)
trend_line = arg1*x1 + arg2
#print(y)#圖表的設定散佈圖
plt.title("COS相似度")
#ax.legend('beam column','wall')
plt.xlabel('in')
plt.ylabel('out')
#plt.xlim(left=-0, right=1)
#plt.ylim(bottom=-0, top=1)
n = np.arange(1000)
#print(n)
#for i,txt in enumerate(n):
#    plt.annotate(txt,(cosin[i],cosout[i]))
plt.text(0.7,0.1,text1,fontsize=10)
plt.text(0.7,0.05,coe,fontsize=10)
plt.scatter(curin, curout,color = 'red')
plt.plot(trend_line)
#plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
#plt.legend([plot1],['beam column'])
plt.show()

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
