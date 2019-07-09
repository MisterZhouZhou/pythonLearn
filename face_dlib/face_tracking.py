# -*- coding: utf-8 -*-
import cv2
import dlib

# 跟踪类
tracker = dlib.correlation_tracker()  # 导入correlation_tracker()类
cap = cv2.VideoCapture(0)             # opencv打开摄像头，参数为设备索引号，笔记本电脑，0表示使用其内置摄像头

selection = None     # 实时跟踪鼠标的跟踪区域
track_window = None  # 要检测的物体所在区域
drag_start = None    # 标记，是否开始拖动鼠标


# 鼠标点击事件回调函数
def onmouse(event, x, y, flags, param):
    global selection, track_window, drag_start  # 定义全局变量
    if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下
        drag_start = (x, y)  # 鼠标起始位置
        track_window = None
    if drag_start:  # 是否开始拖动鼠标，记录鼠标位置
        xmin = min(x, drag_start[0])
        ymin = min(y, drag_start[1])
        xmax = max(x, drag_start[0])
        ymax = max(y, drag_start[1])
        selection = (xmin, ymin, xmax, ymax)
    if event == cv2.EVENT_LBUTTONUP:  # 鼠标左键松开
        drag_start = None
        track_window = selection
        selection = None


def main():
    # 创建图像与窗口，并将窗口与回调函数绑定
    cv2.namedWindow('image', 1)
    cv2.setMouseCallback('image', onmouse)

    k = 0
    while (1):
        ret, frame = cap.read()  # 从摄像头读入1帧，ret表明成功与否
        if not ret:
            print("Game over!")
            break
        print("Processing Frame {}".format(k))
        img_raw = frame         # 初始帧
        image = img_raw.copy()  # 不改变初始帧，拷贝新的帧

        # 初始化第一帧
        if k == 0:
            # 用鼠标拖拽一个框来指定区域
            while True:
                img_first = image.copy()  # 不改变原来的帧，拷贝一个新的
                if track_window:  # 跟踪目标的窗口画出后，实时标出跟踪目标
                    cv2.rectangle(img_first, (track_window[0], track_window[1]), (track_window[2], track_window[3]),
                                  (0, 0, 255), 1)
                elif selection:  # 跟踪目标的窗口随鼠标拖动实时显示
                    cv2.rectangle(img_first, (selection[0], selection[1]), (selection[2], selection[3]), (0, 0, 255), 1)
                cv2.imshow('image', img_first)
                if cv2.waitKey(5) == 27:  # 等待时间为5ms,用户按下按下ESC(ASCII码为27)，退出循环
                    break
            print(track_window)
            tracker.start_track(image,
                                dlib.rectangle(track_window[0], track_window[1], track_window[2], track_window[3]))
        else:
            # 不是第一帧了
            tracker.update(image)  # 更新，实时跟踪
            # time.sleep(3)

        box_predict = tracker.get_position()  # 得到目标的位置
        cv2.rectangle(image, (int(box_predict.left()), int(box_predict.top())),
                      (int(box_predict.right()), int(box_predict.bottom())), (0, 255, 255), 1)
        cv2.imshow('image', image)

        c = cv2.waitKey(5)
        if c == 27: break  # 如果按下ESC，则退出
        k += 1
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()