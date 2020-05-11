import numpy as np
import cv2
import glob
import itertools
import random
import csv
import os, os.path

    
    
training_file_name = "training_model.csv"
testing_file_name = "testing_model.csv"


with open(training_file_name,'w') as file:

   images_path = "./Data/Dataset/"
   labels_path = "./Data/Labels/"

   images = glob.glob( images_path + "*.jpg"  )
   images.sort()
   labels  = glob.glob( labels_path + "*.png" )
   labels.sort()

   #check if label counts equals to image counts
   assert len(images) == len(labels) + 2
   for im , seg in zip(images,labels):
      count = 0
      if count >= 2:
         assert(im.split('-')[-1].split(".")[0] ==  seg.split('-')[-1].split(".")[0] )
      count += 1

   for i in range(2, len(images)): 
      file_name = images[i].split('-')[-1]
      file.write(images[i] + "," + images[i-1] + "," + images[i-2] + "," + labels[i-2] + "\n")



file.close()

lines = open(training_file_name).read().splitlines()

#70% for training, 30% for testing 
training_images_number = int(len(lines)*0.7)
testing_images_number = len(lines) - training_images_number
print("Total images:", len(lines), "Training images:", training_images_number,"Testing images:", testing_images_number)

#shuffle the images
# random.shuffle(lines)
#training images
with open(training_file_name,'w') as training_file:
    training_file.write("img, img1, img2, label\n")
    #testing images
    with open(testing_file_name,'w') as testing_file:
        testing_file.write("img, img1, img2, label\n")
        
        #write img, img1, img2, label to csv file
        for i in range(0,len(lines)):
            if lines[i] != "":
                if training_images_number > 0:
                    training_file.write(lines[i] + "\n")
                    training_images_number -=1
                else:
                    testing_file.write(lines[i] + "\n")
                    
training_file.close()
testing_file.close()
    

