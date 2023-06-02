import numpy as np
list_a = list()
for i in range(20):
    list_a.append(i)

numpy_a = np.array(list_a)
print(numpy_a)
print()

list_new_a = [i for i in range(20)]
print(f"list_new_a : {list_new_a}")
print()

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(a + b)
print()
print(a - 1)
print()

print(a * 10)   # broadcasting
print()

c = np.array([[10, 20, 30],
              [40, 50, 60]])
d = np.array([2, 3, 4])
print(c + d)
print()

print(np.zeros(2, 3))
print()
