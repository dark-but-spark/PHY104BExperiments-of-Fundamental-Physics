import pandas as pd
import numpy as np
import os

df = pd.read_csv('data.csv',index_col=0,header=0)

df1=df.mean(axis=1)
df2=df.std(axis=1)
df['std'] = df2
df['mean'] = df1
print(df1)