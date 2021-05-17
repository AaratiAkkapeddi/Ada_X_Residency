import os
import PIL
from PIL import Image

def convert_image(filename):
	if filename.endswith(".jpg"): #check file type is a jpg
	    im = Image.open('./frames/'+ filename)
	    im.transpose(PIL.Image.FLIP_LEFT_RIGHT).save('./flipped/' + filename,
	                           'JPEG',
	                           quality_mode='dB',
	                           quality_layers=[41]) #save flipped version in a different directory


for filename in os.listdir('./frames'):
     convert_image(filename)