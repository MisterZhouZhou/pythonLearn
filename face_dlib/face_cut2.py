import dlib         # 人脸识别的库dlib
import numpy as np  # 数据处理的库numpy
import cv2          # 图像处理的库OpenCv
import os

'''
  人脸识别&剪切
'''

# 存放图片的地方
path_save = 'data/imgs/faces/'


# Delete old images
def clear_images():
   imgs = os.listdir(path_save)
   for img in imgs:
       os.remove(path_save + img)

clear_images()

# Dlib 检测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('data/libs/shape_predictor_68_face_landmarks.dat')

# 读取图像
img = cv2.imread("data/imgs/faces_2.jpeg")


# Dlib 检测
dets = detector(img, 1)
print("人脸数：", len(dets), "\n")

# 记录人脸矩阵大小
height_max = 0
width_sum = 0

# 计算要生成的图像 img_blank 大小
for k, d in enumerate(dets):
    # 计算矩形大小
    # (x,y), (宽度width, 高度height)
    pos_start = tuple([d.left(), d.top()])
    pos_end = tuple([d.right(), d.bottom()])

    # 计算矩形框大小
    height = d.bottom()-d.top()
    width = d.right()-d.left()

    # 生成用来显示的图像
    img_blank = np.zeros((height, width, 3), np.uint8)
    # 填充
    for i in range(height):
        for j in range(width):
                img_blank[i][j] = img[d.top()+i][d.left()+j]

    # 存在本地
    print("Save to:", path_save+"img_face_"+str(k+1)+".jpg")
    cv2.imwrite(path_save+"img_face_"+str(k+1)+".jpg", img_blank)