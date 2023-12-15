import math
import matplotlib.pyplot as plt
import numpy as np

plt.axis((0.4,0.6, 15, 30))

def f(x):
    #that's the iterative function
    return 0.5*(math.cos(x/2)-abs(x-0.5))


def FixedPointIteration(x,n):
    #i denotes the number of iterations
    i=0
    while abs(0.4722515914-f(x))>(0.568/(1-0.568))*abs(f(x)-x) or (0.568/(1-0.568))*abs(f(x)-x)>n:
        x=f(x)
        #print(abs(0.4722515914-f(x)),">",(0.45/(1-0.45))*abs(f(x)-x))

        i+=1
    return [x,i]


print(FixedPointIteration(0.45,0.5*10**(-10))[0])
    

for i in range(1,100):
    L = FixedPointIteration(0.45+0.001*i,0.5*10**(-10))
    #print("hey")
    plt.scatter(0.45+0.001*i,L[1])


plt.show()
