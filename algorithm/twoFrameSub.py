import cv2


def subjectDetect(frame, lastFrame):
    # 计算当前帧和前帧的不同
    frameDelta = cv2.absdiff(lastFrame, frame)

    # 结果转为灰度图
    thresh = cv2.cvtColor(frameDelta, cv2.COLOR_BGR2GRAY)

    # 图像二值化
    thresh = cv2.threshold(thresh, 25, 255, cv2.THRESH_BINARY)[1]

    ''' 
    #去除图像噪声,先腐蚀再膨胀(形态学开运算) 
    thresh=cv2.erode(thresh,None,iterations=1) 
    thresh = cv2.dilate(thresh, None, iterations=2) 
    '''
    targetList = []

    # 阀值图像上的轮廓位置
    cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历轮廓
    count = 0
    for c in cnts:
        # 忽略小轮廓，排除误差
        if (cv2.contourArea(c)) < 10 or (cv2.contourArea(c) > 80):
            continue
        # 计算轮廓的边界框，在当前帧中画出该框
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        placeIndex = {
            'x': x,
            'y': y,
            'w': w,
            'h': h
        }
        ojbect = {
            "id": count,
            "place": placeIndex
        }
        targetList.append(ojbect)
        count += 1
    return frame, targetList