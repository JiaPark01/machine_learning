import numpy as np
from math import sin

a = np.array([[10, 20, 30], [40, 50, 60]])
b = np.array([2, 3, 4])
print(a * b)
print()
print(a + b)
print()

print(np.eye(4) * 10)   # broadcasting
print()
print(np.full((2, 3), 10))
print()

print(np.arange(0.0, 1.0, 0.2)) # increase by 0.2
print()

a = np.linspace(0, 10, 4)       # split into 4 numbers
print(a)
print()

data = np.linspace(0, np.pi, 11)
result = list()

for i in data:
    result.append(i)
    pass
print(result)
print()