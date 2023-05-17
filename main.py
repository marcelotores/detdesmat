import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from src import sift
from PIL import Image

img1 = cv.imread('imagens/p5.jpg')
img2 = cv.imread('imagens/1.jpg')


kp1, des1 = sift.sift_detectores_e_descritores(img1)
kp2, des2 = sift.sift_detectores_e_descritores(img2)
#sift.imprime_detectores(kp)

imagem_out, good, kp1, kp2 = sift.correspondencias(img1, img2, kp1=kp1, kp2=kp2,
                                                   des1=des1, des2=des2)

