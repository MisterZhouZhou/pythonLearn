# coding:utf-8
import cv2

cv2.namedWindow('W1', 0)
cv2.resizeWindow('W1', 600, 480)
cv2.moveWindow("trans:", 1000, 100)

def test():

    # 框住人脸的矩形边框颜色
    color = (0, 255, 0)
    # 捕获指定摄像头的实时视频流
    cap = cv2.VideoCapture(0)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # 循环检测识别人脸
    while True:
        ret, frame = cap.read()  # 读取一帧视频
        frame = cv2.flip(frame, 1)  # 水平反转
        if ret is True:
            # 图像灰化，降低计算复杂度
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            continue
        width = size[0]
        height = size[1]
        divide_x = width // 3
        divide_y = height // 3
        # 画图像分割线
        cv2.line(frame, (divide_x, 0), (divide_x, height), (0, 255, 255), 1)
        cv2.line(frame, (2*divide_x, 0), (2*divide_x, height), (0, 255, 255), 1)
        cv2.line(frame, (0, divide_y), (width, divide_y), (0, 255, 255), 1)
        cv2.line(frame, (0, 2*divide_y), (width, 2*divide_y), (0, 255, 255), 1)

        # 使用人脸识别分类器，读入分类器
        cascade = cv2.CascadeClassifier("/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_alt2.xml")
        # 利用分类器识别出哪个区域为人脸
        faceRects = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=1, minSize=(32, 32))
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect
                if x < divide_x:
                    print('left')
                elif x > 2*divide_x:
                    print("right")
                else:
                    print('center')
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness=2)
                cv2.imshow("W1", frame_gray)

        cv2.imshow("W1", frame)
        # 等待10毫秒看是否有按键输入
        k = cv2.waitKey(1)
        # 如果输入q则退出循环
        if k & 0xFF == ord('q'):
            break

    # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    test()