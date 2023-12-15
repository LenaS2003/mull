import math
import matplotlib.pyplot as plt
import numpy as np

plt.axis((0,6, -5, 50))

x=np.linspace(0,12,100)
y=x**3-x**2+x-5
plt.plot(x, y)
plt.scatter(1,-4)
plt.annotate("(x_0,h(x_0))", (1, -4))
plt.scatter(3,3**3-3**2+3-5)
plt.annotate("x_1,h(x_1)", (3,3**3-3**2+3-5))
z= (3-1)/(3**3-3**2+3-5+4) x + 9

plt.show()


a=np.linspace(0.45,0.55,100)