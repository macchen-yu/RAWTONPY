import json
import numpy as np
import cv2

# 讀取 JSON 文件
with open("../fx17.json", "r") as f:
    data = json.load(f)

# 創建一個空白的圖像
image = cv2.imread("../falsecolor.jpg")
mask = np.zeros_like(image, dtype=np.uint8)

# 遍歷每個 shape 並提取坐標點
# for i,shape in data["shapes"]:
for i, shape in enumerate(data["shapes"]):
    if "points" in shape:
        points = np.array(shape["points"], dtype=np.int32)
        cv2.fillPoly(mask, [points], (i+1, i+1, i+1))

# 保存掩碼為 .npy 文件
np.save("mask.npy", mask[..., 0])