# -*- coding: utf-8 -*-
# 图像边缘处理

import cv2
import os
import numpy as np

Min_Max = [(0, 50), (0, 100), (0, 150), (0, 200), (0, 250),
           (50, 100), (50, 150), (50, 200), (50, 250),
           (100, 150), (100, 200), (100, 250),
           (150, 200), (150, 250),
           (200, 250)]
pic = cv2.imread('girl.jpg')

try:
    os.mkdir('pic/pretreated_with_Gaussian_filter')
    os.mkdir('pic/without_Gaussian_filter')
    os.mkdir('pic/concatenate')
except OSError:
    pass

# 不经过　高斯滤波处理　去除噪声
for min_max in Min_Max:
    min = min_max[0]
    max = min_max[1]
    edges = cv2.Canny(pic, min, max)
    edges = np.expand_dims(edges, axis=2)
    # cv2.imshow('canny_edge[{:>03},{:>03}]'.format(min, max), edges)
    # cv2.waitKey(2000)
    # cv2.destroyAllWindows()
    cv2.imwrite('pic/without_Gaussian_filter/canny_edge[{:>03},{:>03}].jpg'.format(min, max), edges)


# 有先经过　高斯滤波处理　去除噪声
pic = cv2.GaussianBlur(src=pic, ksize=(5, 5), sigmaX=0, sigmaY=0)

for min_max in Min_Max:
    min = min_max[0]
    max = min_max[1]
    edges = cv2.Canny(pic, min, max)
    edges = np.expand_dims(edges, axis=2)
    # cv2.imshow('canny_edge[{:>03},{:>03}]'.format(min, max), edges)
    # cv2.waitKey(2000)
    # cv2.destroyAllWindows()
    cv2.imwrite('pic/pretreated_with_Gaussian_filter/canny_edge[{:>03},{:>03}].jpg'.format(min, max), edges)


# 组合显示图片　进行对比
image_no_gaussian_paths = [os.path.join('pic/without_Gaussian_filter', path) for path in os.listdir('pic/without_Gaussian_filter')]
image_with_gaussian_paths = [path.replace('without_Gaussian_filter', 'pretreated_with_Gaussian_filter') for path in image_no_gaussian_paths]

for (image_no_gaussian_path, image_with_gaussian_path) in zip(image_no_gaussian_paths, image_with_gaussian_paths):
    image_no_gaussian = cv2.imread(image_no_gaussian_path)
    image_with_gaussian = cv2.imread(image_with_gaussian_path)
    concat_pic = np.concatenate([image_no_gaussian, image_with_gaussian], axis=1)
    # cv2.imshow(image_no_gaussian_path[-23:-4], concat_pic)
    # cv2.waitKey(2000)
    # cv2.destroyAllWindows()
    cv2.imwrite('pic/concatenate/{:>03}.jpg'.format(image_no_gaussian_path[-23:-4]), concat_pic)