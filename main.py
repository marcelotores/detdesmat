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

# for g in good:
#     print(g[0].distance)

good_np = np.array(good)
good_np = good_np.reshape(good_np.shape[0], )
arr_distance = np.array([])
#app_arr = np.append(arr, [13,15,17])
count_0 = 0
for g in good_np:
    arr_distance = np.append(arr_distance, g.distance)
    if g == 0:
        count_0 += 1

print(np.min(arr_distance))
print(np.max(arr_distance))
print(np.average(arr_distance))
print(count_0)
print('----')
print(len(kp1))
print(len(kp2))
menor_ponto = (min(len(kp1), len(kp2)))
print(menor_ponto)

print(good_np.shape[0]/menor_ponto)


