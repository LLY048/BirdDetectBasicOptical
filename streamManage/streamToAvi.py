import cv2
import sys


def save_avi(cap, outVideo, frames, part):
    if cap.isOpened():
        rval, frame = cap.read()
        # print('true')
    else:
        rval = False
        # print('False')
    tot = 1
    # c = 1
    # 循环使用cv2的read()方法读取视频帧
    while rval:
        rval, frame = cap.read()
        # cv2.imshow('live', frame)
        # 每间隔200帧保存一张图像帧
        if tot % 200 == 0:
            print('tot=', tot)
            # cv2.imwrite('cut/'+'cut_'+str(c)+'.jpg',frame)
            # c += 1
        tot += 1
        # print('tot=', tot)
        # 使用VideoWriter类中的write(frame)方法，将图像帧写入视频文件
        outVideo.write(frame)
        cv2.waitKey(25)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        if tot % int(frames) == 0:
            outVideo.release()
            part += 1
            part %= 3  # save three modules for the analysis
            break
    return part
    print("===========record finished==========")


def getconfigure(cap,  part):
    fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
    outVideo = cv2.VideoWriter('./video/saveDir'+str(part)+'.avi', fourcc, fps, size)
    return outVideo, fps


def stream2avi(url, seconds):
    part = 0
    count = 0
    cap = cv2.VideoCapture(url)
    while True:
        outVideo, fps = getconfigure(cap, part)
        print(fps)
        print("video clip " + str(count) + " starts")
        frameCount = fps*seconds
        part = save_avi(cap, outVideo, frameCount, part)
        print("video clip " + str(count) + " finished")
        count += 1
        if count == 4:
            break

# stream2avi(r"http://ivi.bupt.edu.cn/hls/cctv5phd.m3u8", 3)


