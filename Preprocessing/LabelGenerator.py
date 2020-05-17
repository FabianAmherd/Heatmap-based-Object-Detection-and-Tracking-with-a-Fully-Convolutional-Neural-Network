# Create the label for the CNN to learn from
# read out locations.txt file, create PIL Image, apply 2D Gaussian distribution to the label

from PIL import Image
import numpy as np
import os

count = 2  # How many frames of the .avi file from jAER do not have been labelled at the start of the video?
size = 10  # has to be large enough to render the whole blob, can create high-contrast  edges
variance = 10  # changes the size of the blob
label_width = 240  # label resolution
label_height = 180  # label resolution


# create gaussian heatmap
def gaussian_kernel(variance):
    x, y = np.mgrid[-size:size+1, -size:size+1]
    g = np.exp(-(x**2+y**2)/float(2*variance))
    return g 


gaussian_kernel_array = gaussian_kernel(variance)
gaussian_kernel_array = gaussian_kernel_array * 255/gaussian_kernel_array[int(len(gaussian_kernel_array)/2)][int(len(gaussian_kernel_array)/2)]
gaussian_kernel_array = gaussian_kernel_array.astype(int)


with open('Data/preprocessing/jAER_simplest_by_hand_better_240_180-targetLocations.txt') as fp:
    # Get the first line
    line = fp.readline()
    while line:
        wholeLine = line.strip()
        line = fp.readline()
        if '#' != wholeLine[0]:
            
            data = wholeLine.split()
            x = int(int(data[3]))
            y = label_height - int(int(data[4]))

            if data[3] != '-1' and data[4] != '-1':
                if (x >= 0) and (y >= 0):

                    heatmap = Image.new("RGB", (label_width, label_height))
                    pix = heatmap.load()
                    for i in range(label_height):
                        for j in range(label_width):
                            pix[j, i] = (0, 0, 0)

                    for i in range(-size, size+1):
                        for j in range(-size, size+1):
                            if x+j<label_width and x+j>=0 and y+i<label_height and y+i>=0:
                                temp = gaussian_kernel_array[j+size][i+size]
                                if temp > 0:
                                    pix[x+j, y+i] = (temp, temp, temp)

                    FileName = f'label-%04d' % count
                    if os.path.isfile(FileName):
                        heatmap.save("Data/traindir/labels/" + FileName + ".png", "PNG")
                    count += 1