# -*- coding: UTF-8 -*-
import cv2

def CatchUsbVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)
    # 视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
    cap = cv2.VideoCapture(camera_idx)
    # 告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier("/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
    # 识别出人脸后要画的边框的颜色，RGB格式
    color = (0, 0, 255)
    # num = 0
    while cap.isOpened():
        ok, frame = cap.read() #读取一帧数据
        frame = cv2.flip(frame, 1)  # 水平反转
        if not ok:
            break
        # 将当前帧转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        # faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:  # 大于0则检测到人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x-10, y-10), (x + w + 10, y + h + 10), color, 2)
                # 显示当前捕捉到了多少人脸图片了，这样站在那里被拍摄时心里有个数
                # num += 1
                # fonts = cv2.FONT_HERSHEY_SIMPLEX
                # cv2.putText(frame, 'num:%d' % (num), (x + 30, y + 30), fonts, 1, (255, 0, 255), 4)
        # 显示图像
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(10)
        if key & 0xFF == ord('q'):
            break
    # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    CatchUsbVideo(r"识别人脸区域", 0)