import numpy as np
import cv2
import cmath


def subs(tup1, tup2):
    return abs(int(tup1[0]) - int(tup2[0])), abs(int(tup1[1]) - int(tup2[1])), abs(int(tup1[2]) - int(tup2[2]))
#
# def isOk(tupl1, tupl2, delta):
#     diff_btwn_pxls = subs(tupl1, tupl2)
#     for item in diff_btwn_pxls:
#         if (item > delta):
#             return False
#     return True

def isOk_2(tup1, tup2, delta):
    return (abs(int(tup1[0]) - int(tup2[0])) < delta and
           abs(int(tup1[1]) - int(tup2[1])) < delta and
           abs(int(tup1[2]) - int(tup2[2])) < delta)

def diff(img_cur, img_emp):
    delta = 10
    img_cur[0, 0] = [255, 255, 255]
    white = img_cur[0, 0]
    for i in range(len(img_cur)):
        for j in range(len(img_cur[0])):
            # print (type(img_cur[i][j]))
            if isOk_2(img_cur[i,j], img_emp[i, j], delta):
                img_cur[i, j] = white
    return img_cur

def diff_w(img_cur, img_emp):

    W_empt = 0
    W = 0
    delta = 10
    for i in range(len(img_cur) - 1, -1, -1):
        res = 0
        res_empt = 0
        for j in range(len(img_cur[0]) - 1, -1, -1):
            res_empt += 1
            # print (type(img_cur[i][j]))
            if isOk(img_cur[i,j], img_emp[i, j], delta):
                img_cur[i, j] = [255, 255, 255]
            else:
                res += 1
        W += res * 0.05 *  math.exp(float(len(img_cur) - i) / 5.0)
        W_empt += res_empt * 0.05 *  math.exp((len(img_cur) - i) / 5.0)
    print("W = ", W, "W_rmpt = ", W_empt, float(W) / W_empt)
    cv2.waitKey(0)

    return img_cur