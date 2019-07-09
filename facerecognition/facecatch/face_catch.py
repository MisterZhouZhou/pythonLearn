#-*- coding: utf-8 -*-
import cv2, json
from facerecognition.facecatch.face_train import Model

class Face_recognition():
    def __init__(self):
        with open('contrast_table', 'r') as f:
            self.contrast_table = json.loads(f.read())
        self.model = Model()
        self.model.load_model(file_path='../model/zhouwei.face.model.h5')
        # 框住人脸的矩形边框颜色
        self.color = (0, 255, 0)

        # 捕获指定摄像头的实时视频流
        self.cap = cv2.VideoCapture(0)

        # 人脸识别分类器本地存储路径
        self.cascade_path = "/usr/local/libs/python3.7/site-packages/cv2/data/haarcascade_frontalface_alt2.xml"
        # self.cascade_path = "/usr/local/libs/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml"

    def recongition(self):
        while True:
            ret, frame = self.cap.read()  # 读取一帧视频
            frame = cv2.flip(frame, 1)  # 水平反转
            if ret is True:
                # 图像灰化，降低计算复杂度
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            else:
                continue
            # 使用人脸识别分类器，读入分类器
            cascade = cv2.CascadeClassifier(self.cascade_path)

            # 利用分类器识别出哪个区域为人脸
            faceRects = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
            if len(faceRects) > 0:
                for faceRect in faceRects:
                    x, y, w, h = faceRect
                    # 截取脸部图像提交给模型识别这是谁
                    image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                    probability, name_number = self.model.face_predict(image)
                    name = self.contrast_table[str(name_number)]
                    cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), self.color, thickness=2)
                    # 文字提示是谁
                    # cv2.putText(frame, name, (x + 30, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                    print('probability=',probability)
                    if probability > 0.7:
                        cv2.putText(frame, name, (x + 30, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                    else:
                        cv2.putText(frame, 'unknow', (x + 30, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow("face_recognition", frame)
            # 等待10毫秒看是否有按键输入
            k = cv2.waitKey(10)
            # 如果输入q则退出循环
            if k & 0xFF == ord('q'):
                break
        # 释放摄像头并销毁所有窗口
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    fr = Face_recognition()
    fr.recongition()