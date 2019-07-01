### 22，验证码识别
import cv2 as cv
from PIL import Image
import pytesseract as tess


def recognize_Text(image):
    # 转化为灰度图像
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 将灰度图像二值化
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # 定义一个形态学处理的[1*2]的矩形结构核
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))
    # 对图像进行开运算去掉噪声点与干扰线
    open_out = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow("binary_image", open_out)
    ##将array形式图像变为Image
    textImage = Image.fromarray(open_out)
    # 利用模块中的方法识别
    text = tess.image_to_string(textImage)
    print("识别结果: %s" % text)


# （只能识别数字，鸡肋）
src = cv.imread(r'test2.png')
# cv.imshow("src", src)
recognize_Text(src)
cv.waitKey(0)
cv.destroyAllWindows()