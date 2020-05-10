#Preprocessing the data before feeding it into the CNN


#Change environment with: conda activate pt-labi
#import av
# import numpy as np
# from PIL import Image
# from numpy import save
# import math
# import os

import glob
import csv
import numpy
import matplotlib.pyplot as plt
from PIL import Image
import os 

#Open the .avi files, extract the frames, and turn them into numpy arrays
#
# container = av.open('Data/preprocessing/jAER_simplest_by_hand_better_240_180.avi')
#
# for frame in container.decode(video=0):
#     frame.to_image().save('Data/preprocessing/frames/frame-%04d.jpg' % frame.index)
#
#     image = Image.open('Data/preprocessing/frames/frame-%04d.jpg' % frame.index) # open the image and check the size
#     xsize, ysize = image.size
#
#     r, g, b = image.split()
#     r_data = np.array(r.getdata())  # data is now a 1D array of length ysize*xsize
#     g_data = np.array(g.getdata())
#
#     r_data = r_data.reshape(ysize, xsize)  # Reshape the image to a 2D-array
#     g_data = g_data.reshape(ysize, xsize)
#
#     filename_r = 'Data/testdir/r_data/r_data-%04d.npy' % frame.index
#     filename_g = 'Data/testdir/g_data/g_data-%04d.npy' % frame.index
#     if os.path.isfile(filename_r):
#         save(filename_r, r_data)
#
#     if os.path.isfile(filename_g):
#         save(filename_g, g_data)


# read out locations.txt file, turn into numpy array and apply 2D Gaussian distribution
# array_frames = []

count = 2

size = 10
#create gussian heatmap 
def gaussian_kernel(variance):
    x, y = numpy.mgrid[-size:size+1, -size:size+1]
    g = numpy.exp(-(x**2+y**2)/float(2*variance))
    return g 



variance = 10
gaussian_kernel_array = gaussian_kernel(variance)
#rescale the value to 0-255
gaussian_kernel_array =  gaussian_kernel_array * 255/gaussian_kernel_array[int(len(gaussian_kernel_array)/2)][int(len(gaussian_kernel_array)/2)]
#change type as integer
gaussian_kernel_array = gaussian_kernel_array.astype(int)

width = 240
height = 180

with open('Data/preprocessing/jAER_simplest_by_hand_better_240_180-targetLocations.txt') as fp:
    # Get the first line
    line = fp.readline()
    while line:
        wholeLine = line.strip()
        line = fp.readline()
        if '#' != wholeLine[0]:
            
            data = wholeLine.split()
            x = int(int(data[3]))
            y = height - int(int(data[4]))

            if data[3] != '-1' and data[4] != '-1':
                if (x >= 0) and (y >= 0):

                    heatmap = Image.new("RGB", (width, height))
                    pix = heatmap.load()
                    for i in range(height):
                        for j in range(width):
                                pix[j,i] = (0,0,0)

                    for i in range(-size,size+1):
                        for j in range(-size,size+1):
                                if x+j<width and x+j>=0 and y+i<height and y+i>=0 :
                                    temp = gaussian_kernel_array[j+size][i+size]
                                    if temp > 0:
                                        pix[x+j,y+i] = (temp,temp,temp)

                    
                    FileName = f'label-%04d' % count
                    heatmap.save("Data/Labels/" + FileName + ".png", "PNG")
                    count += 1

        
