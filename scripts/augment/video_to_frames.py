import sys
import argparse

import cv2

vidcap = cv2.VideoCapture("1.mp4") #load video
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  if count % 3 == 0:
	  print ('Read a new frame: ', success)
	  if success:
	  	cv2.imwrite('./frames/' + "frame%d.jpg" % count, image)     # save frame as JPEG file in assumed pre-existing /frames folder 
  count += 1	  