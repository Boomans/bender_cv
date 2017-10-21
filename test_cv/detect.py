import cv2
import funcs.differ as dff
from imutils import paths


empty_rooms_imgs = {}
for image_path in paths.list_images('img_empt'):
    empty_rooms_imgs[image_path.split('/')[-1]] = cv2.imread(image_path)
for image_path in paths.list_images('img'):
    key = image_path.split('/')[-1]
    diff_img = dff.diff(cv2.imread(image_path), empty_rooms_imgs[key])
    print(dff.get_count_of_people(diff_img))

# print(empty_rooms_imgs)

