import cv2
import os
import face_recognition
import re
# script to resize each image in a folder so that all the central faces are 100px in width


def resize_by_face(filename):
    # Load the cascade
    print(filename)
    if filename.endswith(".jpg"):
        # Read the input image
        imgOg = cv2.imread('./test/' + filename)
        img = face_recognition.load_image_file('./test/' + filename)
        # Convert into grayscale
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        faces = face_recognition.face_locations(img)
        # Draw rectangle around the faces
        counter = 0
        face_distance = 1000000
        face = ""
        for (top, right, bottom, left) in faces:
            faceCenterX = int(left + ((right - left) / 2))
            faceCenterY = int(top + ((bottom - top) / 2))
            (imageH, imageW) = img.shape[:2]
            imgCenterX = int(imageW / 2)
            imgCenterY = int(imageH / 2)
            result = ((((imgCenterX - faceCenterX)**2) + ((imgCenterY - faceCenterY)**2))**0.5)
            if abs(result) < face_distance:
                face_distance = abs(result)
                face = [top, right, bottom, left, result]

        if face != "":
            print(face[4])
            top = face[0]
            right = face[1]
            bottom = face[2]
            left = face[3]
            faceCenterX = int(left + ((right - left) / 2))
            faceCenterY = int(top + ((bottom - top) / 2))
            (imageH, imageW) = img.shape[:2]
            imgCenterX = int(imageW / 2)
            imgCenterY = int(imageH / 2)
            w = right - left
            scale_percent = (100 / w) * 100
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dsize = (width, height)
            counter = counter + 1
            # Saving the image
            roi = cv2.resize(imgOg, dsize)
            cv2.imwrite("resized/" + filename.split(".jpg")
                        [0] + str(counter) + ".jpg", roi)


for filename in os.listdir('./test/'):
    resize_by_face(filename)
