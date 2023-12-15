import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x, y) = -2xy^2
def f(x, y):
  return -2 * x * y**2


# Define the Runge-Kutta method
def rk4(f, x0, y0, h):
  k1 = h * f(x0, y0)
  k2 = h * f(x0 + h/2, y0 + k1/2)
  k3 = h * f(x0 + h/2, y0 + k2/2)
  k4 = h * f(x0 + h, y0 + k3)
  return y0 + (k1 + 2*k2 + 2*k3 + k4) / 6


# Fourth-order Adams-Bashforth-Moulton method
def adams_bashforth_moulton(f, x0, y0, h, n):
  y = np.zeros(n + 1)
  y[0] = y0

  # Use the Runge-Kutta method for the first 3 steps
  for i in range(1, 4):
    y[i] = rk4(f, x0 + (i - 1) * h, y[i - 1], h)

  # Apply the fourth-order Adams-Bashforth method for the remaining steps
  for i in range(4, n + 1):
    yp = y[i - 1] + h * (55 * f(x0 + (i - 1) * h, y[i - 1]) - 59 * f(x0 + (i - 2) * h, y[i - 2]) + 37 * f(x0 + (i - 3) * h, y[i - 3]) - 9 * f(x0 + (i - 4) * h, y[i - 4])) / 24
    print(x0+(i-1)*h," ", y[i-1])
    print(f(x0 + (i - 1) * h, y[i - 1]))
    print(f(x0 + (i - 2) * h, y[i - 2]))
    print(f(x0 + (i - 3) * h, y[i - 3]))
    print(f(x0 + (i - 4) * h, y[i - 4]))
    print(yp)
    # Apply the fourth-order Adams-Moulton method
    yc = y[i - 1] + h * (9 * f(x0 + i * h, yp) + 19 * f(x0 + (i - 1) * h, y[i - 1]) - 5 * f(x0 + (i - 2) * h, y[i - 2]) + f(x0 + (i - 3) * h, y[i - 3])) / 24

    y[i] = yc

  return y

# Initial values
x0 = 0
y0 = 1
h = 0.25 #step size
n = 4 #number of steps

# Compute solution using the Adams-Bashforth-Moulton method
x = np.linspace(x0, x0 + n * h, n + 1)
y_abm = adams_bashforth_moulton(f, x0, y0, h, n)

# Compute solution using the Runge-Kutta method
y_rk4 = np.zeros(n + 1)
y_rk4[0] = y0
for i in range(1, n + 1):
  y_rk4[i] = rk4(f, x0 + (i - 1) * h, y_rk4[i - 1], h)

# Define the exact solution function
def exact(x):
  return 1 / (1 + x**2)

# Print results
print("x\ty_abm\ty_rk4\ty_exact")
for i in range(n + 1):
  print(f"{x[i]:.5f}\t{y_abm[i]:.5f}\t{y_rk4[i]:.5f}\t{exact(x[i]):.5f}")

# Plot results
plt.plot(x, y_abm, label="Adams-Bashforth-Moulton")
plt.plot(x, y_rk4, label="Runge-Kutta")
plt.plot(x, exact(x), label="Exact Solution", linestyle='--')

# Add labels, title, and legend
plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparison of Numerical and Analytic Solutions")
plt.legend()

# Show the plot
plt.grid(True)
#plt.show()  


# Calculate errors
error_abm = np.abs(y_abm - exact(x))
error_rk4 = np.abs(y_rk4 - exact(x))
print(error_abm)

# Print errors
print("x\tError_ABM\tError_RK4")
for i in range(n + 1):
    print(f"{x[i]:.5f}\t{error_abm[i]:.5f}\t{error_rk4[i]:.5f}")

# Plot errors
plt.plot(x, error_abm, label="Adams-Bashforth-Moulton", color='red')
plt.plot(x, error_rk4, label="Runge-Kutta", color='blue')

# Add labels and title
plt.xlabel("x")
plt.ylabel("|y_computed - y_exact|")
plt.title("Comparison of Errors")
plt.legend()

# Show the plot
plt.grid(True)
plt.semilogy()  # use semilogy for better visualization of errors
#plt.show()
