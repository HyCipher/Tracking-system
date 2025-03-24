import motion_detector as md
import argparse
import cv2
import time


def cam_or_video(args):
    # 如果video参数为None,那么从摄像头直接读取数据
    if args.get("video", None) is None:
        camera = cv2.VideoCapture(0)
        time.sleep(0.25)

    # 否则读取第一个视频文件
    else:
        camera = cv2.VideoCapture(args["video"])
    return camera


# 创建参数解析器并解析参数
def pre_parse():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", help="path to the video file")
    ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
    args = vars(ap.parse_args())
    return args


def main():
    args = pre_parse()
    args['video'] = "dataset/Screen Recording 2025-03-24 at 17.13.42.mov"
    args['min_area'] = 500
    camera = cam_or_video(args)
    md.test(camera, args)


if __name__ == '__main__':
    main()
