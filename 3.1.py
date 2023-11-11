import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def f(t):
    return np.log1p(np.abs(1.3+t))-np.exp(t)

t_values= np.arange(2,3,0.05)
s_values = f(t_values)
for i in range(len(t_values)):
    print(f"t={t_values[i]},f(t)={s_values[i]}")
max = np.max(s_values)
print("Наибольшее значение массива: ", max)
min = np.min(s_values)
print("Наименьшее значение массива: ", min)
sr = np.mean(s_values)
print("Среднее значение массива: ", sr)
kol_el = len(s_values)
print("Количество элементов массива: ", kol_el)
sort = np.sort(s_values)[::-1]
print("Отсортированный массив: ", sort)

plt.plot(t_values, s_values, label ='f(t)')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('График функции f(t)')
plt.grid(True)
plt.savefig('plot1.png')

sr_line = np.full(len(s_values),sr)
plt.plot(t_values, s_values,label = 'f(t)')
plt.plot(t_values, sr_line, label = 'Среднее значение')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('График функции f(t) и прямой со средним значением')
plt.legend()
plt.grid(True)
plt.savefig('plot2.png')
