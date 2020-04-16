#Preprocessing the data before feeding it into the CNN
#
#
#Change environment with: conda activate pt-labi
# import av
import numpy as np
# from PIL import Image
from numpy import save
#from numpy import load # Use this to load the .npy arrays later
import math




#Open the .avi files, extract the frames, and turn them into numpy arrays

container = av.open('0Preprocessing_data\jAER_100^2_all_imgs_betterlables/jAER_simplest_by_hand_better.avi')

for frame in container.decode(video=0):
    frame.to_image().save('0Preprocessing_data/jAER_100^2_all_imgs_betterlables/frames/frame-%04d.jpg' % frame.index)

    image = Image.open('0Preprocessing_data/jAER_100^2_all_imgs_betterlables/frames/frame-%04d.jpg' % frame.index) # open the image and check the size
    xsize, ysize = image.size

    r, g, b = image.split()
    r_data = np.array(r.getdata())  # data is now an array of length ysize*xsize
    g_data = np.array(g.getdata())

    r_data = r_data.reshape(ysize, xsize)  # Reshape the image to a 2D-array
    g_data = g_data.reshape(ysize, xsize)

    divisor = 255  # divide every entry of the array by 255 to fit values between 0 and 1
    r_data = np.divide(r_data, divisor)
    g_data = np.divide(g_data, divisor)

    save('0Preprocessing_data/jAER_100^2_all_imgs_betterlables/r_data/r_data-%04d.npy' % frame.index, r_data)
    save('0Preprocessing_data/jAER_100^2_all_imgs_betterlables/g_data/g_data-%04d.npy' % frame.index, g_data)

    # data = load('r_data.npy')  # Use this to load the .npy arrays later






# read out locations.txt file, turn into numpy array and apply 2D Gaussian distribution
import numpy as np
import os
import sys
import pandas as pd
from numpy import save
from numpy import load

np.set_printoptions(threshold=sys.maxsize)


array_frames = []
count = 0

with open('./test.txt') as fp:
   line = fp.readline()
   while line:
      wholeLine = line.strip()
      if ('#' != wholeLine[0]):
         frame = np.zeros((100,100))
         data = wholeLine.split()
         x_converted = round((int(data[3]) / 240) * 100)
         y_converted = round((int(data[4]) / 180) * 100)
         if data[3] != "-1" or data[4] != "-1":
            if (x_converted >= 0) and (y_converted >= 0):
               for y in range(len(frame)):
                  y_array = frame[y]
                  for x in range(len(y_array)):
                     x_d = x - x_converted 
                     y_d = y - y_converted 
                     
                     distance = math.sqrt(x_d ** 2.0 + y_d ** 2.0) 
                     frame[x][y] = math.exp( - ((distance) ** 2.0))
   
            save(f'./output/label-{count}.npy',frame)
            count += 1


      line = fp.readline()


converted_frame = np.around(frame, decimals = 2)
