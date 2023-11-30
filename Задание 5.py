import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 5)
y = np.linspace(0, 10, 5)

X, Y = np.meshgrid(x, y)  # двумерная сетка

z1 = np.power(X, 0.25) + np.power(Y, 0.25)
z2 = np.power(X, 2) - np.power(Y, 2)
z3 = 2 * X + 3 * Y
z4 = np.power(X, 2) + np.power(Y, 2)
z5 = 2 + 2 * X + 2 * Y - np.power(X, 2) - np.power(Y, 2)

ax = plt.figure(figsize=(15, 15))

ax1 = ax.add_subplot(321, projection='3d')
ax1.plot_surface(X, Y, z1, cmap='viridis')
ax1.set_title('z1')

ax1 = ax.add_subplot(322, projection='3d')
ax1.plot_surface(X, Y, z2, cmap='viridis')
ax1.set_title('z2')

ax1 = ax.add_subplot(323, projection='3d')
ax1.plot_surface(X, Y, z3, cmap='viridis')
ax1.set_title('z3')

ax1 = ax.add_subplot(324, projection='3d')
ax1.plot_surface(X, Y, z4, cmap='viridis')
ax1.set_title('z4')

ax1 = ax.add_subplot(325, projection='3d')
ax1.plot_surface(X, Y, z5, cmap='viridis')
ax1.set_title('z5')

plt.tight_layout()
plt.show()
