import math


def f(x):
    #function
    return math.exp(x)-x**2


def ridders_method(x0, x2):
    for i in range(0,1000):
        x1 = (x0+x2)/2
        x = -1
        if f(x0):
            x =1 
        #h = ((f(x1)-x*math.sqrt(f(x1)**2-f(x0)*f(x2)))/f(x2))**(2/(x2-x0))
        x3= x1 + (x1-x0)*(x*f(x1))/math.sqrt(f(x1)**2-f(x0)*f(x2))
        if f(x1)*f(x3)<0:
            x2 = x3
            x0 = x1
        elif f(x0)*f(x3)<0:
            x2 = x3
        elif f(x2)*f(x3)<0:
            x0 = x3
    return x3 


print(ridders_method(-1,0))