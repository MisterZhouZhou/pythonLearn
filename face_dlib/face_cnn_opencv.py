import dlib
import cv2
'''
    cnn人脸检测
'''

# 使用 Dlib导入cnn模型
detector = dlib.cnn_face_detection_model_v1('data/lib/mmod_human_face_detector.dat')

# 图片所在路径
img = cv2.imread('data/imgs/faces_2.jpeg')
# 将图片转为灰度
frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用detector检测器来检测图像中的人脸
faces = detector(img, 1)
print("人脸数 / faces in all：", len(faces))

# 遍历绘制人脸边框
for rect in faces:
    # cnn检测返回的结果和dlib人脸检测返回的结果结构还是有点不一样的
    face = rect.rect
    cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 255), 2)

cv2.namedWindow("img", 2)
cv2.imshow("img", img)
# 等待10毫秒看是否有按键输入
cv2.waitKey(0)