import numpy as np
from matplotlib import pyplot as plt

t_values = np.arange(2, 3, 0.03)
s_values = []

for t in t_values:
    s = np.log(abs(1.3 + t)) * np.exp(t)
    s_values.append(s)


s_max = max(s_values)
s_min = min(s_values)
s_avg = np.mean(s_values)
s_len = len(s_values)

plt.plot(t_values, s_values)

line_avg = [s_avg] * len(t_values)
plt.plot(t_values, line_avg)

plt.xlabel("t")
plt.ylabel("s")

plt.show()