import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
matplotlib.use('TkAgg')

dataset = pd.read_csv('test.csv')
values = dataset.sample(n=1000)
missing = values.isnull().sum()
print("Пропущенные значения:\n", missing)

fig, axes = plt.subplots(1,2, figsize=(10,5))
values['Id'].plot.box(ax=axes[0])
values['Id'].plot.hist(ax=axes[1])
plt.show()


values['Id'].fillna(values['Id'].mean(), inplace=True)
lower_bound = values['Id'].quantile(0.05)
upper_bound = values['Id'].quantile(0.95)
values['Id']= np.where(values['Id'] < lower_bound, lower_bound, values['Id'])
values['Id'] = np.where(values['Id'] > upper_bound, upper_bound, values['Id'])

room_counts = values['Rooms'].value_counts()
print("Количество квартир по количеству комнат: ", room_counts)

pivot_table = values.pivot_table(index='DistrictId', columns='Rooms', values='Square',aggfunc="sum", fill_value=0)
if 'DistrictId' in values.columns and 'Rooms' in values.columns:
    pivot_table = values.pivot_table(index='DistrictId', columns='Rooms', values='Square',aggfunc="sum", fill_value=0)
else:
    print("Столбцы 'DistrictId' и/или 'Rooms' отсутстыуют")
print("Сводная таблица:\n ", pivot_table)

plt.show()

