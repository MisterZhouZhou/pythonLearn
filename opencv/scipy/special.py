'''
一些特殊的数学函数
special库中的特殊函数都是超越函数，所谓超越函数是指变量之间的关系不能用有限次加、减、乘、除、乘方、开方 运算表示的函数。如初等函数中的三角函数、反三角函数与对数函数、指数函数都是初等超越函数，一般来说非初等函数都是超越函数。
'''

'''
scipy.special.jn()     计算n阶贝塞尔函数
scipy.special.ellipj() 函数计算椭圆函数
scipy.special.erf()计算高斯曲线的面积
scipy.linalg.det():计算方阵的行列式
scipy.linalg.inv():计算方阵的逆
scipy.linalg.svd():奇异值分解
scipy.fftpack.fftfreq():生成样本序列
scipy.fftpack.fft():计算快速傅立叶变换
'''

from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

'''
scipy.optimize模块提供了函数最值、曲线拟合和求根的算法
'''
#定义目标函数
def f(x):
    return x**2+10*np.sin(x)

def optimize_function():
    # 绘制目标函数的图形
    plt.figure(figsize=(10, 5))
    x = np.arange(-10, 10, 0.1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('optimize')
    plt.plot(x, f(x), 'r-', label='$f(x)=x^2+10sin(x)$')
    # 图像中的最低点函数值
    # 求函数中的最值, 获取到的是局部最小值，对于精确到全局最低点，可以使用暴力搜索算法
    min_value = optimize.fmin_bfgs(f, 0)
    print(min_value)
    # 暴力搜寻算法，它会评估范围网格内的每一个点
    grid = (-10, 10, 0.1)
    min_value = optimize.brute(f, (grid,))
    print(min_value)
    min_a = f(min_value)
    max_b = 40
    plt.annotate('min', xy=(-1.3, min_a), xytext=(3, max_b), arrowprops=dict(facecolor='black',shrink=0.05))
    plt.legend()
    plt.show()

'''
使用最小二乘法拟合直线
'''
#定义拟合函数形式
def func(p, x):
    k,b = p
    return k*x + b

#定义误差函数
def error(p,x,y,s):
    return func(p,x)-y


def leastsq_function():
    # 训练数据
    Xi = np.array([8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78])
    Yi = np.array([7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05])
    # 随机给出参数的初始值
    p = [10, 2]
    # 使用leastsq()函数进行参数估计
    s = '参数估计次数'
    Para = optimize.leastsq(error, p, args=(Xi, Yi, s))
    k, b = Para[0]
    # 图形可视化
    plt.figure(figsize=(8, 6))
    # 绘制训练数据的散点图
    plt.scatter(Xi, Yi, color='r', label='Sample Point', linewidths=3)
    plt.xlabel('x')
    plt.ylabel('y')
    x = np.linspace(0, 10, 1000)
    y = k * x + b
    plt.plot(x, y, color='orange', label='Fitting Line', linewidth=2)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    leastsq_function()