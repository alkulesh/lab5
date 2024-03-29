import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
matplotlib.use('TkAgg')


x = np.linspace(0,2,40)
y = np.linspace(0,2,40)
X,Y=np.meshgrid(x,y)

Z1 = X**0.25 + Y**0.25
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_wireframe(X,Y,Z1)
plt.show()

Z2 = X**2-Y**2
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_wireframe(X,Y,Z2)
plt.show()

Z3 = 2*X +3*X
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_wireframe(X,Y,Z3)
plt.show()

Z4 = X**2 +Y**2
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_wireframe(X,Y,Z4)
plt.show()

Z5 = 2+2*X+2*Y-X**2-Y**2
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_wireframe(X,Y,Z5)
plt.show()