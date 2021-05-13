import os
import face_recognition
import numpy as np
import shutil 

#script for finding unique faces and grouping images by face
#array of unique face encodings
known_face_encodings = []

def convert_image(filename):
	file = '/Users/aarati/Desktop/batch/all/' + filename
	image = face_recognition.load_image_file(file)
	encodings = face_recognition.face_encodings(image)
	#check if it's an image file...
    if filename.endswith(".jpg"):
    	#iterate through found faces
		for encoding in encodings:
			# if it's the first face in our list append it.
			if len(known_face_encodings) == 0:
				known_face_encodings.append(encoding)
			else: #otherwise check against all faces in list to compare and see if it's unique or already exists in our array
				print(known_face_encodings)
				results = face_recognition.compare_faces(known_face_encodings, encoding)
				distances = face_recognition.face_distance(known_face_encodings, encoding)
				print(distances)
				isitnew = True
				for distance in distances:
					if distance < 0.4: #adjust threshold for comparison here
						isitnew = False
				if isitnew:
					known_face_encodings.append(encoding)
					if not os.path.isdir("/Users/aarati/Desktop/test2/"+str((len(known_face_encodings)- 1))+"/"):
						os.mkdir(str((len(known_face_encodings)- 1)))
					shutil.copy(file, str((len(known_face_encodings)- 1)) +"/"+ filename)	
					print(str((len(known_face_encodings)- 1)) +"/"+ filename)
					print(known_face_encodings)
				else:
					for i,x in enumerate(distances):
						if x < 0.4:
							print("/Users/aarati/Desktop/test2/"+str(i) + "/")
							if not os.path.isdir("/Users/aarati/Desktop/test2/"+str(i) + "/"):
								os.mkdir(str(i))
							shutil.copy(file, str(i) +"/"+ filename)
			
		if len(encodings) == 0:
			shutil.copy(file, "none/"+ filename)
		#shutil.copy(file, i +"/"+ filename)			
#in the end you will have a series of folders for each "unique" face. Although it's quite messy and full of mistakes
for filename in os.listdir('/Users/aarati/Desktop/batch/all/'):
     convert_image(filename)

print(len(known_face_encodings)	)