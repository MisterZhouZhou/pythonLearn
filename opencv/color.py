# -*- coding: utf-8 -*-
# 图片色道调整, 混色
import cv2
import numpy as np

pic = cv2.imread('girl.jpg')
b, g, r = cv2.split(pic)

# 单色图片
# 保留blue通道，其他通道全部置为0
b_pic = np.zeros((424, 600, 3), np.uint8)
b_pic[:, :, 0] = b
cv2.imshow('b_pic', b_pic)
key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()

# 保留 green 通道，其他通道全部置０
    g_pic = np.zeros((424, 600, 3), np.uint8)
    g_pic[:, :, 1] = g
    cv2.imshow('g_pic', g_pic)
    cv2.imwrite('../images/g_pic.jpg', g_pic)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    # 保留 red 通道，其他通道全部置０
    r_pic = np.zeros((424, 600, 3), np.uint8)
    r_pic[:, :, 2] = r
    cv2.imshow('r_pic', r_pic)
    cv2.imwrite('../images/r_pic.jpg', r_pic)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


    ### 双色混合图片
    # green、red通道混合，其他通道全部置０
    gr_pic = cv2.imread('../images/girl.jpg')
    gr_pic[:, :, 0] = 0
    cv2.imshow('gr_pic', gr_pic)
    cv2.imwrite('../images/gr_pic.jpg', gr_pic)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    # blue、red通道混合，其他通道全部置０
    br_pic = cv2.imread('../images/girl.jpg')
    br_pic[:, :, 1] = 0
    cv2.imshow('br_pic', br_pic)
    cv2.imwrite('../images/br_pic.jpg', br_pic)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    # blue、green通道混合，其他通道全部置０
    bg_pic = cv2.imread('../images/girl.jpg')
    bg_pic[:, :, 2] = 0
    cv2.imshow('bg_pic', bg_pic)
    cv2.imwrite('../images/bg_pic.jpg', bg_pic)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


    ### 三通道全混合
    # 存为 RGB 通道顺序的 图片
    rgb_pic = np.zeros((424, 600, 3), np.uint8)
    rgb_pic[:, :, 0] = r
    rgb_pic[:, :, 1] = g
    rgb_pic[:, :, 2] = b
    cv2.imshow('rgb_pic', rgb_pic)
    cv2.imwrite('../images/rgb_pic.jpg', rgb_pic)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

    # 存为 BGR 通道顺序的 图片
    bgr_pic = np.zeros((424, 600, 3), np.uint8)
    bgr_pic[:, :, 0] = b
    bgr_pic[:, :, 1] = g
    bgr_pic[:, :, 2] = r
    cv2.imshow('bgr_pic', bgr_pic)
    cv2.imwrite('../images/bgr_pic.jpg', bgr_pic)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()