# https://levelup.gitconnected.com/pixels-arrays-and-images-ef3f03638fe7 Tutorial
import cv2 as cv
import numpy as np
from src import utilidades as ut, sift
from PIL import Image

#fg_img = cv.imread('imagens/p4.jpg')
#bg_img = cv.imread('imagens/1.jpg')

# Guarda as coordenadas
left, top, right, bottom = 300, 150, 380, 220
#left, top, right, bottom = 302, 151, 308, 153
#left, top, right, bottom = 300, 150, 335, 185

imagem_original_pil = Image.open(r"imagens/1.jpg")

# Passo 1
patch = ut.corta(imagem_original_pil, left, top, right, bottom)

## Convertendo imagens

patch_numpy = np.array(patch)
imagem_original_numpy = np.array(imagem_original_pil)


## Passo 2

## Calculando descritores
kp1, des1 = sift.sift_detectores_e_descritores(patch_numpy)
kp2, des2 = sift.sift_detectores_e_descritores(imagem_original_numpy)

## Calculando Correspondências
imagem_out, good, kp1, kp2 = sift.correspondencias(patch_numpy, imagem_original_numpy, kp1=kp1, kp2=kp2, des1=des1, des2=des2)

## Passo 3

imagem_original_numpy[top:bottom, left:right] = patch_numpy

## Passo 4

for g in good:
    x, y = kp1[g[0].queryIdx].pt
    x2, y2 = kp2[g[0].trainIdx].pt
    novo_x = left + x
    novo_y = top + y
    #print('Novo:', novo_x, novo_y, 'Orig: ', p2, '---', g[0].distance)
    print('Distancia entre pixels: ', (novo_x - x2)**2, (novo_y - y2)**2)
#patch_numpy = np.array(patch)
#imagem_original_numpy = np.array(imagem_original_pil)
#h1, w1 = fg_img.shape[:2]
#print (h1, w1)

#pip_h = 10
#pip_w = 10
#print(pip_h,pip_h+h1,pip_w,pip_w+w1)


#bg_img[pip_h:pip_h+h1,pip_w:pip_w+w1] = fg_img
#bg_img[0:h1,0:w1] = fg_img


#cv.imshow('', bg_img)
#cv.waitKey(0)