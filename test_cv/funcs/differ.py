from multiprocessing import Process, Queue
import time
import numpy as np
import imutils
import cv2


HS_Cascade = cv2.CascadeClassifier('funcs/HS.xml')
img_cr = None

def subs(tup1, tup2):
    return (abs(int(tup1[0]) - int(tup2[0])),
            abs(int(tup1[1]) - int(tup2[1])),
            abs(int(tup1[2]) - int(tup2[2])))


def is_same_px(tup1, tup2, delta):
    return (abs(int(tup1[0]) - int(tup2[0])) < delta and
            abs(int(tup1[1]) - int(tup2[1])) < delta and
            abs(int(tup1[2]) - int(tup2[2])) < delta)


def calc_dif(img1, img2, que, ind):

    white = np.uint8(255)
    for i in range(1, len(img1), 2):
        for j in range(1, len(img1[0]), 2):
            if (abs(int(img1[i,j-1]) - int(img2[i, j-1])) < 2):
                img1[i, j] = white
                img1[i-1, j] = white
                img1[i, j-1] = white
                img1[i-1, j-1] = white
    que.put((img1,ind))
    # print("Done")



def diff(img_cur, img_empt):

    buf = {}
    result_queue = Queue()
    img_cur = imutils.resize(img_cur, height=min(720, img_cur.shape[0]))
    img_empt = imutils.resize(img_empt, height=min(720, img_empt.shape[0]))
    img_cur = cv2.cvtColor(img_cur, cv2.COLOR_BGR2GRAY)
    img_empt = cv2.cvtColor(img_empt, cv2.COLOR_BGR2GRAY)

    p1 = Process(target=calc_dif,
                 args=(img_cur[:len(img_cur) // 4, : ], img_empt[:len(img_cur) // 4, :], result_queue, 1))
    p2 = Process(target=calc_dif,
                 args=(img_cur[len(img_cur) // 4: len(img_cur) // 2, : ], img_empt[len(img_cur) // 4: len(img_cur) // 2, : ], result_queue, 2))
    p3 = Process(target=calc_dif,
                 args=(img_cur[len(img_cur) // 2: len(img_cur) //  4*3, :], img_empt[len(img_cur) // 2: len(img_cur) // 4*3, :], result_queue, 3))
    p4 = Process(target=calc_dif, args=(img_cur[len(img_cur) //  4*3:, : ], img_empt[len(img_cur) // 4 * 3:, :], result_queue, 4))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    for i in range(4):
        buf_tup = result_queue.get()
        buf[buf_tup[1]] = buf_tup[0]

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    img = np.vstack((np.vstack((buf[1], buf[2])),
                     np.vstack((buf[3], buf[4]))))
    return img

def get_count_of_people(img_cur):

    peoples = HS_Cascade.detectMultiScale(img_cur, 1.1, 1, minSize=(30, 30), maxSize=(150, 150))
    for (x, y, w, h) in peoples:
        cv2.rectangle(img_cur, (x, y), (x + w, y + h), (0, 0, 0), 2)
    cv2.imshow('result', img_cur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return len(peoples)