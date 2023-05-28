from datetime import datetime
from src import utilidades as ut, sift
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from src.crop_f import crop
from src.encaixa import encaix

img_original = cv.imread("imagens/1.jpg")
rep, good = crop(ut.ndarray_pil(img_original), 85, 85, 20, 'segundo_teste')
exit()

imagem_original_pil = Image.open(r"imagens/1.jpg")
#patch_pil = Image.open(r"imagens/patchs/162.jpg")


left, right, top, bottom = 220, 305, 180, 265
patch = ut.corta(imagem_original_pil, left, top, right, bottom)

imagem_original_numpy = ut.ndarray_pil(imagem_original_pil, False)
patch_numpy = ut.ndarray_pil(patch, False)


kp1, des1 = sift.sift_detectores_e_descritores(patch_numpy)
kp2, des2 = sift.sift_detectores_e_descritores(imagem_original_numpy)

imagem_out, good, kp1, kp2 = sift.correspondencias(patch_numpy, imagem_original_numpy, kp1=kp1, kp2=kp2, des1=des1, des2=des2)

#novo_left, novo_right, novo_top, novo_bottom, dist = encaix(good, kp1, kp2, imagem_original_numpy, patch_numpy, left, right, top, bottom)
novo_top, novo_bottom, novo_left, novo_right, dist = encaix(good, kp1, kp2, imagem_original_numpy, patch_numpy, left, right, top, bottom)
#left, right, top, bottom = 220, 305, 180, 265
#novo_left, novo_right, novo_top, novo_bottom = 625, 710, 264, 349

imagem_original_numpy[int(novo_top):int(novo_bottom), int(novo_left):int(novo_right)] = patch_numpy

cv.imshow('', imagem_original_numpy)
cv.waitKey(0)


