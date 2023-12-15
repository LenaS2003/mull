import math
import matplotlib.pyplot as plt
import numpy as np


def f(x,t):
    return x *(1 - math.exp(t))/(math.exp(t) + 1)
def u(t):
    return 12* math.e**t/(math.e**t + 1)**2

def runge_kutta(M,t,x,h):
    ret=[]
    e=abs(u(t )-x)
    ret.append([0,t,x,e])
    for k in range (1,M):
        F1 = h* f(x,t )
        F2 = h* f(x+F1/2,t+h/2 )
        F3 = h* f(x+F2/2,t+h/2 )
        F4 = h* f(x+F3,t+h )
        x= x+ (F1+2*F2+2*F3+F4)/6
        t=t+h
        e=abs(u(t )-x)
        ret.append([k,t,x,e])
        #print(x)

    return ret    
        


#exactness
M = 200
h = -0.01  
#initial value
t = 0
x = 3



#calculate the numerical solution
solution = runge_kutta(M,t,x,h )

t_values = [i[1] for i in solution]
x_values = [i[2] for i in solution]
error_values = [i[3] for i in solution]

#calculate the exact solution
exact_values = [u(i) for i in t_values]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(t_values, x_values, label='Numerical Solution')
plt.plot(t_values, exact_values, label='Exact Solution')
plt.xlabel('t')
plt.ylabel('x')
plt.title('Runge-Kutta Method for Differential Equation')
plt.legend()
plt.grid(True)
#plt.show()

#Error
plt.figure(figsize=(10, 5))
plt.plot(t_values, error_values, label='Error')
plt.xlabel('t')
plt.ylabel('x')
plt.title('Errors of the Runge-Kutta Method')
plt.legend()
plt.grid(True)
plt.show()