import numpy as np

a = 0.3
b = -21.17

y = (a+1.5)**(1/3)+(a-b)**8-b/np.arcsin(np.abs(a)**2)

print("Значение выражения равно: ", y)