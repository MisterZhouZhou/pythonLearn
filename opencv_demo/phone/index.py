# coding=utf-8
import cv2
if __name__ == '__main__':

    cv2.namedWindow("camera", 0)
    # 开启ip摄像头
    video = "http://admin:admin@192.168.1.103:8081/"
    capture = cv2.VideoCapture(video)

    num = 0
    while True:
        ret, frame = capture.read()  # 读取一帧视频
        # frame = cv2.flip(frame, 1)  # 水平反转
        cv2.imshow("camera", frame)
        # 按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口
        key = cv2.waitKey(1)
        # 如果输入q则退出循环
        if key & 0xFF == 27:
            # esc键退出
            print("esc break...")
            break
        if key & 0xFF == ord(' '):
            # 保存一张图像
            num = num + 1
            filename = "frames_%s.jpg" % num
            cv2.imwrite(filename, frame)

    # 释放摄像头并销毁所有窗口
    capture.release()
    cv2.destroyAllWindows()