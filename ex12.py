import matplotlib.pyplot as plt
import numpy as np

f1 = np.random.normal(0, 1, 10_000)
f2 = np.random.normal(3, 5, 10_000)

plt.hist(f1, bins=200, color='red', alpha=0.8)
plt.hist(f2, bins=200, color='green', alpha=0.4)
plt.show()