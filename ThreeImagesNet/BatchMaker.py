import numpy as np
import cv2
import itertools
import csv
import sys
from collections import defaultdict
import av
#np.set_printoptions(threshold=sys.maxsize)

def ThreeImagesInput(path, path1, path2):

      
   img = cv2.imread(path, 1)
   img = img[:,:,2]
   img = img.astype(np.float32)
   img = img / 255

   img1 = cv2.imread(path1, 1)
   img1 = img1[:,:,2]
   img1 = img1.astype(np.float32)
   img1 = img1 / 255

   img2 = cv2.imread(path2, 1)
   img2 = img2[:,:,2]
   img2 = img2.astype(np.float32)
   img2 = img2 / 255

   imgs = np.dstack((img, img1, img2))

   return imgs

def Labels(path):
   img = cv2.imread(path, 1)
   img = img.astype(np.float32)
   img = img[:, :, 0] / 255
   return img
   

def BatchMaker(images_path, batch_size):

   columns = defaultdict(list)
   with open(images_path) as f:
      reader = csv.reader(f)
      reader.__next__()
      for row in reader:
         for (i, v) in enumerate(row):
            columns[i].append(v)

   zipped = itertools.cycle(zip(columns[0], columns[1], columns[2], columns[3]))

   while True:
      Input = []
      Output = []
      for _ in range(batch_size):
         path, path1, path2, label = zipped.__next__()
         Input.append(ThreeImagesInput(path, path1, path2))
         Output.append(Labels(label))

      yield np.array(Input), np.array(Output)