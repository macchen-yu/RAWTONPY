# 把labelme未框選到範圍值變成0

from spectral import envi # load envi module
import numpy as np
file_name = f"./orignal_data/1_RT.hdr" # or use 'os.listdir' to list files inside the folder

data = envi.open(file_name)
np_data = data.asarray()

mask = np.load("./4_mask/mask.npy")


# 將 mask 擴展為三維數組以與 npdata 尺寸對應
mask_3d = np.expand_dims(mask, axis=2)
mask_3d = np.repeat(mask_3d, np_data.shape[2], axis=2)  # 每個通道的值都一樣
#
# # 檢查 mask_3d 是否每個通道的值都一樣
# if np.all(mask_3d == mask_3d[:, :, 0][:, :, np.newaxis]):
#     mask_3d = mask_3d[:, :, 0]  # 將其轉換為二維數組

# 找出 mask 中為 0 的位置
zero_positions = np.where(mask_3d == 0)

# 複製 npdata 以允許修改
npdata_copy = np.copy(np_data)

# 將相同位置的 npdata 中的值設置為 0
npdata_copy[zero_positions] = 0

np.save("result.npy",npdata_copy)

