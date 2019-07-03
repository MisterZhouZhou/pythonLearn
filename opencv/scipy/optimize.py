
'''
使用最小二乘法拟合正弦函数
'''
import numpy as np
from scipy import optimize
import  matplotlib.pyplot as plt

#定义拟合函数图形
def func(x,p):
    A,k,theta = p
    return A*np.sin(2*np.pi*k*x+theta)

#定义误差函数
def error(p,x,y):
    return y-func(x,p)

#生成训练数据
#随机给出参数的初始值
p0 = [10, 0.34, np.pi/6]
A,k,theta = p0
x = np.linspace(0, 2*np.pi, 1000)
#随机指定参数
y0 = func(x, p0)
#randn(m)从标准正态分布中返回m个值，在本例作为噪声
y1 = y0 + 2*np.random.randn(len(x))
#进行参数估计
Para = optimize.leastsq(error, p0, args=(x,y1))
A, k, theta = Para[0]
'''
图形可视化
'''
plt.figure(figsize=(20, 8))
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)

#在ax1区域绘图
plt.sca(ax1)
#绘制散点图
plt.scatter(x, y1, color='red', label='Sample Point', linewidth=3)
plt.xlabel('x')
plt.xlabel('y')
plt.plot(x, y0, color='black', label='sine', linewidth=2)

#在ax2区域绘图
plt.sca(ax2)
y = func(x, p0)
e = y-y1
plt.plot(x, e, color='orange', label='error', linewidth=1)

#显示图例和图形
plt.legend()
plt.show()