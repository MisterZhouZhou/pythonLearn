import dlib
# from skimage import io
import cv2
'''
    人脸检测1
'''

# 使用 Dlib 的正面人脸检测器 frontal_face_detector
detector = dlib.get_frontal_face_detector()

cv2.namedWindow('W1', 0)
cv2.resizeWindow('W1', 600, 480)
cv2.moveWindow("trans:", 1000, 100)

# 图片所在路径
img = cv2.imread('data/imgs/faces_2.jpeg')
frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 生成 Dlib 的图像窗口(window在新版本不能用）
# win = dlib.image_window()
# win.set_image(img)

# 使用detector检测器来检测图像中的人脸
faces = detector(img, 1)
print("人脸数 / faces in all：", len(faces))

for i, rect in enumerate(faces):
    w = rect.right() - rect.left()
    h = rect.bottom() - rect.top()
    cv2.rectangle(frame_gray, (rect.left(), rect.top()), (rect.left() + w, rect.top() + h), (0, 255, 0), thickness=2)
    cv2.imshow("W1", frame_gray)

cv2.imshow("W1", frame_gray)
# 等待10毫秒看是否有按键输入
k = cv2.waitKey(0)
# # 如果输入q则退出循环
# if k & 0xFF == ord('q'):
#     print('exit')
# 释放摄像头并销毁所有窗口
cv2.destroyAllWindows()

