# pip install opencv-python

import cv2

f = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = f.detectMultiScale(gray, 1.1, 4)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (225,0,0), 2)

cv2.imshow('img', img)
cv2.waitKey()

cv2.imwrite("face_d.jpg", img)