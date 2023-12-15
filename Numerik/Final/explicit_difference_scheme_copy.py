import numpy as np
import math
from matplotlib import pyplot as plt

def u_initial(x, t):
    print("x=",x)
    if t == 0 and 0 <= x <= 0.5:
        return x
    elif t == 0 and 0.5 < x <= 1:
        return 1 - x
    elif x == 0 or x == 1:
        return 0

def explicit_difference_scheme(x, t, delta_x, delta_t, D):
    # Initialization
    print(" ")
    U = np.zeros((len(t), len(x)))
    for k in range(len(x)):
        U[0, k] = u_initial(x[k], 0)
        print(U[0,k])

    # Calculate other values of the matrix
    S = D * (delta_t) / ((delta_x) ** 2)
    for i in range(1, len(t)):
        for j in range(1, len(x) - 1):
            U[i, j] = S * (U[i - 1, j + 1] - 2 * U[i - 1, j] + U[i - 1, j - 1]) + U[i - 1, j]

    return U


def exact_solution(x, t, D):
    U = np.zeros((len(t), len(x)))
    for i in range(len(t)):
        for j in range(len(x)):
            s = 0
            for k in range(1, 14):
                s += (4 / (k * math.pi) ** 2) * math.sin(k * math.pi / 2) * math.sin(k * math.pi * x[j]) * math.exp(-D * (k * math.pi) ** 2 * t[i])
            U[i, j] = s
    return U



#we calculate our solutions
D = 0.5
delta_x = 0.1
x=[]
i=0
while i<1:
    x.append(i)
    i=i+delta_x



##############################################
#plot the errors
delta_t = 1 / 50
t = np.arange(0, 4*delta_t, delta_t)
#calculate the numerical solution
solution = explicit_difference_scheme(x, t, delta_x, delta_t, D)
#calculate the exact solution
exact = exact_solution(x,t,D)

plt.figure(figsize=(8, 5))
for target_time in t:
    #plot the numerical solution
    t_index = np.abs(t - target_time).argmin()
    plt.plot(x, np.abs(solution[t_index, :]-exact[t_index, :]), label=f't = {target_time}')

plt.xlabel('X')
plt.ylabel('Error')
plt.title('Error for Delta_t=1/50')
plt.legend()
plt.grid(True)
plt.show()


delta_t = 1 / 100
t = np.arange(0, 4*delta_t, delta_t)
#calculate the numerical solution
solution = explicit_difference_scheme(x, t, delta_x, delta_t, D)
#calculate the exact solution
exact = exact_solution(x,t,D)

plt.figure(figsize=(8, 5))
for target_time in t:
    #plot the numerical solution
    t_index = np.abs(t - target_time).argmin()
    plt.plot(x, np.abs(solution[t_index, :]-exact[t_index, :]), label=f't = {target_time}')

plt.xlabel('X')
plt.ylabel('Error')
plt.title('Error for Delta_t=1/100')
plt.legend()
plt.grid(True)
plt.show()


delta_t = 1 / 200
t = np.arange(0, 4*delta_t, delta_t)
#calculate the numerical solution
solution = explicit_difference_scheme(x, t, delta_x, delta_t, D)
#calculate the exact solution
exact = exact_solution(x,t,D)

plt.figure(figsize=(8, 5))
for target_time in t:
    #plot the numerical solution
    t_index = np.abs(t - target_time).argmin()
    plt.plot(x, np.abs(solution[t_index, :]-exact[t_index, :]), label=f't = {target_time}')

plt.xlabel('X')
plt.ylabel('Error')
plt.title('Error for Delta_t=1/200')
plt.legend()
plt.grid(True)
plt.show()

#############################################
#for delta_t=1/50
delta_t = 1 / 50
t = np.arange(0, 4*delta_t, delta_t)
#calculate the numerical solution
solution = explicit_difference_scheme(x, t, delta_x, delta_t, D)
#calculate the exact solution
exact = exact_solution(x,t,D)

plt.figure(figsize=(8, 5))
for target_time in t:
    #plot the numerical solution
    t_index = np.abs(t - target_time).argmin()
    plt.plot(x, solution[t_index, :], label=f'NS: t = {target_time}')
    plt.plot(x, exact[t_index, :], label=f'ES: t = {target_time}')

plt.xlabel('X')
plt.ylabel('U')
plt.title('Solution for Delta_t=1/50')
plt.legend()
plt.grid(True)
plt.show()

################################
#for delta_t=1/100
delta_t = 1 / 100
t = np.arange(0, 4*delta_t, delta_t)
#calculate the numerical solution
solution = explicit_difference_scheme(x, t, delta_x, delta_t, D)
#calculate the exact solution
exact = exact_solution(x,t,D)

plt.figure(figsize=(8, 5))
for target_time in t:
    #plot the numerical solution
    t_index = np.abs(t - target_time).argmin()
    plt.plot(x, solution[t_index, :], label=f'NS: t = {target_time}')
    plt.plot(x, exact[t_index, :], label=f'ES: t = {target_time}')


plt.xlabel('X')
plt.ylabel('U')
plt.title('Solution for Delta_t=1/100')
plt.legend()
plt.grid(True)
plt.show()

###################################3
#for delta_t=1/200
delta_t = 1 / 200
t = np.arange(0, 4*delta_t, delta_t)
#calculate the numerical solution
solution = explicit_difference_scheme(x, t, delta_x, delta_t, D)
#calculate the exact solution
exact = exact_solution(x,t,D)

plt.figure(figsize=(8, 5))
for target_time in t:
    #plot the numerical solution
    t_index = np.abs(t - target_time).argmin()
    plt.plot(x, solution[t_index, :], label=f'NS: t = {target_time}')
    plt.plot(x, exact[t_index, :], label=f'ES: t = {target_time}')


plt.xlabel('X')
plt.ylabel('U')
plt.title('Solution for Delta_t=1/200')
plt.legend()
plt.grid(True)
plt.show()

