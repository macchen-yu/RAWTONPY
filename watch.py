#查看result.npy的第一個band

import numpy as np
import matplotlib.pyplot as plt

data = np.load("result.npy")

plt.imshow(data[...,1])
plt.show()
