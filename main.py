import cv2 as cv
from matplotlib import pyplot as plt
from src import sift

img1 = cv.imread('imagens/p1.jpg')
img2 = cv.imread('imagens/1.jpg')

kp1, des1 = sift.sift_detectores_e_descritores(img1)
kp2, des2 = sift.sift_detectores_e_descritores(img2)
#sift.imprime_detectores(kp)

imagem_out, good, kp1, kp2, correspondencias = sift.correspondencias(img1, img2, kp1=kp1, kp2=kp2,
                                                   des1=des1, des2=des2, qtd_match=3)
#print(correspondencias)
for g, n in correspondencias:
    p1 = kp1[g.queryIdx].pt
    p2 = kp2[g.trainIdx].pt


#for match in matches:
#  p1 = kp1[match.queryIdx].pt
#  p2 = kp2[match.trainIdx].pt
#print(kp1[0])
#print(kp2[0])

plt.imshow(imagem_out)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()




