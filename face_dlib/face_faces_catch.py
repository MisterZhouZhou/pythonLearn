# -*- coding: utf-8 -*-
import cv2
import dlib
# import datetime
import numpy as np

'''
 面部表情跟踪
'''

def face_boundary(img, shape):
    # enumerate方法同时返回数据对象的索引和数据
    for i, d in enumerate(shape.parts()):
        if i == 0:
            x_min = d.x
            x_max = d.x
            y_min = d.y
            y_max = d.y
        else:
            if d.x < x_min:
                x_min = d.x

            if d.x > x_max:
                x_max = d.x

            if d.y < y_min:
                y_min = d.y

            if d.y > y_max:
                y_max = d.y

    # 如果出现负值，即人脸位于图像框之外的情况，应忽视图像外的部分，将负值置为0
    if x_min < 0:
        x_min = 0

    if y_min < 0:
        y_min = 0

    if x_min == x_max or y_min == y_max:
        return None
    else:
        return img[y_min:y_max, x_min:x_max]


def draw_left_eyebrow(img, shape):
    # 17 - 21
    pt_pos = []
    for index, pt in enumerate(shape.parts()[17:22]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)


def draw_right_eyebrow(img, shape):
    # 22 - 26
    pt_pos = []
    for index, pt in enumerate(shape.parts()[22:27]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)


def draw_left_eye(img, shape):
    # 36 - 41
    pt_pos = []
    for index, pt in enumerate(shape.parts()[36:42]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)

    cv2.line(img, pt_pos[0], pt_pos[-1], 255, 2)


def draw_right_eye(img, shape):
    # 42 - 47
    pt_pos = []
    for index, pt in enumerate(shape.parts()[42:48]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)

    cv2.line(img, pt_pos[0], pt_pos[-1], 255, 2)


def draw_nose(img, shape):
    # 27 - 35
    pt_pos = []
    for index, pt in enumerate(shape.parts()[27:36]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)

    cv2.line(img, pt_pos[0], pt_pos[4], 255, 2)
    cv2.line(img, pt_pos[0], pt_pos[-1], 255, 2)
    cv2.line(img, pt_pos[3], pt_pos[-1], 255, 2)


def draw_mouth(img, shape):
    # 48 - 59
    pt_pos = []
    for index, pt in enumerate(shape.parts()[48:60]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)

    cv2.line(img, pt_pos[0], pt_pos[-1], 255, 2)

    # 60 - 67
    pt_pos = []
    for index, pt in enumerate(shape.parts()[60:]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)

    cv2.line(img, pt_pos[0], pt_pos[-1], 255, 2)


def draw_jaw(img, shape):
    # 0 - 16
    pt_pos = []
    for index, pt in enumerate(shape.parts()[0:17]):
        pt_pos.append((pt.x, pt.y))

    for num in range(len(pt_pos) - 1):
        cv2.line(img, pt_pos[num], pt_pos[num + 1], 255, 2)


# 使用特征提取器get_frontal_face_detector
detector = dlib.get_frontal_face_detector()
# dlib的68点模型，使用训练好的特征预测器
predictor = dlib.shape_predictor("data/lib/shape_predictor_68_face_landmarks.dat")
# 使用电脑自带摄像头
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while (1):
    # cap.read()
    # 返回两个值：
    #    一个布尔值true/false，用来判断读取视频是否成功/是否到视频末尾
    #    图像对象，图像的三维矩阵
    ret, frame = cap.read()

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    dets = detector(img, 1)

    for index, face in enumerate(dets):
        # 使用预测器得到68点数据的坐标
        shape = predictor(img, face)
        # image.shape获取图像的形状，返回值是一个包含行数、列数、通道数的元组
        features = np.zeros(img.shape[0:-1], dtype=np.uint8)  # 黑色图像
        for i, d in enumerate(shape.parts()):
            d_pos = (d.x, d.y)
            cv2.circle(features, d_pos, 2, 255, 1)

        draw_left_eyebrow(features, shape)
        draw_right_eyebrow(features, shape)
        draw_left_eye(features, shape)
        draw_right_eye(features, shape)
        draw_nose(features, shape)
        draw_mouth(features, shape)
        draw_jaw(features, shape)

        faceROI = face_boundary(features, shape)
        faceROI = cv2.resize(faceROI, (500, 500), interpolation=cv2.INTER_LINEAR)
        cv2.imshow('face {}'.format(index), faceROI)

    if cv2.waitKey(10) == 27:  # 按ESC
        break