import argparse
import glob
import cv2
import numpy as np
from datetime import datetime

parser = argparse.ArgumentParser(description='Video pre-processing on frames data')
parser.add_argument('--fp', dest='frames_path', type=str, help='frames path')
parser.add_argument('--ff', dest='frame_format', type=str, help='original frame format file, ex: tif, png')
parser.add_argument('--vp', dest='video_path', type=str, help='video path')

def main(frames_path, frame_format, video_path):
    files_path = sorted(glob.glob(frames_path + "/*." + frame_format))
    video_data = []
    for file_path in files_path:
        frame = cv2.imread(file_path, 0)
        video_data.append(frame)

    video = np.asarray(video_data)
    out = video
    print('output image shape:', out.shape, 'data type', out.dtype)
    now = datetime.now()
    # print(datetime.now().strptime("%Y_%m_%d_%H_%M_%S"))
    fnOut = video_path + '/raw_video_' + str(now.year) + str(now.month) + str(now.day) + str(now.minute) + str(now.second) + str(now.microsecond) + '.yuv'
    fo = open(fnOut, 'wb')
    fo.write(out)
    fo.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = parser.parse_args()
    main(args.frames_path, args.frame_format, args.video_path)