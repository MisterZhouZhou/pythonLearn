# coding=utf-8
import cv2
# 原图像路径
origin_pic = cv2.imread('google.jpeg')
# 文档路径，用于记录轮廓框坐标
txt_file = open('contours.txt', 'w')
# 要先转换成单通道灰度图像才能进行后续的图像处理
pic = cv2.cvtColor(origin_pic, cv2.COLOR_BGR2GRAY)
# 阈值处理，将前景全填充为白色，背景全填充为黑色
_, pic = cv2.threshold(src=pic, thresh=200, maxval=255, type=1)
# 中值滤波，去除椒盐噪声
pic = cv2.medianBlur(pic, 5)
# 边缘检测，得到的轮廓列表
contours, _2 = cv2.findContours(pic, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 根据轮廓列表，循环在原始图像上绘制矩形边界
for i in range(len(contours)):
    cnt = contours[i]
    x, y, w, h = cv2.boundingRect(cnt)
    origin_pic = cv2.rectangle(origin_pic, (x, y), (x+w, y+h), (255, 0, 0), 2)
    txt_file.write('{}: [{},{}  {},{}  {},{}  {},{}]\n'.format(i+1, x, y, x, y+h, x+w, y, x+w, y+h))

cv2.imwrite('rectangle.jpg', origin_pic)
txt_file.close()

cv2.imshow('', origin_pic)
cv2.waitKey(0)
cv2.destroyAllWindows()