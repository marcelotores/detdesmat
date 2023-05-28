# https://levelup.gitconnected.com/pixels-arrays-and-images-ef3f03638fe7 Tutorial
import cv2 as cv
import numpy as np
from src import utilidades as ut, sift
from PIL import Image

from src.encaixa import encaix

#fg_img = cv.imread('imagens/p4.jpg')
#bg_img = cv.imread('imagens/1.jpg')

# Guarda as coordenadas
left, top, right, bottom = 300, 150, 380, 220
#left, top, right, bottom = 302, 151, 308, 153
#left, top, right, bottom = 300, 150, 335, 185

imagem_original_pil = Image.open(r"imagens/1.jpg")

# Passo 1 - Recorta patch da imagem original, guardando as coordenadas (c1) do patch na imagem original.
patch = ut.corta(imagem_original_pil, left, top, right, bottom)

## Convertendo imagens
patch_numpy = ut.ndarray_pil(patch, False)
imagem_original_numpy = ut.ndarray_pil(imagem_original_pil, False)
#patch_numpy = np.array(patch)
#imagem_original_numpy = np.array(imagem_original_pil)


## Passo 2 - Calcula os descritores e correspondências entre o patch e a imagem original.

## Calculando descritores
kp1, des1 = sift.sift_detectores_e_descritores(patch_numpy)
kp2, des2 = sift.sift_detectores_e_descritores(imagem_original_numpy)


## Calculando Correspondências
imagem_out, good, kp1, kp2 = sift.correspondencias(patch_numpy, imagem_original_numpy, kp1=kp1, kp2=kp2, des1=des1, des2=des2)

### O crop faz até essa parte.

## Passo 3 - Coloca de volta o patch na imagem original, usando as coordenadas guardadas no passo 1 e mantendo os descritores correspondentes
## tanto na imagem original quanto no patch.

### imagem_original_numpy[top:bottom, left:right] = patch_numpy

## Passo 4 - Calculado distâcia das cooredenadas dos keypoints e também a média de distância


dif_x = 0
dif_y = 0
distancia_total = 0
for g in good:
    x, y = kp1[g[0].queryIdx].pt
    x2, y2 = kp2[g[0].trainIdx].pt
    x1 = left + x
    y1 = top + y
    print(f'Novo: ({x1}, {y1}) Orig: ({x2}, {y2}) --- {g[0].distance}')
    distancia_total += g[0].distance
    #print('Distancia entre pixels: ', (novo_x - x2), (novo_y - y2))
    ############################################################################

    ## Somando todos os y e x para ver a diferença de posição entre as coordenadas do patch e da imagem original
    dif_x += x2 - x1
    dif_y += y2 - y1

# Após fazer isso para todas as imagens, criar um gráfico dessas distâncias (dif_x, dif_y)
## Também fazer um gráfico com a soma das distâncias das correspondências para cada imagem
print(dif_x, dif_y)
# Atribuindo novos valores para as coordenadas do patch que será encaixado na imagem
novo_left = left + dif_x
novo_right = right + dif_x
novo_top = top + dif_y
novo_bottom = bottom + dif_y


## Apenas dar destaque a cor do patch
##patch_numpy = cv.cvtColor(patch_numpy, cv.COLOR_BGR2RGB)

## Encaixando o patch na imagem original
imagem_original_numpy[int(novo_top):int(novo_bottom), int(novo_left):int(novo_right)] = patch_numpy
cv.imshow('', imagem_original_numpy)
cv.waitKey(0)









