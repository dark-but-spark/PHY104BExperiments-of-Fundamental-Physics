import matplotlib.pyplot as plt
import numpy as np
f=open("大实验/5.20油滴1.in","r")
n=1200
t=[0]*n
a=[0]*n
b=[0]*n
c=[0]*n
x=[0]*n
x2=[0]*n
x3=[0]*n
s=f.readline().split()
# print(s)
for i in range(n):
    # print(f.readline())
    s=f.readline().split()
    # print(s)
    a[i]=float(s[1])*1000
    b[i]=float(s[2])
    t[i]=float(s[0])

for i in range(1,n):
    c[i]=(a[i]-a[i-1])/(t[i]-t[i-1])
    x[i]=np.mean(c[0:i+1])
    x2[i]=np.mean([(i)*(i) for i in c[0:i+1]])
    x3[i]=np.var(c[0:i+1])
f.close()
plt.plot(t,x,label="<X>")
plt.plot(t,x2,label="<X^2>")
plt.plot(t,x3,label="var")
# plt.plot(a,b,label="a,b")
plt.xlabel("time")
plt.ylabel("value")
plt.title("mean and var")
plt.legend()
plt.show()

