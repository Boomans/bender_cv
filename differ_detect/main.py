from PIL import Image

img_1 = Image.open("1.jpg")
img_2 = Image.open("1.2.jpg")
pixels_1 = img_1.load()
pixels_2 = img_2.load()
#img_1.rotate(45).show
print(pixels_1)
for i in range(img_1.size[0]):
    for j in range(img_1.size[1]):
        if sum(pixels_1[i,j]) - sum(pixels_2[i,j]) < 60:
            pixels_1[i,j] = (255, 255, 255)

img_1.save("out.jpg")

