import numpy as np
import os
import sys
import pandas as pd
import math
from numpy import save
from numpy import load

np.set_printoptions(threshold=sys.maxsize)


array_frames = []
count = 0

with open('./test.txt') as fp:
  # Get the first line
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
   
            save(f'./converter-runs/label-{count}.npy',frame)
            count += 1


      line = fp.readline()


converted_frame = np.around(frame, decimals = 2)
