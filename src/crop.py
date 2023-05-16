# Importing Image class from PIL module
from PIL import Image
from matplotlib import pyplot as plt
from src import utilidades as ut
import cv2 as cv


def corta(img, coordenadas):

    im1 = im.crop((coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3]))
    im1.show()

# Opens a image in RGB mode
im = Image.open(r"../imagens/1.jpg")
img = cv.imread("../imagens/1.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size


for left in range(0, width, 20):
    for top in range(0, height, 20):
        print(left, top)
        print(left+88.75, top+88.75)
        print()
    #corta(im, (0, 0, 88.75, 88.75))
print(width, height)
#cv.imshow('', img)
# Shows the image in image viewer
#im1.show()

#plt.imshow(img)
#plt.imshow(img2)
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()