import numpy as np


def rectify(h):
    h = h.reshape((4, 2))  # 改变数组的形状，变成4*2形状的数组
    hnew = np.zeros((4, 2), dtype=np.float32)  # 创建一个4*2的零矩阵
    # 确定检测文档的四个顶点
    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]  # argmin()函数是返回最大数的索引
    hnew[2] = h[np.argmax(add)]

    diff = np.diff(h, axis=1)  # 沿着制定轴计算第N维的离散差值
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]

    return hnew
