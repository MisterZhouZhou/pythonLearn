import dlib
import cv2
'''
    人脸检测
'''

# 使用 Dlib 的正面人脸检测器 frontal_face_detector
detector = dlib.get_frontal_face_detector()

# 图片所在路径
img = cv2.imread('data/imgs/faces_2.jpeg')
# 将图片转为灰度
frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用detector检测器来检测图像中的人脸
faces = detector(img, 1)
print("人脸数 / faces in all：", len(faces))

# 遍历绘制人脸边框
for rect in faces:
    cv2.rectangle(img, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 255, 255), 2)

cv2.namedWindow("img", 2)
cv2.imshow("img", img)
# 等待10毫秒看是否有按键输入
cv2.waitKey(0)