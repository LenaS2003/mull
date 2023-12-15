import math


def f(x):
    return x - math.tan(x)


def bisection_method(min, max, error):
    #print("minimum", min)
    #print("maximum", max)
    if max-min<error:
        return (min+max)/2
    elif f(min)==0:
        return min
    elif f(max)==0:
        return max
    elif f(min)*f(max)<0:
        d = (max+min)/2
        #print("d", d)
        if f(min)*f(d)<=0:
            return bisection_method(min,d,error)
        elif f(d)*f(max)<=0:
            return bisection_method(d,max,error)
    else:
        print("there is no root in this interval")
        return 0



x = bisection_method(1,2, 10**(-15))
print(x)
print(f(x))