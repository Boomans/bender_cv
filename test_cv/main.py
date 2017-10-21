import multiprocessing

import cv2
import funcs.differ as dff
from imutils import paths


empty_rooms_imgs = {}
for image_path in paths.list_images('img_empt'):
    empty_rooms_imgs[image_path.split('/')[-1]] = cv2.imread(image_path)
for image_path in paths.list_images('img'):
    key = image_path.split('/')[-1]
    dif_buf = dff.diff(cv2.imread(image_path), empty_rooms_imgs[key])
    diff_img = dif_buf[0]
    weight = dif_buf[1]
    print(weight / 590)
    print(dff.get_count_of_people(diff_img))

# print(empty_rooms_imgs)

