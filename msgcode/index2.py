import PIL.Image,PIL.ImageDraw,PIL.ImageFont,PIL.ImageFilter
import random

#随机字母
def rndchar():
    return chr(random.randint(65, 90))

#random.randint()函数生成随机数字，数字范围为在65 到90内,在此范围内的美国标准信息编码是大写的A-Z
#chr（kk） 函数，kk为整数，asc编码值，函数返回asc编码为kk 的对应的字符

#随机颜色1
def rndcolor():
    return random.randint(64, 255),random.randint(64, 255),random.randint(64, 255)

#随机颜色2
def rndcolor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

width = 60*4
height = 60
image = PIL.Image.new('RGB', (width, height), (255, 255, 255))

#RGB文件：RGB色彩模式是工业界的一种颜色标准，是通过对红®、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色的，RGB即是代表红、绿、蓝三个通道的颜色

#创建font对象
font = PIL.ImageFont.truetype('font.ttf', 36)

#加载一个TrueType或者OpenType字体文件，并且创建一个字体对象，这里的路径可以打开控制面板->字体->选择一种字体，将字体样式的路径复制到这里这个函数从指定的文件加载了一个字体对象，并且为指定大小的字体创建了字体对象。

#创建draw对象
draw = PIL.ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndcolor())

#输出文字
for t in range(4):
    draw.text((60*t+10, 10), rndchar(), font=font, fill=rndcolor2())

image = image.filter(PIL.ImageFilter.BLUR)
image.save('test2.png')