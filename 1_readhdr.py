#讀取hdr檔案

from spectral import envi # load envi module

import numpy as np

file_name = "./orignal_data/1_RT.hdr"  # or use 'os.listdir' to list files inside the folder
data = envi.open(file_name)

print(type(data))
print(data)

print(type(data.metadata['wavelength']))
print(data.metadata['wavelength'])

np_data = data.asarray() # convert to numpy
print(type(np_data))
print(np_data.shape) # (row, sample, band)