import numpy as np

A = np.arange(12).reshape(3,4)
print(A)
resutl_A = np.vsplit(A, 2)
print(resutl_A)