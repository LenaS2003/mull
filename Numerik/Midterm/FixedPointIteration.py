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
    while abs(f(x)-x)>n:
        x=f(x)

        i+=1
    return [x,i]



#for i in range (-100,100):
#    L = FixedPointIteration(i,0.5*10**(-10))
#    plot1.scatter(i,L[1])


# Problem 4
# part 2
#   x = 0.4722515913
#   from part 1) we already know that [0.45,0.55] is contractive, so my initial guess would be
#   to start in that interval:
#   Theorem 1 of the book on page 102 states that if T is a contactive mapping og C into C,
#   than F has a unique fixed point. So we know about the existence of the fixed point. Moreover
#   we know that if we start in C that the limes of the fixedpoint iteration is that fixed point.
#   So if we start in [0.45,0.55] than our sequence has a limes and that limes is the searched point


#part 4
#q = 0.45
for i in range(1,100):
    L = FixedPointIteration(0.45+0.001*i,0.5*10**(-10))
    plt.scatter(0.45+0.001*i,L[1])


plt.show()