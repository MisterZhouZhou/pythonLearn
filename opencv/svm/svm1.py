# encoding:utf-8
import cv2
import numpy as np

SZ = 20
bin_n = 16
affine_flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR


# 使用方向梯度直方图HOG作为特征向量
def deskew(img):
    m = cv2.moments(img)  # 计算图像中的中心矩(最高到三阶)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11'] / m['mu02']
    M = np.float32([[1, skew, -0.5 * SZ * skew], [0, 1, 0]])
    # 图像的平移，参数:输入图像、变换矩阵、变换后的大小
    img = cv2.warpAffine(img, M, (SZ, SZ), flags=affine_flags)
    return img


# 计算图像的 X 方向和 Y 方向的 Sobel 导数
def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)  # 笛卡尔坐标转换为极坐标, → magnitude, angle
    bins = np.int32(bin_n * ang / (2 * np.pi))
    bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
    mag_cells = mag[:10, :10], mag[10:, :10], mag[:10, 10:], mag[10:, 10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)

# 将大图分割为小图，使用每个数字的前250个作为训练数据，后250个作为测试数据
img = cv2.imread('ts.png', 0)
cells = [np.hsplit(row, 100) for row in np.vsplit(img, 50)]
# 第一部分是训练数据，剩下的是测试数据
train_cells = [i[:50] for i in cells]
test_cells = [i[50:] for i in cells]


deskewed = [list(map(deskew, row)) for row in train_cells]
hogdata = [list(map(hog, row)) for row in deskewed]


trainData = np.float32(hogdata).reshape(-1, 64)
labels = np.repeat(np.arange(10), 250)[:, np.newaxis]

svm = cv2.ml.SVM_create()
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setType(cv2.ml.SVM_C_SVC)
svm.setC(2.67)
svm.setGamma(5.383)
svm.train(trainData, cv2.ml.ROW_SAMPLE, labels)
svm.save('svm_data.dat')

deskewed = [list(map(deskew, row)) for row in test_cells]
hogdata = [list(map(hog, row)) for row in deskewed]
testData = np.float32(hogdata).reshape(-1, bin_n * 4)


ret, result = svm.predict(testData)
mask = result == labels
correct = np.count_nonzero(mask)
print(correct * 100.0 / len(result), '%')