import cv2  
import numpy as np
import os

def crop_img(filename):
	if filename.endswith(".jpg"):
		image = cv2.imread("./all_pasted/"+filename)
		h, w, channels = image.shape
		x = w/2
		y = h/2

		crop_img = image[int(y-1000):int(y+1000), int(x-1000):int(x+1000)]
		cv2.imwrite("test/"+filename, crop_img)


for filename in os.listdir('./all_pasted/'):
    crop_img(filename)