# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms import Form, CharField, ImageField
from random import random
from datetime import datetime
from PCV.differ import diff, get_count_of_people
import memcache
from json import dumps, loads
import cv2
db = memcache.Client(["127.0.0.1:11211"])

db.set('210_max', 22)
db.set('210_last', 0.8)

nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 32, 33, 34, 38, 39, 40, 46, 47, 48,
        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 68, 69, 89, 90, 91, 100, 101, 102, 106, 107, 108,
        109, 110, 111, 112, 113, 114, 115, 116, 117, 121, 127, 128, 129, 130, 131, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172,
        173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
        195, 196, 197, 198, 200, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218,
        219, 220, 221, 222, 223, 224, 226, 227, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242,
        243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264,
        265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286,
        287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 302, 304, 305, 306, 307, 308, 314, 315,
        316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339,
        340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, '351a', 352, 353, 354, 355, 356, 357, 358, 359, 360,
        361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 375, 376, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390,
        391, 392, 393, 394, 395, 396, 397, 398, 399, 400, ]


class UploadForm(Form):
    token = CharField(max_length=32)
    image = ImageField()


def data_json(request):
    response = {"last-update": datetime.today()}
    response['data'] = [{"num": n, "count": random()} for n in nums]
    response['data'][210] = db.get('210_last')
    return JsonResponse(response)


@csrf_exempt
def upload(request):
    response = HttpResponse()
    if request.method == 'POST' and request.POST.get('token') == '23317bcdde58306bfb3e321fb2803fea':
        form = UploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():

            if request.GET.get('id') is None:
                src_img = 'Data/000.jpg'
            else:
                src_img = 'Data/%s.jpg' % request.GET['id']

            f = request.FILES['image']
            with open('buf.jpg', 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            dif_img, weight = diff(cv2.imread('buf.jpg'), cv2.imread(src_img))
            count = get_count_of_people(dif_img)

            if request.GET.get('max') is None:
                max_result = db.get('210_max')
                if max_result < weight:
                    max_result = weight
                if max_result < count:
                    max_result = count
            else:
                max_result = request.GET['max']

            if request.GET.get('last') is None:
                last = db.get('210_last')
            else:
                last = request.GET['last']

            result = (last + (weight + count) / max_result) / 3
            db.set('210_last', result)
            db.set('210_max', max_result)
            response.write("<result>%f</result>" %result)
        else:
            response.write("<p>Invalid form</p>")
    else:
        response.write("<p>No POST format or invalid token</p>")
    return response
