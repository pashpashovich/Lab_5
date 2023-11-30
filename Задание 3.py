import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('test.csv')

df = df.sample(n=1000)

print(f"\nПропуски в значениях:"
      f"\n{df.isnull().sum()}")

plt.figure(figsize=(12,12))
plt.subplot(1,2,1)
df['Square'].plot(kind='box', logy=True)
plt.title('Ящик с усами')

plt.subplot(1, 2, 2)
df['Square'].plot(kind='hist', bins=30, logy=True)
plt.title('Гистограмма')

plt.show()

#5
numeric_columns = ['Square','LifeSquare','KitchenSquare','Healthcare_1']
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
df = df[(df['Square'] > 20) & (df['Square'] < 200)]

#6
print(f"\n\tNumber of Apartments by Number of Rooms"
          f"\n{df['Rooms'].value_counts()}")

#7
pivot_table = df.pivot_table(index='DistrictId', columns='Rooms', values='Id', aggfunc='count')
print(f"\n\tSummury Table"
      f"\n{pivot_table}")

#8
df.to_csv('surname.csv',index=False)