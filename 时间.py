import pandas as pd
import numpy as np
import math

def P(x,a_bar,sigma):
    return 1/(math.sqrt(2*math.pi)*sigma)*math.exp(-(x-a_bar)**2/(2*(sigma**2)))
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
pf=pd.DataFrame(a[1:n+1])
b=[0]*14
b[0]=2.76+0.03
# print("[",format(b[0]-0.03,'.2f'),",",format(b[0]+0.03,'.2f'),'],',end='')
for i in range(1,13):
    b[i]=b[i-1]+0.06
    # print("(",format(b[i]-0.03,'.2f'),",",format(b[i]+0.03,'.2f'),'],',end='')

cnt=[0]*14
for i in range(1,n+1):
    for j in range(12):
        if b[j]-0.03<a[i]<=b[j]+0.03:
            cnt[j]+=1
        if b[j]-0.03==a[i] and j==0:
            cnt[j]+=1
for i in range(12):
    print("|$(",format(b[i]-0.03,'.2f'),",",format(b[i]+0.03,'.2f'),']$|$',
          cnt[i],'$|$',format(cnt[i]/n,'.2f'),'$|$',format(cnt[i]/(n*0.06),'.2f'),'$|$',format(P(b[i],a_bar,sigma),'.2f'),'$|')

#pf.to_csv('时间.csv')
f.close()

