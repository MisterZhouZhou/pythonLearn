import random
from PIL import Image, ImageDraw, ImageFont
# 图片宽高
width = 160
height = 50


def getRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def getRandomChar():
    random_num = str(random.randint(0, 9))
    random_lower = chr(random.randint(97, 122))  # 小写字母a~z
    random_upper = chr(random.randint(65, 90))  # 大写字母A~Z
    random_char = random.choice([random_num, random_lower, random_upper])
    return random_char

def drawLine(draw):
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=getRandomColor())


def drawPoint(draw):
    for i in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x,y), fill=getRandomColor())

def createImg():
    pwd = ''
    bg_color = getRandomColor()
    # 创建一张随机背景色的图片
    img = Image.new(mode="RGB", size=(width, height), color=bg_color)
    # 获取图片画笔，用于描绘字
    draw = ImageDraw.Draw(img)
    # 修改字体
    font = ImageFont.truetype(font="font.ttf", size=36)
    for i in range(5):
        # 随机生成5种字符+5种颜色
        random_txt = getRandomChar()
        pwd = pwd + random_txt
        txt_color = getRandomColor()
        # 避免文字颜色和背景色一致重合
        while txt_color == bg_color:
            txt_color = getRandomColor()
        # 根据坐标填充文字
        draw.text((10 + 30 * i, 3), text=random_txt, fill=txt_color, font=font)
    # 画干扰线点
    drawLine(draw)
    drawPoint(draw)
    # 打开图片操作，并保存在当前文件夹下
    with open("test.png", "wb") as f:
        img.save(f, format="png")
    return pwd

if __name__ == '__main__':
    pwd = createImg()
    print(pwd)