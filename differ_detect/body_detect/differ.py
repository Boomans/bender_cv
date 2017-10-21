from PIL import Image
import cv2
import time



def isOk(tupl1, tupl2, delta):
    x, y, z = tupl1
    x1, y1, z1 = tupl2
    return (abs(x - x1) < delta and abs(y-y1) < delta and abs(z-z1) < delta)


def differ_img(img_emp, img_curn):

    img_cur = Image.open(str(img_curn) + '.jpg')
    img_empt = Image.open(str(img_emp) + '.jpg')

    print("\t", time.time())

    pixels_cur = img_cur.load()

    print("\t", time.time())

    pixels_emp = img_empt.load()

    print("\t", time.time())
    #img_1.rotate(45).show
    # print(pixels_1)
    delta = 7
    for i in range(1, img_cur.size[0]-1):
        for j in range(1, img_cur.size[1]-1):
            if isOk(pixels_cur[i,j],pixels_emp[i,j], delta):
                pixels_cur[i,j] = (0, 255, 255)
                # pixels_emp[i,j] = (255, 255, 255)

    print("\t", time.time())
    img_cur.save("out.jpg")
    return "out.jpg"

def exp(x):
    return exp(x)
def get_room_fullness(img):
    pass
