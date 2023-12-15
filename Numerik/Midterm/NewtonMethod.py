import math
import matplotlib.pyplot as plt
import numpy as np

plt.axis((0.4,0.6, 30, 45))

# the function f
def f(x):
    #that's the iterative function
    return x-0.5*(math.cos(x/2)- abs(x-0.5))

# the derivative of f
def dev_f(x):
    return 1-0.5*(0.5*math.sin(x/2)-1)


def NewtonMethod(x,n):
    i=0
    if x == 0.5:
        return
    x0=x - f(x)/dev_f(x)
    while abs(x-x0)>n:
        if x == 0.5:
            x = x - f(x)/dev_f(x0)
        else:
            x0=x
            x = x - f(x)/dev_f(x)
            i+=1
    return [x,i]

print(NewtonMethod(0.45,0.5*10**(-10))[0])
for i in range(1,100):
    if 0.001*i!= 0.05:
        L=NewtonMethod(0.45+0.001*i,0.5*10**(-10))
        plt.scatter(0.45+0.001*i,L[1])


plt.show()

# excersise 4
# part 4
#   The probplem is that the derivative at x=0.5 does not exist.
#   in case we have x=5 we can't calculate the derivative of f at x=0.5. What we can do instead
#   of calculating dev_f(x_n), we can take x_n-1 and use the derivative of that value instread.
#   This might increase the number of iterations we need, but we will recive the correct result.