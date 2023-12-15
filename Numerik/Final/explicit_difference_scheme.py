import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def u_initial(x,t):
    if t==0 and 0<=x<=0.5:
        return x
    elif t==0 and 0.5<x<=1:
        return 1-x
    elif x==0 or x==1:
        return 0
    
def explicit_difference_scheme(x,t, delta_x,delta_t,D):
    #initialisation
    U = np.zeros((len(t), len(x)))
    for k in range(0,len(x)):
        U[0,k]=u_initial(x[k],0)
    #for k in range(0,len(t)):
    #    U[0,k]=u_initial(0,t[k])
    #    U[1,k]=u_initial(1,t[k])

    U[0, :] = 0
    U[1, :] = 0

    #calculate the other values of the matrix
    S= D*(delta_t)/((delta_x)**2)
    for i in range (1,len(t)):
        for j in range(1,len(x)-1):
            U[i,j] = S*(U[i-1,j+1] - 2*U[i-1,j] + U[i-1,j-1]) + U[i-1,j]

    
    return U




D=0.5
delta_x=0.1
x=np.arange(0, 1, delta_x)

delta_t=1/50
t=np.arange(0, 1, delta_t)
#solution=explicit_difference_scheme(x,t,delta_x,delta_t,D)

#print (solution)


delta_t=1/100
t=np.arange(0, 1, delta_t)
solution=explicit_difference_scheme(x,t,delta_x,delta_t,D)

delta_t=1/200
t=np.arange(0, 1, delta_t)
#solution=explicit_difference_scheme(x,t,delta_x,delta_t,D)

# Plotting the solutions
X, T = np.meshgrid(x, t)

fig = plt.figure(figsize=(10, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, T, solution.T, cmap='viridis')  # Transpose solution_1 for correct shape
ax1.set_title('Solution for delta_t = 1/50')

plt.show()



"""


def finite_difference_scheme(x, t, delta_x, delta_t, D):
    s = D * (delta_t / delta_x**2)

    # Create the solution matrix
    U = np.zeros((len(t), len(x)))
    print('U shape:',U.shape)

    # Set the boundary conditions
    U[0, :] = 0
    U[1, :] = 0

    U[:, 0] = u_initial(x)

    # Loop over time
    for n in range(1, len(t) - 1):
        # Loop over space
        for i in range(1, len(x) - 1):
            U[n+1, i] = s * U[n, i-1] + (1 - 2 * s) * U[n,i] + s * U[n,i+1]

    return U


def u_initial(x):
    '''
    Initial conditions - u(x,0)
    '''
    for i in range(len(x)):
        if 0 <= x[i] <= 0.5:
            u = x[i]
        elif 0.5 < x[i] <= 1:
            u = 1 - x[i]

    return u


def u_exact(D, x, t):
    result = 0

    for k in range(1, 14):
        result += 4 / (k * np.pi)**2 * np.sin(k * np.pi / 2) * np.sin(k * np.pi * x) * np.exp(-D * (k ))

    return result

D = 0.5

#Create the grid
dt = 0.02
dx = 0.1

x = np.arange(0, 1 + dx, dx)
t = np.arange(0, 1 + dt, dt)
X, T = np.meshgrid(x, t)

exact_solution = u_exact(D, X, T)
print(exact_solution.shape)

solution = finite_difference_scheme(x, t, dx, dt, D)
print(solution.shape)

X, T = np.meshgrid(x, t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, solution, cmap='viridis')
#Rotate the figure
ax.view_init(azim=30)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('u')
"""