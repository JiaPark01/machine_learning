import numpy as np

a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
new_a = np.append([a], b, axis=0)   # append by default convert into 1D array
print(new_a)
print()

c = np.arange(12)
print(c.reshape(-1, 4))

rnd = np.random.rand(5) * 10 + 165  # -10~10 + avg
print(rnd)