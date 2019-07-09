'''
图片扫描
'''
import cv2
import numpy as np
from opencv_demo.utils import rect


#读入要检测的图片，此处读入单张图片。如果分辨率足够好的话，我们也可以使用笔记本电脑的摄像头。
image = cv2.imread('images/book.png')
#重新设置图片的大小，以便对其进行处理:选择最佳维度，以便重要内容不会丢失
image = cv2.resize(image, (1500, 880))
#创建原始图像的副本
orig = image.copy()
#对图像进行灰度处理，并进而进行行高斯模糊处理
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#使用canny算法进行边缘检测
edged = cv2.Canny(blurred, 0, 50)
#创建canny算法处理后的副本
orig_edged = edged.copy()
#找到边缘图像中的轮廓，只保留最大的，并初始化屏幕轮廓
#findContours()函数用于从二值图像中查找轮廓
img, contours, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#使用python中的sorted函数返回contours重新排序的结果（降序），排序规则（key）：根据计算的轮廓面积大小
contours = sorted(contours, key=cv2.contourArea, reverse=True)
#得到近似轮廓

for c in contours:
    p = cv2.arcLength(c, True)  # 计算封闭轮廓的周长或者曲线的长度
    approx = cv2.approxPolyDP(c, 0.02 * p, True)  # 指定0.02*p精度逼近多边形曲线，这种近似曲线为闭合曲线,因此参数closed为True
    if len(approx) == 4:  # 如果逼近的是四边形
        target = approx  # 则此轮廓为要找的轮廓
        break  # 找到即跳出循环

#将目标映射到800*800四边形
approx = rect.rectify(target)
pts2 = np.float32([[0, 0], [800, 0], [800, 800], [0, 800]])

# 透视变换
# 使用gtePerspectiveTransform函数获得透视变换矩阵：approx是源图像中四边形的4个定点集合位置；pts2是目标图像的4个定点集合位置
M = cv2.getPerspectiveTransform(approx, pts2)
# 使用warpPerspective函数对源图像进行透视变换，输出图像dst大小为800*800
dst = cv2.warpPerspective(orig, M, (800, 800))
# 画出轮廓，-1表示所有的轮廓，画笔颜色为（0,255,0），粗细为2
cv2.drawContours(image, [target], -1, (0, 255, 0), 2)
# 对透视变换后的图像进行灰度处理
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

# 对透视变换后的图像使用阈值进行约束获得扫描结果

# 使用固定阈值操作：threshold()函数：有四个参数：第一个是原图像，第二个是进行分类的阈值，第三个是高于(低于)阈值时赋予的新值，
# 第四个是一个方法选择参数：cv2.THRESH_BINARY(黑白二值)
# 该函数返回值有两个参数，第一个是retVal(得到的阈值值(在OTSU会用到))，第二个是阈值化后的图像
ret, th1 = cv2.threshold(dst, 127, 255, cv2.THRESH_BINARY)  # 进行固定阈值处理，得到二值图像
# 使用Otsu's二值化，在最后一个参数加上cv2.THRESH_OTSU
ret2, th2 = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 使用自适应阈值操作：adaptiveThreshold()函数
# 第二个参数为领域内均值，第五个参数为规定正方形领域大小（11*11），第六个参数是常数C：阈值等于均值减去这个常数
th3 = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# 第二个参数为领域内像素点加权和，权重为一个高斯窗口，第五个参数为规定正方形领域大小（11*11），第六个参数是常数C：阈值等于加权值减去这个常数
th4 = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 输出处理后的图像
# cv2.imshow("原始图像", orig)
# cv2.imshow("原始图像经灰度变换", gray)
# cv2.imshow("原始图像经高斯模糊处理", blurred)
# cv2.imshow("原始图像经canny边缘检测后的结果", orig_edged)
# cv2.imshow("边界被标记的原图", image)
# cv2.imshow("固定阈值操作", th1)
# cv2.imshow("Otsu二值化", th2)
cv2.imshow("自适应阈值（领域内均值）", th3)
cv2.imshow("自适应阈值（领域内像素点加权和）", th4)
# cv2.imshow("透视变换后的图像", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()