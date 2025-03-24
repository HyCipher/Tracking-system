import argparse
import datetime
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

# 如果video参数为None,那么从摄像头直接读取数据
if args.get("video", None) is None:
    camera = cv2.VideoCapture(0)
    time.sleep(0.25)

# 否则读取第一个视频文件
else:
    camera = cv2.VideoCapture(args["video"])

# 初始化视频流的第一帧
firstFrame = None