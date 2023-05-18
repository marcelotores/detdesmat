# Importing Image class from PIL module
from PIL import Image
from matplotlib import pyplot as plt
from src import utilidades as ut
import cv2 as cv
import numpy as np
from src import sift


# Opens a image in RGB mode
imagem_original_pil = Image.open(r"../imagens/1.jpg")
#imagem_original_numpy = cv.imread("../imagens/1.jpg")
#img = cv.imread("../imagens/1.jpg")

width, height = imagem_original_pil.size
patch_width = 85
patch_height = 85
aument = 20
count = 0
for left in range(0, width, aument):
    right = left + patch_width
    if right > width:
        break
    for top in range(0, height, aument):
        bottom = top + patch_height
        if bottom > height:
            break
        patch = ut.corta(imagem_original_pil, left, top, right, bottom)

        ## Convertendo imagens
        patch_numpy = np.array(patch)
        imagem_original_numpy = np.array(imagem_original_pil)

        ## Calculando descritores
        kp1, des1 = sift.sift_detectores_e_descritores(patch_numpy)
        kp2, des2 = sift.sift_detectores_e_descritores(imagem_original_numpy)

        ## Calculando Correspondências
        imagem_out, good, kp1, kp2 = sift.correspondencias(patch_numpy, imagem_original_numpy, kp1=kp1, kp2=kp2,
                                                                             des1=des1, des2=des2)
        print('##################################################################')
        print(f'#### Patch {count} ---> {len(kp1)}:{len(kp2)} -- {len(good)} ####')

        ## Calculo da distancia mínima, máxima e média
        if len(good) != 0:
            good_np = np.array(good)
            good_np = good_np.reshape(good_np.shape[0], )
            arr_distance = np.array([])
            # app_arr = np.append(arr, [13,15,17])
            count_0 = 0
            for g in good_np:
                arr_distance = np.append(arr_distance, g.distance)
                if g.distance == 0:
                    count_0 += 1
            print('Repetibilidade (matching/min[qtd_kp1, qtd_kp2]): ', good_np.shape[0]/(min(len(kp1), len(kp2))))
            print('Min: ', np.min(arr_distance))
            print('Máx: ', np.max(arr_distance))
            print('Méd: ', np.average(arr_distance))
            print('Quantidade de correspondências Zeros: ', count_0)

        #patch.save(f"../imagens/patchs/Patch {count}.jpg")
        count+=1


cv.imshow(f'{len(kp1)}:{len(kp2)} -- {len(good)}', imagem_out)
cv.waitKey(0)

#plt.imshow(img)
#plt.imshow(img2)
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()