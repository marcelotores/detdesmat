import cv2 as cv
from matplotlib import pyplot as plt
from src import sift

img1 = cv.imread('imagens/p5.jpg')
img2 = cv.imread('imagens/1.jpg')

kp1, des1 = sift.sift_detectores_e_descritores(img1)
kp2, des2 = sift.sift_detectores_e_descritores(img2)
#sift.imprime_detectores(kp)

imagem_out, good, kp1, kp2 = sift.correspondencias(img1, img2, kp1=kp1, kp2=kp2,
                                                   des1=des1, des2=des2)
#print(correspondencias)
#for g, n in correspondencias:
#    print(g, n)
#print(good)
#print(good[1][0].distance)
#print(good[1][0].imgIdx)
#print(good[1][0].queryIdx)
#print(good[1][0].trainIdx)
#print()
#print(good[0][0].distance)
#print(good[0][0].imgIdx)
#print(good[0][0].queryIdx)
#print(good[0][0].trainIdx)
#print(dir(kp1[0]))

#for g in good:
#    pass
     #print(kp1[g[0].queryIdx].pt, kp2[g[0].trainIdx].pt, g[0].distance)


#for m, n in correspondencias:
#    print(m, n, m.distance, n.distance)
    #print('m')
    #print(kp1[m.queryIdx].pt, kp2[m.trainIdx].pt, m.distance)
    #print('n')
    #print(kp1[n.queryIdx].pt, kp2[n.trainIdx].pt, n.distance)
#print(correspondencias)
    #print(m, n)
#for g in good:
#    print(g)
#print('Pontos 1')
#for k1 in kp1:
#    print(k1)
#print('Pontos 2')
#for k2 in kp2:
#    print(k2)

#p1 = kp1[good[0][0].queryIdx]
#p2 = kp2[good[0][0].trainIdx]
#print(p1, p2)
#for k in kp1:
#    print(k)
#for k2 in kp2:
#    print(k2.pt)
#print(correspondencias)



#for match in matches:
#  p1 = kp1[match.queryIdx].pt
#  p2 = kp2[match.trainIdx].pt
#print(kp1[0])
#print(kp2[0])
cv.imshow(f'{len(kp1)}:{len(kp2)} -- {len(good)}', imagem_out)
cv.waitKey(0)
#plt.imshow(imagem_out)
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()




