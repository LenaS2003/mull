import math

def f(x):
    return 5*x-1

def limes(n, min, max,r):
    i=0
    while i<=n:
        if f(min)*f(max)<0:
            d=(min+max)/2
            if d==r:
                print("We found the root")
                break
            elif f(min)*f(d)<=0:
                max = d
            elif f(d)*f(max)<=0:
                min = d
            #print("d", d)
            #print(abs(r-(min+max)/2)/abs(r-d))
            print((d-r)*2**i)
        else:
            print("either max or min is a root or there is no root")
            break
        i+=1


limes(100,0,2,1/5)
#print(f(0))
#print(f(3))