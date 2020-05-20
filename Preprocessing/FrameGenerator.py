import av
import cv2
from PIL import Image
import numpy as np

container = av.open('jAER_simplest_by_hand_better_240_180_20052020.avi')
for frame in container.decode(video=0):
    img = frame.to_image()

    aps_frame = img.crop((0, 0, 240, 180)).getchannel(0)
    dvs_frame = img.crop((240, 0, 480, 180)).getchannel(0)

    aps_frame = np.expand_dims(np.array(aps_frame), 2)
    dvs_frame = np.expand_dims(np.array(dvs_frame), 2)
    zero_blue = np.zeros((180, 240, 1))

    img = np.concatenate((aps_frame, dvs_frame, zero_blue), axis=2)
    img = Image.fromarray(img.astype(np.uint8))
    img.save('../frames/frame-%04d.png' % frame.index)
