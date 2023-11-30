import numpy as np

X = np.zeros((12, 3))  # заполняем матрицу нулями
X[:, 0] = 1  # 1-й столбец единицами
X[:, 1] = np.random.randint(15, 27, (1, 12))  # второй столбец произвольными целыми числами от 15 до 15+12
X[:, 2] = np.random.randint(60, 82, (1, 12))  # третий столбец
print("Матрица X: ")
print(X)
Y = np.zeros((12, 1))  # вектор-столбец
Y[:, 0] = np.random.uniform(13.5, 18.6, (1, 12))
print("Вектор-столбец Y: ")
print(Y)
A = np.linalg.inv(X.transpose() @ X) @ (X.transpose() @ Y)  # inv - обратная
print("Вектор оценок A: ")
print(A)

Y = X @ A
print("Проверка:")
print(Y)
