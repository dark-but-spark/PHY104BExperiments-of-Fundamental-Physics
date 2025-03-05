import pandas as pd
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt


def P(x,a_bar,sigma):
    return 1/(math.sqrt(2*math.pi)*sigma)*math.exp(-(x-a_bar)**2/(2*(sigma**2)))

matplotlib.rcParams['font.sans-serif'] = ['SimHei'] # 用黑体显示中文
f=open('时间.in','r')
n=200
a=[0]*(n+10)
mn=10
mx=0
a_bar=0
for i in range(1,n+1):
    a[i]=float(f.readline())
    mn=min(a[i],mn)
    mx=max(a[i],mx)
    a_bar+=a[i]/n
print('平均值:',a_bar)
print('最大值:',mx)
print('最小值:',mn)

sigma=sum([(a[i]-a_bar)**2 for i in range(1,n+1)])/(n-1)
sigma=sigma**0.5
print('方差:',sum([(a[i]-a_bar)**2 for i in range(1,n+1)])/(n-1))
print('标准差:',sum([(a[i]-a_bar)**2 for i in range(1,n+1)])/(n-1)**0.5)
print('极差:',mx-mn)
# pf=pd.DataFrame(a[1:n+1])
b=[0]*14
b[0]=2.76+0.03
# print("[",format(b[0]-0.03,'.2f'),",",format(b[0]+0.03,'.2f'),'],',end='')
for i in range(1,13):
    b[i]=b[i-1]+0.06
    # print("(",format(b[i]-0.03,'.2f'),",",format(b[i]+0.03,'.2f'),'],',end='')

cnt=[0]*14
p=[0]*14
sigm=[0]*4
for i in range(1,n+1):
    for j in range(1,3):
        
    for j in range(12):
        if b[j]-0.03<a[i]<=b[j]+0.03:
            cnt[j]+=1
        if b[j]-0.03==a[i] and j==0:
            cnt[j]+=1
for i in range(12):
    cnt[i]=cnt[i]/(n*0.06)#下一行输出markdown表格格式
    p[i]=P(b[i],a_bar,sigma)
   # print("|$(",format(b[i]-0.03,'.2f'),",",format(b[i]+0.03,'.2f'),']$|$',cnt[i],'$|$',format(cnt[i]/n,'.2f'),'$|$',format(cnt[i]/(n*0.06),'.2f'),'$|$',format(P(b[i],a_bar,sigma),'.2f'),'$|')

plt.bar(b[0:12],cnt[0:12],width=0.05)
plt.plot(b[0:12],p[0:12],color='red',label='正态分布曲线',marker='*')
plt.xlabel('时间/s')
plt.ylabel('概率密度/s^-1')
plt.title('概率密度直方图与正态分布曲线的对比')
plt.legend()
plt.savefig('时间.png',dpi=300)
plt.show()

#pf.to_csv('时间.csv')

f.close()

