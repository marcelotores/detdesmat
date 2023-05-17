# Importing Image class from PIL module
from PIL import Image
from matplotlib import pyplot as plt
from src import utilidades as ut
import cv2 as cv


def corta(im, left, top, right, bottom):

    im1 = im.crop((left, top, right, bottom))
    return im1
    #im1.show()

# Opens a image in RGB mode
im = Image.open(r"../imagens/1.jpg")
img = cv.imread("../imagens/1.jpg")
#im.save("teste/geeks.jpg")
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
patch_width = 85
patch_height = 85
aument = 20

for left in range(0, width, aument):
    right = left + patch_width
    if right > width:
        break
    for top in range(0, height, aument):
        bottom = top + patch_height
        if bottom > height:
            break
        im1 = corta(im, left, top, right, bottom)

        #im1.save(f"teste/{left}-{top}-{right}-{bottom}.jpg")
        #print(left, top, right, bottom)




#plt.imshow(img)
#plt.imshow(img2)
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()