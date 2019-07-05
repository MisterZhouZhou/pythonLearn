# encoding:utf-8
'''
图片切割
'''
import cv2
import pickle

file_name = 'img/lianliankan2.png'
# cv2.imread()：读入图片，共两个参数，第一个参数为要读入的图片文件名，第二个参数为如何读取图片，包括cv2.IMREAD_COLOR：读入一副彩色图片；cv2.IMREAD_GRAYSCALE：以灰度模式读入图片；cv2.IMREAD_UNCHANGED：读入一幅图片，并包括其alpha通道。

img = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)  # alpha通道
size = img.shape
width = size[1]
height = size[0]
cv2.imshow('src', img)

# 分割为9行8列
x1 = 0
y1 = 0
xp = int(height / 9)
yp = int(width / 8)
mat = []
for x2 in range(xp, height, xp):
    p1 = []
    for y2 in range(yp, width, yp):
        cut = img[x1: x2, y1: y2]
        cv2.imshow('cut', cut)
        cv2.waitKey(100)
        y1 = y2
        p1.append(cut)
    cv2.waitKey(100)
    y1 = 0
    x1 = x2
    mat.append(p1)
'''
pickle提供了一个简单的持久化功能
可以将对象以文件的形式存放在磁盘上
'''
with open('photo_mat', 'wb') as f:
    pickle.dump(mat, f)

print('finish!')

cv2.waitKey(0)
cv2.destroyAllWindows()
