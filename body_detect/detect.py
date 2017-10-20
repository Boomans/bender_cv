import numpy as np
import timeit
import imutils
import cv2

face_cascade = cv2.CascadeClassifier('/home/murt/opencv/data/haarcascades/haarcascade_upperbody.xml')
eye_cascade = cv2.CascadeClassifier('/home/murt/opencv/data/haarcascades/haarcascade_eye.xml')
body_cascade = cv2.CascadeClassifier('/home/murt/opencv/data/haarcascades/haarcascade_fullbody.xml')
hs_casc = cv2.CascadeClassifier('H5.xml')

img = cv2.imread('zz.jpg')
img = imutils.resize(img, width=min(1300, img.shape[1]))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#faces = face_cascade.detectMultiScale(gray, 1.1, 1)
#bodies = body_cascade.detectMultiScale(gray, 1.01, 1)
# faces = hs_casc.detectMultiScale(gray, 1.1, 1, minSize=(150,150), maxSize=(250, 250))
faces = hs_casc.detectMultiScale(gray, 1.2, 1, minSize=(4,4), maxSize=(200, 200))
# print(timeit.timeit('hs_casc.detectMultiScale(gray, 1.1, 2, minSize=(50, 50), maxSize=(80,80))', setup='import cv2; from __main__ import gray, hs_casc', number=5))
print(len(faces))
print(faces)
#bodies = body_cascade.detectMultiScale(gray, 1.01, 2 )#, minSize=(40, 15))
#print(len(bodies))
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # roi_gray = gray[y:y+h, x:x+w]
    # roi_color = img[y:y+h, x:x+w]
    # eyes = eye_cascade.detectMultiScale(roi_gray, 1.5, 10)
    # for (ex,ey,ew,eh) in eyes:
    #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()