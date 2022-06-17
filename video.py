import cv2
from genericpath import exists
import argparse
import os

parser = argparse.ArgumentParser(description='Converting Image Frames to Video Sequence')
parser.add_argument('--path', type=str, help='source folder datapath')
parser.add_argument('--fps', type=int, help='video fps',default=30)

args = parser.parse_args()

video_name = 'video.avi'

print('Converting ..')

images = [img for img in os.listdir(args.path) if img.endswith(".png")]
images.sort()
frame = cv2.imread(os.path.join(args.path, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, args.fps, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(args.path, image)))

cv2.destroyAllWindows()
video.release() 
