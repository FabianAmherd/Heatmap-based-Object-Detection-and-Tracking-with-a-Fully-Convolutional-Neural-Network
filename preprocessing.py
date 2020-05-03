#Preprocessing the data before feeding it into the CNN


#Change environment with: conda activate pt-labi
import av
import numpy as np
from PIL import Image
from numpy import save
import math
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
array_frames = []
count = 2

with open('Data/preprocessing/jAER_simplest_by_hand_better_240_180-targetLocations.txt') as fp:
    # Get the first line
    line = fp.readline()
    while line:
        wholeLine = line.strip()
        if '#' != wholeLine[0]:
            frame = np.zeros((90, 120))
            data = wholeLine.split()
            x_converted = 90 - int(int(data[4])/2)
            y_converted = int(int(data[3])/2)
            if data[3] != '-1' and data[4] != '-1':
                if (x_converted >= 0) and (y_converted >= 0):
                    for y in range(120):
                        for x in range(90):
                            x_d = x - x_converted
                            y_d = y - y_converted

                            distance = math.sqrt(x_d ** 2.0 + y_d ** 2.0)
                            frame[x][y] = math.exp(- ((distance/3) ** 2.0))
                filename = f'Data/traindir/labels/label-%04d.npy' % count
                factor = 255
                frame = np.multiply(frame, factor)
                if os.path.isfile(filename):
                    save(filename, frame)
                count += 1

        line = fp.readline()
