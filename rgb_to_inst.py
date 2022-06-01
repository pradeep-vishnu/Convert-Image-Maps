from genericpath import exists
import numpy as np
import argparse
import os
from torchvision.datasets.folder import default_loader
from PIL import Image as im
import glob

parser = argparse.ArgumentParser(description='Converting RGB Segmentation maps to Instance Maps')
parser.add_argument('--path', type=str, help='source folder datapath')
parser.add_argument('--imagewidth', type=int, help='source image width',default=2048)
parser.add_argument('--imageheight', type=int, help='source image height', default=1024)
parser.add_argument('--savepath', type=str, help='save path for converted files',default='./save/')
args = parser.parse_args()

os.makedirs(args.savepath, exist_ok=True)

color = [(70, 70, 70),(100, 40, 40),(55, 90, 80),(220, 20, 60),(153, 153, 153),(157, 234, 50),(128, 64, 128),
         (244, 35, 232),(107, 142, 35),(0, 0, 142),(102, 102, 156),(220, 220, 0),(70, 130, 180),(81, 0, 81),
        (150, 100, 100),(230, 150, 140),(180, 165, 180),(250, 170, 30),(110, 190, 160),(170, 120, 50),
         (45, 60, 150),(145, 170, 100)]

print('Converting ..')

for file in glob.glob(os.path.join(args.path, '*.png')):
    label = default_loader(file)
    label = np.array(label)
    _,file_name = os.path.split(file)
    i=0
    while(i<args.imageheight):
        j=0
        while(j<args.imagewidth):
            label[i][j]=np.array([np.where(label[i][j]==color)[0][0],0,0])
            j=j+1
        i=i+1
    data = im.fromarray(label, 'RGB')
    data.save(args.savepath+file_name)
    print(file_name+' : sucess')

print('.. Completed')