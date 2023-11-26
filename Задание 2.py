import numpy as np

X = np.zeros((12, 3))
X[:, 0] = 1
X[:, 1] = np.random.randint(15, 27, (1, 12))
X[:, 2] = np.random.randint(60, 82, (1, 12))

Y = np.zeros((12, 1))
Y[:, 0] = np.random.uniform(13.5, 18.6, (1, 12))
print(Y)

A = np.linalg.inv(X.transpose() @ X) @ (X.transpose() @ Y)

Y = X @ A
print(Y)