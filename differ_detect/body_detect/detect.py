import imutils
import cv2
import time
import np_detect


def diff(img,img1): # returns just the difference of the two images

    return cv2.absdiff(img,img1)


def diff_remove_bg(img0,img1): # removes the background but requires three images
    # d1 = diff(img0,img1)
    return cv2.absdiff(img1, img0)

hs_casc = cv2.CascadeClassifier('HS.xml')
# hs_casc = cv2.CascadeClassifier('/home/murt/opencv/data/haarcascades/haarcascade_profileface.xml')


img_cur = cv2.imread('img/cur2.jpg')
img_empty = cv2.imread('img/empt.jpg')

# img_name = differ.differ_img('empt', 'cur')
# print(time.time())

# img = cv2.bitwise_and(img_cur, cv2.bitwise_not(img_empty))

# img = differ.differ_img('empt', 'cur')  # work but slow
time_s = time.time()
print("func: ", time.time())

img = np_detect.diff(img_cur, img_empty)

print("func: ", time.time()-time_s)

# img = cv2.imread(img)
cv2.imshow("no_nose",img)
cv2.waitKey(0)



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.fastNlMeansDenoising(gray,templateWindowSize=7, searchWindowSize=21 ,h=10)
# cv2.imshow("no_nose",gray)
# cv2.waitKey(0)
print(time.time())
print("HALF")
faces = hs_casc.detectMultiScale(gray, 1.2, 2, minSize=(2, 2), maxSize=(200, 200))
print(time.time())
# print(timeit.timeit('hs_casc.detectMultiScale(gray, 1.1, 2, minSize=(50, 50), maxSize=(80,80))', setup='import cv2; from __main__ import gray, hs_casc', number=5))
print(len(faces))

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()