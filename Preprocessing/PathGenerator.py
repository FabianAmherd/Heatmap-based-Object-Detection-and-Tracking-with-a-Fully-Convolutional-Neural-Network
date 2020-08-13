import glob
import random


training_file_name = "data.csv"
dataset_number = "036"

with open(training_file_name, 'w') as file:

   images_path = f"Data/Dataset_{dataset_number}/frames/"
   labels_path = f"Data/Dataset_{dataset_number}/labels/"

   images = glob.glob(images_path + "*.png")
   images.sort()
   labels = glob.glob(labels_path + "*.png")
   labels.sort()

   # check if label counts equals to image counts
   assert len(images) == len(labels)
   for im, seg in zip(images, labels):
      count = 0
      if count >= 2:
         assert(im.split('-')[-1].split(".")[0] == seg.split('-')[-1].split(".")[0] )
      count += 1

   for i in range(2, len(images)): 
      file_name = images[i].split('-')[-1]
      file.write(images[i] + "," + images[i-1] + "," + images[i-2] + "," + labels[i] + "\n")

file.close()


lines = open(training_file_name).read().splitlines()


# training images
with open(training_file_name, 'w') as training_file:
    training_file.write("img, img1, img2, label\n")
    for i in range(0, len(lines)):
        if lines[i] != "":
            training_file.write(lines[i] + "\n")
                    
                    
training_file.close()
    

