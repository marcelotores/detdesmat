from datetime import datetime

from src import utilidades as ut, sift
from PIL import Image
import numpy as np
import cv2 as cv

imagem_original_pil = Image.open(r"imagens/1.jpg")

nome_arquivo = datetime.now().strftime("%d%m%H%M%S")
print(nome_arquivo)
exit()

left, top, right, bottom = 302, 151, 308, 153

patch1 = ut.corta(imagem_original_pil, left, top, right, bottom)
patch2 = ut.corta(patch1, 0, 2, 1, 4)

patch_numpy1 = np.array(patch1)
patch_numpy2 = np.array(patch2)

print(patch_numpy1[2:4, 0:1].shape)
print(patch_numpy2.shape)
exit()
patch_numpy1[0:2, 3:4] = patch_numpy2
print(patch_numpy1)
print('------------------')
print(patch_numpy2)
#patch_numpy = ut.pontos(patch_numpy, 2, 1)

cv.imshow('', patch_numpy1)
#cv.imshow('', patch_numpy1)
cv.waitKey(0)

