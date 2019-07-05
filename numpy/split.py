import numpy as np

A = np.arange(12).reshape(3,4)
print(A)
# # 纵向分割, 分成两部分, 按列分割
# print(np.split(A, 2, axis=1))
# # 横向分割, 分成三部分, 按行分割
# print(np.split(A, 3, axis=0))

# 不均等分割
# print(np.array_split(A, 3, axis=1))

# 垂直方向分割
print(np.vsplit(A, 3))
# 水平方向分割
print(np.hsplit(A, 2))