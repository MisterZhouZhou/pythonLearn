import numpy as np
from sklearn.model_selection import train_test_split

# test_size：如果是浮点数，在0-1之间，表示样本占比；如果是整数的话就是样本的数量
# random_state 随机数种子：其实就是该组随机数的编号，在需要重复试验的时候，保证得到一组一样的随机数。比如你每次都填1，其他参数一样的情况下你得到的随机数组是一样的。但填0或不填，每次都会不一样。
# random_state值不变产生相同的随机数

if __name__ == '__main__':
    x,y = np.arange(10).reshape((5,2)), range(5)
    print(x)
    print(list(y))
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    print('========')
    print(x_train)
    print('========')
    print(x_test)
    print('========')
    print(y_train)
    print('========')
    print(y_test)