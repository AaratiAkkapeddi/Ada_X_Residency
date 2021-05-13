import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
import os

def paste_img(filename):
	if filename.endswith(".jpg"):
		blank_image = np.zeros((8000,8000,3), np.uint8)
		blank_image[:] = 255
		s_img = cv2.imread("./all_resized/"+filename)
		height = s_img.shape[0]
		width = s_img.shape[1]
		if width < 8000 and height < 8000:
			x_offset= int(4000 - (width/2))
			y_offset= int(4000 - (height/2))

			blank_image[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

			cv2.imwrite("test/"+filename, blank_image)


for filename in os.listdir('./all_resized/'):
    paste_img(filename)