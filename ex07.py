import numpy as np

data = np.arange(1, 17)

print(data[data%2 == 0])
print()

a = np.array([[1, 2], [1, -3]])
b = np.array([6, 1])
s = np.linalg.solve(a, b)
print(s)
print()

a = np.array([[2, 1], [4, 5]])
det_a = np.linalg.det(a)
b = np.array([[1, 2], [3, -6]])
det_b = np.linalg.det(b)
print(det_a, det_b)
print()

a = np.array([[1, 1, -1], [2, -1, 3], [1, 2, 1]])
det_a = np.linalg.det(a)
b = np.array([0, 9, 8])
s = np.linalg.solve(a, b)
print(det_a)
print()

# vstack can merge any dimension,
# hstack only when dim equal

# 그만 졸아