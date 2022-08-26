import argparse
import glob
import cv2
import numpy as np
from datetime import datetime
import rasterio
from rasterio.plot import reshape_as_image
from natsort import natsorted

parser = argparse.ArgumentParser(description='Video pre-processing on frames data')
parser.add_argument('--fp', dest='frames_path', type=str, help='frames path')
parser.add_argument('--ff', dest='frame_format', type=str, help='original frame format file, ex: tif, png')
parser.add_argument('--vp', dest='video_path', type=str, help='video path')

def main(frames_path, frame_format, video_path):
    now = datetime.now()
    fnOut_avi = video_path + '/raw_video_' + str(now.year) + str(now.month) + str(now.day) + str(now.minute) + str(now.second) + str(now.microsecond) + '.avi'
    video_writer = cv2.VideoWriter(fnOut_avi, cv2.VideoWriter_fourcc(*'DIVX'), 3, (2560, 2560))
    files_path = natsorted(glob.glob(frames_path + "/*." + frame_format))
    video_data = []
    for file_path in files_path:
        frame = cv2.imread(file_path)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write data to AVI file
        video_writer.write(frame)

    #   Write the AVI file
    video_writer.release()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = parser.parse_args()
    main(args.frames_path, args.frame_format, args.video_path)