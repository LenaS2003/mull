import math
import matplotlib.pyplot as plt
import numpy as np

plt.axis((0.4,0.6, 25, 45))

def f(x):
    #that's the iterative function
    return 0.5*(math.cos(x/2)-abs(x-0.5))
# the derivative of f
def abs_dev_f(x):
    for i in range(0,len(x)):
        x[i]=abs(0.5*(-0.5*math.sin(x[i]/2)-1))
    return x


def FixedPointIteration(x,lam,n):
    #i denotes the number of iterations
    i=0
    x0=x
    while abs(f(x)-x)>((lam**(i+1))/(1-lam))* abs(x0-f(x0)) or ((lam**(i))/(1-lam))* abs(x0-f(x0))>n:
        x=f(x)
        i+=1
    return [x,i]




lamd=0.56789

print(FixedPointIteration(0.5,lamd,0.5*10**(-10))[0])

for i in range(1,100):
    L = FixedPointIteration(0.45+0.001*i,lamd,0.5*10**(-10))
    plt.scatter(0.45+0.001*i,L[1])


plt.show()