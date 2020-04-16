import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from numpy import load

plt.style.use('fivethirtyeight')

ax = plt.axes(projection="3d")
data = load("converter-runs/label-0.npy")
   
def z_function(x,y):
   return data[np.int(x)][np.int(y)]

f2 = np.vectorize(z_function)

x = np.linspace(99, 0)
y = np.linspace(99, 0)


X, Y = np.meshgrid(x,y)
Z = f2(X, Y)

ax.plot_surface(X,Y,Z)

plt.show()