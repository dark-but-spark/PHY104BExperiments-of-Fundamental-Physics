import pandas as pd
import numpy as np
import math
import os

df = pd.read_csv('data.csv',index_col=0,header=0)
a=[0]*10
b=[0]*10
k=0
for i in df.index:
    for j in df.columns:
        a[k]+=df.loc[i][j]/5.0
    k+=1
   
k=0
for i in df.index:
    for j in df.columns:
        b[k]+=(df.loc[i][j]-a[k])**2/20.0
    k+=1
print(a)
for i in range(3):
    b[i]=b[i]**0.5
print(b)
