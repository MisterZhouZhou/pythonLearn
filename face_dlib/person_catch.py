"""
HOG+SVM行人检测
"""
import cv2

image = cv2.imread(r'data/imgs/faces_2.jpeg')
cv2.imshow("input", image)

# 初始化HOG描述子和行人检测器
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# 检测图像中的人
# image:图像
# winStride:HOG检测窗口移动时的步长
# padding:在原图外围添加像素,适当的pad可提高检测的准确率
# scale:可控制金字塔的层数，参数越小，层数越多。通常scale在1.01-1.5之间
(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                        padding=(8, 8), scale=1.05)

for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("hog-detector", image)
cv2.waitKey(0)
