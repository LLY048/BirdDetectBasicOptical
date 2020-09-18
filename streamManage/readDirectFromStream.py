import cv2
import os
from algorithm.twoFrameSub import subjectDetect
from SRS.pushFlv import pushFlv
# import subprocess

# VIDEO_URL = 'http://ivi.bupt.edu.cn/hls/cctv5phd.m3u8'
# timeSeg = 100
# fourcc = cv2.VideoWriter_fourcc('a','v','c','1')
# outVideoDir = '../video/partVideo.mp4'
# reSize = (500, 400)
# root_path = r"E:\FFMPEG\ffmpeg-20200831-4a11a6f-win64-static\bin\ffmpeg.exe"


def streamToFrame(url, timeSeg, outVideoDir, reSize, fourcc):
    cap = cv2.VideoCapture(url)
    if not cap.isOpened():
        print("Stream Stopped")
    fps = cap.get(cv2.CAP_PROP_FPS)
    wait_ms = int(1000/fps)
    print('FPS:', fps)
    lastFrame = None
    frameSegSize = timeSeg*fps
    frameCount = 0
    outVideo = cv2.VideoWriter(outVideoDir, fourcc, fps, reSize)
    resultList = []
    while True:
        ret, frame = cap.read()
        # process
        frameCount += 1
        if not ret:
            print("no more frame to process")
            break
        frame = cv2.resize(frame, reSize, interpolation=cv2.INTER_CUBIC)
        # cv2.imshow('frame', frame)
        if lastFrame is None:
            lastFrame = frame
            continue
        frame, targetList = subjectDetect(frame, lastFrame)
        # print(targetList)
        lastFrame = frame.copy()
        outVideo.write(frame)
        if frameCount % fps == 1:
            resultList.append(targetList)
        if frameCount == frameSegSize:
            outVideo.release()
            pushFlv()
            break
            os.remove(outVideoDir)
            frameCount = 0
            outVideo = cv2.VideoWriter(outVideoDir, fourcc, fps, reSize)
        if cv2.waitKey(wait_ms) & 0xFF == ord('q'):
            break
    cap.release()
    print('all process stopped')
    return resultList



# streamToFrame(VIDEO_URL, timeSeg, outVideoDir, reSize, fourcc)
# root_path = r"E:\FFMPEG\ffmpeg-20200831-4a11a6f-win64-static\bin\ffmpeg.exe"
# file_name_path = r"G:\SHU\Bird\basicOptical\video\partVideo.mp4"
# server_address = "127.0.0.1"
# ts_filename = "partVideo"
# mp4ToTs = root_path+" -y -i "+file_name_path+" -codec copy -bsf h264_mp4toannexb -map 0 -f segment -segment_list partVideo.m3u8 -segment_time 1 "+ts_filename+".ts"
# tsToM3u8 = root_path+" -i "+ts_filename+".ts -c copy -map 0 -f segment -segment_time 10 -segment_list "+ts_filename+".m3u8 "+ts_filename+"%03d.ts"
# mp4ToServer = root_path + ' -y -i ' + file_name_path + ' -c:v copy -c:a copy -f hls -hls_flags split_by_time -hls_time 1 ../u3m8/high.m3u8'

# mp4ToServer = root_path + ' -re -y -i ' + file_name_path + ' -vcodec copy -acodec copy -f flv rtmp://'+server_address+'/live/livestream'
# subprocess.call(mp4ToServer, shell=True)
# subprocess.call(tsToM3u8, shell=True)