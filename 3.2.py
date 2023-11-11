import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

x = np.linspace(0,2,40)
y = np.linspace(0,2,40)
X,Y=np.meshgrid(x,y)
Z = X**0.25 + Y**0.25
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(X,Y,Z)
plt.savefig('plot3.2.1.png')
print("Первый график построен")

Z=X**2-Y**2
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(X,Y,Z)
plt.savefig('plot3.2.2.png')
print("Второй график построен")


Z= 2*X + 3*Y
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(X,Y,Z)
plt.savefig('plot3.2.3.png')
print("Третий график построен")

Z= X**2+Y**2
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(X,Y,Z)
plt.savefig('plot3.2.4.png')
print("Четвертый график построен")


Z=2 + 2*X +2*Y -X**2-Y**2
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(X,Y,Z)
plt.savefig('plot3.2.5.png')
print("Пятый график построен")