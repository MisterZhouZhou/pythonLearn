import cv2 as cv

def video_demo():
    count = 1
    saveDir = '/Users/zhouwei/Desktop/python/pythonLearn/opencv/'
    capture = cv.VideoCapture(0)
    width, height, w = 640, 480, 360
    capture.set(cv.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, height)
    crop_w_start = (width - w) // 2
    crop_h_start = (height - w) // 2
    ret, frame = capture.read()  # 获取相框
    frame = frame[crop_h_start:crop_h_start + w, crop_w_start:crop_w_start + w]  # 展示相框
    frame = cv.flip(frame, 1, dst=None)  # 前置摄像头获取的画面是非镜面的，即左手会出现在画面的右侧，此处使用flip进行水平镜像处理
    cv.imshow("capture", frame)
    cv.imwrite("%s/%d.jpg" % (saveDir, count), cv.resize(frame, (224, 224), interpolation=cv.INTER_AREA))
    print(u"%s: %d 张图片" % (saveDir, count))

    # if action == ord('q'):
    #     break
    # while True:
    #     ret, frame = capture.read()  # 获取相框
    #     frame = frame[crop_h_start:crop_h_start + w, crop_w_start:crop_w_start + w]  # 展示相框
    #     frame = cv.flip(frame, 1, dst=None)  # 前置摄像头获取的画面是非镜面的，即左手会出现在画面的右侧，此处使用flip进行水平镜像处理
    #     cv.imshow("capture", frame)
        # action = cv.waitKey(1000) & 0xFF
        # print(action)
        # if action == ord('p'):
        #     cv.imwrite("%s/%d.jpg" % (saveDir, count), cv.resize(frame, (224, 224), interpolation=cv.INTER_AREA))
        #     print(u"%s: %d 张图片" % (saveDir, count))
        #     count += 1
        # if action == ord('q'):
        #     break

    capture.release()  # 释放摄像
    cv.destroyAllWindows()  # 丢弃所有窗口

if __name__ == '__main__':
    video_demo()