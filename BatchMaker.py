import numpy as np
import cv2
import itertools
import csv
import sys
from collections import defaultdict
import datetime

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

   return img

def Labels(path):
   img = cv2.imread(path, 1)
   img = img.astype(np.float32)
   img = img[:, :, 0] / 255
   return img
   

def BatchMaker(images_path):
   count = 0
   columns = defaultdict(list)
   with open(images_path) as f:
      reader = csv.reader(f)
      reader.__next__()
      for row in reader:
         count += 1
         for (i, v) in enumerate(row):
            columns[i].append(v)

   zipped = itertools.cycle(zip(columns[0], columns[1], columns[2], columns[3]))

   Training_Input = []
   Training_Output = []
   Validation_Input = []
   Validation_Output = []

   with open('Preprocessing/jAER_simplest_by_hand_better_240_180-targetLocations.txt') as fp:
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()
      line = fp.readline()

      training = 0
      validation = 0
      for _ in range(count):
         path, path1, path2, label = zipped.__next__()
         Img = Labels(label)
         
         line = fp.readline()
         wholeLine = line.strip()
         data = wholeLine.split()
         x_coordinate = int(int(data[3]))
         y_coordinate = 180 - int(int(data[4]))

         if y_coordinate > 90 and x_coordinate > 120:
            Validation_Input.append(ThreeImagesInput(path, path1, path2))
            Validation_Output.append(Labels(label))
            validation += 1

         else:
            Training_Input.append(ThreeImagesInput(path, path1, path2))
            Training_Output.append(Labels(label))
            training += 1

      print(f"number of training frames: {training}, number of validation frames: {validation}")
      return np.array(Training_Input), np.array(Training_Output), np.array(Validation_Input), np.array(Validation_Output)
