import numpy as np

X = np.zeros((12, 3))
X[:, 0] = 1
X[:, 1] = np.random.randint(15, 27, (1, 12))
X[:, 2] = np.random.randint(60, 82, (1, 12))
print("Матрица X: ")
print(X)
Y = np.zeros((12, 1))
Y[:, 0] = np.random.uniform(13.5, 18.6, (1, 12))
print("Матрица Y: ")
print(Y)
A = np.linalg.inv(X.transpose() @ X) @ (X.transpose() @ Y)
print("Вектор оценок A: ")
print(A)

Y = X @ A
print("Проверка:")
print(Y)