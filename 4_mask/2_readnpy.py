import numpy as np
import matplotlib.pyplot as plt

data = np.load("mask.npy")

plt.imshow(data)
plt.show()
