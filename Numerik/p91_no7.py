import math

def f(x,n):
    i=0
    while i<n:
        x=x-(math.sin(x)/math.cos(x)-1)*math.cos(x)**2

        i+=1
    return x

print(f(0,100000000))