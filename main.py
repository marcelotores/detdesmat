import numpy as np
import cv2 as cv
import sift as sf

img = cv.imread('imagens/p4.jpg')

kp, des = sf.sift_detectores_e_descritores(img, 1)




