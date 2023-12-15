import numpy as np
import math
import matplotlib.pyplot as plt
from tabulate import tabulate



def f(x,t):
    return -2*t*x**2
def u(t):
    return 1/(1+t**2)

h = 0.25
t = 0
x=1
e = 5
steps=5
########################################################################
#adam bashfort (fourth order)

print('Adams-Bashforth fourth order formular')

def adams_bashforth_one_step(T, X, h, step):
    if step <=3:
        #we use the runge kutta method for the first steps
        F1 = h * f(X[step - 1],T[step - 1])
        F2 = h * f(X[step - 1] + F1/2, T[step - 1] + h/2)
        F3 = h * f(X[step - 1] + F2/2, T[step - 1] + h/2)
        F4 = h * f(X[step - 1] + F3, T[step - 1] + h)
        return X[step - 1] + (F1 + 2*F2 + 2*F3 + F4) / 6

    else:
        return X[step - 1] + h * (55 * f(X[step - 1],T[step - 1]) - 59 * f(X[step - 2],T[step - 2]) + 37 * f(X[step - 3],T[step - 3]) - 9 * f(X[step - 4],T[step - 4]))/24


def adams_bashforth(t, x, h, steps):
    T = [t]
    X = [x]

    for i in range (1,min(3, steps)+1):
        T.append( T[i - 1] + h)
        b = adams_bashforth_one_step(T,X,h,i)
        X.append(b)
    
    for i in range(4, steps):
        T.append( T[i - 1] + h)
        X.append(adams_bashforth_one_step(T,X,h,i))

    return T, X




# Calculate the numerical solution
solution = adams_bashforth(t,x,h,steps)

t_values_ab = solution[0]
x_values_ab = [round(i,e) for i in solution[1]]

# Calculate the exact solution
exact_values = [round(u(i),e) for i in t_values_ab]

#we create a table with the values
data = [[t, x, exact_values] for t, x, exact_values in zip(t_values_ab, x_values_ab, exact_values)]
headers = ["t", "x","exact"]
table = tabulate(data, headers, tablefmt="pretty")
print(table)


print(' ')
#########################################################################
#adam moulton (fourth order)
print('Adams-Moulton fourth order formular')


def adams_moulton(t, x, h, steps):
    T = [t]
    X = [x]
    #compute the values we need from the adams-bashforth formular
    x_values = [adams_bashforth_one_step(T,X,h,1)]

    for i in range (1,min(3, steps)+1):
        T.append( T[i - 1] + h)
        b=adams_bashforth_one_step(T,X,h,i)
        X.append( b)
        x_values.append(b)
    
    for i in range(4, steps):
        T.append( T[i - 1] + h)
        #here we need to use the adams bashforth formular
        x_values.append(adams_bashforth_one_step(T,X,h,i))
        X.append( X[i - 1] + h / 24 * (9 * f(x_values[i],T[i]) + 19 * f(X[i - 1], T[i - 1]) - 5 * f(X[i - 2],T[i - 2]) + f(X[i - 3],T[i - 3])))

    return T, X

# Calculate the numerical solution
solution = adams_moulton(t,x,h,steps)

t_values_am = solution[0]
x_values_am = [round(i,e) for i in solution[1]]

# Calculate the exact solution
exact_values = [round(u(i),e) for i in t_values_am]

#we create a table with the values
data = [[t, x, exact_values] for t, x, exact_values in zip(t_values_am, x_values_am, exact_values)]
headers = ["t", "x","exact"]
table = tabulate(data, headers, tablefmt="pretty")
print(table)

print(' ')
###########################################################################
#Runge Kutta
print('Runge Kutta method')

def runge_kutta(M,t,x,h):
    ret=[]
    e=abs(u(t )-x)
    ret.append([0,t,x,e])
    for k in range (1,M):
        F1 = h* f(x,t)
        F2 = h* f(x+F1/2,t+h/2)
        F3 = h* f(x+F2/2,t+h/2)
        F4 = h* f(x+F3,t+h)
        x= x+ (F1+2*F2+2*F3+F4)/6
        t=t+h
        e=abs(u(t )-x)
        ret.append([k,t,x,e])

    return ret  


# Calculate the numerical solution
solution = runge_kutta(steps,t,x,h )

t_values_rk = [i[1] for i in solution]
x_values_rk = [round(i[2],5) for i in solution]

# Calculate the exact solution
exact_values = [round(u(i),e) for i in t_values_rk]

#we create a table with the values
data = [[t, x, exact_values] for t, x, exact_values in zip(t_values_rk, x_values_rk, exact_values)]
headers = ["t", "x","exact"]
table = tabulate(data, headers, tablefmt="pretty")
print(table)


#####################################################################
#Errors
error_am=[]
error_rk=[]
for i in range(0, len(exact_values)):
    error_am.append(round(abs(x_values_am[i]-exact_values[i]),5))
    error_rk.append(round(abs(x_values_rk[i]-exact_values[i]),5))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_values_am, error_am, label='Error Adams-Moulton method')
plt.plot(t_values_rk, error_rk, label='Error Runge Kutta method',linestyle='--')
plt.xlabel('t')
plt.ylabel('x')
plt.title('Runge-Kutta Method for Differential Equation')
plt.legend()
plt.grid(True)
plt.show()