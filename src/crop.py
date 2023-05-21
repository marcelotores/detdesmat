# Importing Image class from PIL module
from PIL import Image
from matplotlib import pyplot as plt
from src import utilidades as ut
import cv2 as cv
import numpy as np
from src import sift
import src.plots as pl


# Opens a image in RGB mode
#imagem_original_pil = Image.open(r"../imagens/1.jpg")
#imagem_original_pil = Image.open(r"../imagens/descarga_05.jpg")
imagem_original_pil = Image.open(r"../imagens/Trinca_06.jpg")

#imagem_original_numpy = cv.imread("../imagens/1.jpg")
#img = cv.imread("../imagens/1.jpg")

width, height = imagem_original_pil.size
patch_width = 85
patch_height = 85
aument = 20
count = 0
rep = []
goods = []
distance = []
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
        goods.append(len(good))
        # with open("hello.txt", "a") as my_file:
        #     my_file.write('###################################################################\n')
        #     my_file.write(f'#### Patch {count} ---> {len(kp1)}:{len(kp2)} -- {len(good)} ####\n')

        ## Calculo da distancia mínima, máxima e média
        if len(good) != 0:
            good_np = np.array(good)
            good_np = good_np.reshape(good_np.shape[0], )
            arr_distance = np.array([])
            repetitibilidade = good_np.shape[0] / (min(len(kp1), len(kp2)))
            rep.append(repetitibilidade)
            # app_arr = np.append(arr, [13,15,17])
            count_0 = 0
            for g in good_np:
                arr_distance = np.append(arr_distance, g.distance)
                if g.distance == 0:
                    count_0 += 1

            distance.append(np.average(arr_distance))
            #distance.append(arr_distance)
            print('Repetibilidade (matching/min[qtd_kp1, qtd_kp2]): ', repetitibilidade)
            print('Min: ', np.min(arr_distance))
            print('Máx: ', np.max(arr_distance))
            print('Méd: ', np.average(arr_distance))
            print('Quantidade de correspondências com Distancia Zero: ', count_0)

            # with open("hello.txt", "a") as my_file:
            #     my_file.write(f'Repetibilidade (matching/min[qtd_kp1, qtd_kp2]): {repetitibilidade}\n')
            #     my_file.write(f'Min: {np.min(arr_distance)}\n')
            #     my_file.write(f'Máx: {np.max(arr_distance)}\n')
            #     my_file.write(f'Méd: {np.average(arr_distance)}\n')
            #     my_file.write(f'Quantidade de correspondências Zeros: {count_0}\n')
        #Image.fromarray(imagem_out).save(f"../imagens/patchs/Patch {count}.jpg")
        count+=1


with open("exp3.py", "a") as my_file:
    my_file.write(f'repa = {rep}\n')
    my_file.write(f'goodsa = {goods}\n')
    my_file.write(f'distance = {distance}')

with open("exp3.txt", "a") as my_file:
    my_file.write(f'Quantidade de Patchs = {count}\n')
    my_file.write(f'Tamanho Imagem Original = {imagem_original_numpy.shape}\n')
    my_file.write(f'Tamanho de cada Patch = {patch_numpy.shape}')

#pl.distancia(np.array(distance))
#pl.cor(np.array(goods))
#pl.rep(np.array(rep))









#media = sum(rep) / len(rep)
#print('Media Rep: ', media)
