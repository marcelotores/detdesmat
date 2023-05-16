# Importing Image class from PIL module
from PIL import Image
from matplotlib import pyplot as plt
from src import utilidades as ut
import cv2 as cv


def corta(im, left, top, right, bottom):

    im1 = im.crop((left, top, right, bottom))
    im1.show()

# Opens a image in RGB mode
im = Image.open(r"../imagens/1.jpg")
img = cv.imread("../imagens/1.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
#print(int((height-88.75)/20))


#for left in range(0, width, 20):
#    print(left)


patch_width = 350
patch_height = 300
aument = 70
for left in range(0, width, aument):
    right = left + patch_width
    if right > width:
        break
    for top in range(0, height, aument):
        bottom = top + patch_height
        if bottom > height:
            break
        corta(im, left, top, right, bottom)
        print(left, top, right, bottom)

    #corta(im, (0, 0, 88.75, 88.75))
print(width, height)





#cv.imshow('', img)
# Shows the image in image viewer
#im1.show()

#plt.imshow(img)
#plt.imshow(img2)
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()