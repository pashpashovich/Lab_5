import numpy as np
from matplotlib import pyplot as plt

t_values = np.arange(2, 3, 0.03)  # массив значений аргумента
s_values = []  # массив значений функции

for t in t_values:  # заполняем значения функции
    s = np.log(abs(1.3 + t)) * np.exp(t)
    s_values.append(s)

print("t      s")

for t, s in zip(t_values, s_values):
    print(f"{t:.2f}  {s:.4f}")

s_max = max(s_values)  # наибольшее значение
s_min = min(s_values)  # наименьшее значение
s_avg = np.mean(s_values)  # среднее количество
s_len = len(s_values)  # количество элементов массива

# сортируем по убыванию
sorted_indices = np.argsort(s_values)[::-1]
sorted_t_values = t_values[sorted_indices]
sorted_s_values = np.array(s_values)[sorted_indices]

print("Отсортированные s по убыванию")
print("t      s")

for t, s in zip(sorted_t_values, sorted_s_values):
    print(f"{t:.2f}  {s:.4f}")

plt.plot(t_values, s_values)

line_avg = [s_avg] * len(t_values)
plt.plot(t_values, line_avg)

plt.xlabel("t")
plt.ylabel("s")

plt.show()
