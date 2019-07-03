# coding=utf-8

'''
 摄像机角度偏移告警
'''
import cv2
import do_match
import numpy as np
from PIL import Image, ImageDraw, ImageFont

'''
 告警信息
'''
def putText(img, text):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype("fonts/simsun.ttc", 30, encoding="utf-8")
    # 绘制文本
    draw.text((50, 50), text, (0, 0, 255), font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

if __name__ == '__main__':
    texts = ["完全偏移", "严重偏移", "轻微偏移", "无偏移"]
    cap = cv2.VideoCapture(0)
    if (cap.isOpened() == False):
        print("Error opening video stream or file")
        import sys
        sys.exit(0)

    first_frame = True
    pre_frame = 0
    index = 0
    while (cap.isOpened()):
        # 获取视频第一帧
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # 水平反转
        if ret == True:
            if first_frame:
                pre_frame = frame
                first_frame = False
                continue
            index += 1
            if index % 24 == 0:
                result = do_match.match2frames(pre_frame, frame)
                print("检测结果===>", texts[result])
                #  应该存在一个问题，就是缓慢调节移动时，严重偏移可以调节
                if result > 1:  # 缓存最近无偏移的帧
                    pre_frame = frame
                size = frame.shape
                if size[1] > 720:  # 缩小显示
                    frame = cv2.resize(frame, (int(size[1] * 0.5), int(size[0] * 0.5)), cv2.INTER_LINEAR)
                text_frame = putText(frame, texts[result])
                # cv2.putText(frame, texts[result],
                #             (50, 50),  # 坐标
                #             cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                #             1,  # 字号
                #             (255, 0, 255),  # 颜色
                #             2)  # 字的线宽
                cv2.imshow('Frame', text_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()