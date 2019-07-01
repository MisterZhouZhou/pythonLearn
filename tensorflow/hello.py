import tensorflow as tf

# 创建一个常量Operation
hw = tf.constant('Hello World!')
# 启动会话
sesstion = tf.compat.v1.Session()
# 允许Graph(计算图)
print(sesstion.run(hw))
# 关闭会话
sesstion.close()