import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

if __name__ == '__main__':
    # 构建数据
    points_num = 100
    vectors = []
    # 用Numpy的正态随机分页函数生成100个点
    # 这些点的(x,y）坐标值对应线程方程 y = 0.1*x + 0.2
    for i in range(points_num):
        x1 = np.random.normal(0.0, 0.66)
        y1 = x1 * 0.1 + 0.2 + np.random.normal(0.0, 0.04)
        vectors.append([x1, y1])
    print(vectors)