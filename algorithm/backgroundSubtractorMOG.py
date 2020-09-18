import numpy as np
import cv2
import imageio

cap = cv2.VideoCapture(r"G:\SHU\Bird\dataBase\0909\bird distinguish\0914.avi")

fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg2 = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg3 = cv2.bgsegm.createBackgroundSubtractorGMG(60)  # initializationFrames=120

# 保存gif参数设置
gif1 = './backgroundSub/v1.gif'
gif2 = './backgroundSub/v2.gif'
gif3 = './backgroundSub/v3.gif'
frames1 = []
frames2 = []
frames3 = []

while True:
    ret, frame = cap.read()
    if not ret:
        print('not found')
        break
    frame = cv2.resize(frame, (400, 400), interpolation=cv2.INTER_CUBIC)

    # 前景掩码
    fgmask1 = fgbg1.apply(frame)
    fgmask2 = fgbg2.apply(frame)
    fgmask3 = fgbg3.apply(frame)

    fgmask4 = cv2.morphologyEx(fgmask3, cv2.MORPH_OPEN, kernel, iterations=1)  # 形态学开运算

    cv2.imshow('frame1', fgmask1)
    cv2.imshow('frame2', fgmask2)
    cv2.imshow('frame3', fgmask3)
    cv2.imshow('frame4', fgmask4)

    # 加入帧
    frames1.append(fgmask1)
    frames2.append(fgmask2)
    frames3.append(fgmask4)

    # 保存gif
    imageio.mimsave(gif1, frames1, 'GIF', duration=0.1)
    imageio.mimsave(gif2, frames2, 'GIF', duration=0.1)
    imageio.mimsave(gif3, frames3, 'GIF', duration=0.1)

    k = cv2.waitKey(100) & 0xff
    if k == 27 or k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()