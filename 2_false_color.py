# 查看偽色圖

from spectral import envi # load envi module
import numpy as np
import matplotlib.pyplot as plt
file_name = f"./orignal_data/1_RT.hdr"  # or use 'os.listdir' to list files inside the folder

data = envi.open(file_name)
np_data = data.asarray()
default_bands = [192,134, 76] # index the (R, G, B)
false_color_data = np_data[..., default_bands]
# print(false_color_data)


plt.imshow(false_color_data)
plt.show()

