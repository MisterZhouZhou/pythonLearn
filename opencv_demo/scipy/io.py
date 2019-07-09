from scipy import io as spio
import numpy as np
'''
数据输入输出
'''
if __name__ == '__main__':
    # 载入和保存matlab文件
    x = np.ones((3, 3))
    spio.savemat('f.mat', {'a': '1212'})
    data = spio.loadmat('f.mat', struct_as_record=True)
    print(data['a'])