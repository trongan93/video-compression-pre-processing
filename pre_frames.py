import argparse
import glob
from pathlib import Path
import cv2
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Pre-processing on frames data')
parser.add_argument('--op', dest='original_frames_path', type=str, help='original frames path')
parser.add_argument('--oformat', dest='original_file_format', type=str, help='original frame format file, ex: tif, png')
parser.add_argument('--dp', dest='destination_frames_path', type=str, help='destination frames path')

_new_frame_size = [2560,2560]

def convert_resize_image(file_path):
    # print('test resize_image: '+ file_path + new_file_path + str(new_width) + str(new_height))
    org_img = cv2.imread(file_path)
    gray_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
    org_height = gray_img.shape[0]
    org_width = gray_img.shape[1]
    # print(org_height)
    # print(org_height/_new_frame_size[0])
    # print(org_width)
    # print(org_width/_new_frame_size[1])

    if org_height/_new_frame_size[0] < org_width/_new_frame_size[1]:
        scale = org_height/_new_frame_size[0]
    else:
        scale = org_width / _new_frame_size[1]
    if scale < 1:
        dim = (int(org_width/scale),int(org_height/scale))
    elif scale > 1:
        dim = (int(org_width * scale), int(org_height * scale))
    else:
        dim = (int(_new_frame_size[1]),int(_new_frame_size[0]))
    print(dim)
    scale_resize = cv2.resize(gray_img, dim, interpolation = cv2.INTER_CUBIC)
    # plt.imshow(scale_resize)
    # plt.show()
    return scale_resize

def save_img(image, file_name):
    cv2.imwrite(file_name, image)
    print("Successful to save ", file_name)

def main(original_frames_path, original_file_format, destination_frame_path):
    files_path =glob.glob(original_frames_path + "/*." + original_file_format)
    for file_path in files_path:
        new_file_name = destination_frame_path + "/" + Path(file_path).name
        resized_img = convert_resize_image(file_path)
        save_img(resized_img, new_file_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = parser.parse_args()
    main(args.original_frames_path, args.original_file_format, args.destination_frames_path)


