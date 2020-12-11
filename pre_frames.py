import argparse
import glob

parser = argparse.ArgumentParser(description='Pre-processing on frames data')
parser.add_argument('--op', dest='original_frames_path', type=str, help='original frames path')
parser.add_argument('--oformat', dest='original_file_format', type=str, help='original frame format file, ex: tif, png')
parser.add_argument('--dp', dest='destination_frames_path', type=str, help='destination frames path')


def main(original_frames_path, original_file_format, destination_frame_path):

    files_path =glob.glob(original_frames_path + "/*." + original_file_format)
    for file_path in files_path:
        print(file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = parser.parse_args()
    main(args.original_frames_path, args.original_file_format, args.destination_frames_path)


