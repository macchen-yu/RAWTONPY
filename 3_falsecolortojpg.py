#將偽色圖輸出成.jpg檔案
from PIL import Image
from spectral import envi # load envi module
import numpy as np
file_name = f"./orignal_data/1_RT.hdr"  # or use 'os.listdir' to list files inside the folder

data = envi.open(file_name)
np_data = data.asarray()
default_bands = [192,134, 76] # index the (R, G, B)
false_color_data = np_data[..., default_bands]
arr_min, arr_max = np.min(false_color_data), np.max(false_color_data)

# 執行歸一化
normalized_arr = (false_color_data- arr_min) / (arr_max - arr_min) * 255

# 將歸一化後的陣列轉換為uint8
fc_int = normalized_arr.astype(np.uint8)
# 創建Image對象
img = Image.fromarray(fc_int)

# 保存為JPG
img.save('falsecolor.jpg')