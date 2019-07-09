import dlib
import cv2
import numpy as np

'''
    68特征值检测
'''

#dlib预测器
detector = dlib.get_frontal_face_detector()    #使用dlib库提供的人脸提取器
# Dlib 的 68点模型
predictor = dlib.shape_predictor('data/lib/shape_predictor_68_face_landmarks.dat')   #构建特征提取器

# 图片所在路径
img = cv2.imread('data/imgs/faces_2.jpeg')
# 将图片转为灰度
frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用 detector 检测器来检测图像中的人脸
faces = detector(img, 1)

if len(faces) != 0:
    for face in faces:
        landmarks = np.matrix([[p.x, p.y] for p in predictor(img, face).parts()])  # 人脸关键点识别
        for idx, point in enumerate(landmarks):  # enumerate函数遍历序列中的元素及它们的下标
            # 68点的坐标
            pos = (point[0, 0], point[0, 1])

            # 利用cv2.circle给每个特征点画一个圈，共68个
            cv2.circle(img, pos, 1, color=(0, 255, 0))
            # 利用cv2.putText输出1-68
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # 各参数依次是：图片，添加的文字，坐标，字体，字体大小，颜色，字体粗细
            # cv2.putText(img, str(idx + 1), pos, font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
else:
    # 没有检测到人脸
    cv2.putText(img, "no face", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)

cv2.namedWindow("img", 2)
cv2.imshow("img", img)  # 显示图像
cv2.waitKey(0)