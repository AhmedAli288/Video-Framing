import cv2

vidcap = cv2.VideoCapture('video.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)
    return hasFrames

sec = 0

frameRate = 0.04

count = 1

while getFrame(sec):
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)