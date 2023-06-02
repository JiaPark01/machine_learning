import numpy as np

b = np.array([[1, 1], [2, 2], [3, 3]])
c = np.insert(b, 1, 4, axis=0)      # [1, 1], [4, 4], [2, 2]
d = np.insert(b, 1, 4, axis=1)      # [1, 4, 1], [2, 4, 2]
print(c)
print(d)
print()

e = np.array([[1, 2, 3], [4, 5, 6]])
f = np.flip(e, axis=1)              # [3, 2, 1], 
print(f)
print()

a = np.array([10, 20, 30])
print("max:", a.max(), "min:", a.min(), "mean:", a.mean())
print()

new_a = a.astype(dtype=np.float64)
print(new_a)
print()

b = np.array([[1, 1], [2, 2], [3, 3]])
print(b.T)              # transpose. switch row and column [1, 2, 3], []
print(b.flatten())      # from multi-D to 1D
print()

c = np.array([3, 5, 9, 1, 0])
c.sort()
print(c)
print(c[::-1])          # reverse sort
print()

d = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
d.sort(axis=0)          # based on the first value in each array, [4][35][69]
                        # default=1. within the array, 24, 35, 55
print(d)
e = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
print(np.flip(e, axis=1))