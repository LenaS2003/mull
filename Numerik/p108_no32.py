import math

def f(x,q):
    i=0
    while i<1:
        x=2*x - q*x**2

        #i+=1
        #print(x)
        if (abs(x-q*x**2<10**(-100))):
            break
    return x

print(f(1, 1))