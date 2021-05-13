import cv2
import os
#https://github.com/ageitgey/face_recognition
import face_recognition


def center_face(filename):
    # Check file extension to filter out .DS_Store files *note you'll have to compesate for multiple image file types here
    if filename.endswith(".jpeg"):
        # Read the input image
        img = cv2.imread('/Users/aarati/Desktop/batch/all/' + filename)
        # Detect faces
        faces = face_recognition.face_locations(img)
        #counter for output file name differentiation
        counter = 0
        #iterate through each of the found faces and center an output image on each face
        for (top, right, bottom, left) in faces:
            # find center of face
            faceCenterX = int(left + ((right - left) / 2))
            faceCenterY = int(top + ((bottom - top) / 2))
            # find center of image
            (imageH, imageW) = img.shape[:2]
            imgCenterX = int(imageW / 2)
            imgCenterY = int(imageH / 2)
            top = 0
            bottom = 0
            left = 0
            right = 0
            #figure out how much we need to compensate on which sides to center the face in the middle of the image
            if imgCenterX > faceCenterX:
                left = (imgCenterX - faceCenterX) * 2
            else:
                right = (faceCenterX - imgCenterX) * 2
            if imgCenterY > faceCenterY:
                top = (imgCenterY - faceCenterY) * 2
            else:
                bottom = (faceCenterY - imgCenterY) * 2
            #create a white border in the areas where the image needs to be extended in order to center the face
            roi = cv2.copyMakeBorder(img, int(top), int(
                bottom), int(left), int(right), cv2.BORDER_CONSTANT, value=[255,255,255] )
            counter = counter + 1
            # Saving the image
            cv2.imwrite("test/" + filename.split(".jpg")
                        [0] + str(counter) + ".jpg", roi)

#iterate through folder of images
for filename in os.listdir('/Users/aarati/Desktop/batch/all/'):
    center_face(filename)
