import matplotlib.pyplot as plt
import numpy as np
f=open("大实验/2.in","r")
n=1200
t=[0]*n
a=[0]*n
b=[0]*n
x=[0]*n
x2=[0]*n
s=f.readline().split()
# print(s)
for i in range(n):
    # print(f.readline())
    s=f.readline().split()
    # print(s)
    a[i]=float(s[1])
    b[i]=float(s[2])
    t[i]=float(s[0])
k=a[0]
for i in range(n):
    a[i]-=k
    x[i]=np.mean(a[0:i+1])
    x2[i]=np.var(a[0:i+1])
f.close()
plt.plot(t,x,label="<X>")
plt.plot(t,x2,label="<X^2>")
plt.plot(a,b,label="a,b")
plt.xlabel("time")
plt.ylabel("value")
plt.title("mean and var")
plt.legend()
plt.show()

