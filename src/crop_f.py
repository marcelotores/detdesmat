# Importing Image class from PIL module
from PIL import Image
from matplotlib import pyplot as plt
from src import utilidades as ut
import numpy as np
from src import sift
import src.plots as pl
from datetime import datetime
from src.encaixa import encaix
import cv2 as cv

def crop(imagem_original_pil, patch_width=85, patch_height=85, aument=20, n_arquivo=None):
    """

    :param imagem_original_pil: uma imagem do tipo Image (PIL)
    :param patch_width: largura do patch
    :param patch_height: altura do patch
    :param aument: A distância que cada patch será arrastado para ser cortado da imagem original
    :return: Lista de Repetibilidade e das Correspondências
    """
    width, height = imagem_original_pil.size

    count = 0
    rep = []
    goods = []
    distance = []
    novas_imagens_coord = []

    for left in range(0, width, aument):
        right = left + patch_width
        if right > width:
            break
        for top in range(0, height, aument):
            bottom = top + patch_height
            if bottom > height:
                break
            patch = ut.corta(imagem_original_pil, left, top, right, bottom)


            ## Convertendo imagens para numpy
            patch_numpy = ut.ndarray_pil(patch, False)
            imagem_original_numpy = ut.ndarray_pil(imagem_original_pil, False)
            #patch_numpy = np.array(patch)
            #imagem_original_numpy = np.array(imagem_original_pil)

            ## Calculando descritores
            kp1, des1 = sift.sift_detectores_e_descritores(patch_numpy)
            kp2, des2 = sift.sift_detectores_e_descritores(imagem_original_numpy)

            ## Calculando Correspondências
            imagem_out, good, kp1, kp2 = sift.correspondencias(patch_numpy, imagem_original_numpy, kp1=kp1, kp2=kp2, des1=des1, des2=des2)

            ################
            novo_top, novo_bottom, novo_left, novo_right, distancia_total = encaix(good, kp1, kp2, imagem_original_numpy, patch_numpy, left, right, top, bottom)
            print(left, right, top, bottom)
            print(novo_left, novo_right, novo_top, novo_bottom)

            novas_imagens_coord.append([novo_left, novo_top, novo_right, novo_bottom, distancia_total])
            ## Apenas dar destaque a cor do patch
            #patch_numpy = cv.cvtColor(patch_numpy, cv.COLOR_BGR2RGB)

            imagem_original_numpy[int(novo_top):int(novo_bottom), int(novo_left):int(novo_right)] = patch_numpy
            cv.imwrite(f"/home/marcelo/projetos/mestrado/pesquisa/detdesmat/imagens/encaixa/{count}.jpg", imagem_original_numpy)

            #Image.fromarray(imagem_original_numpy).save(f"../imagens/encaixa/{count}.jpg")
            #Image.fromarray(imagem_original_numpy).save(f"../imagens/patchs/Patch {count}.jpg")


            ################

            print('##################################################################')
            print(f'#### Patch {count} ---> {len(kp1)}:{len(kp2)} -- {len(good)} ####')

            ## Colando as correspondências na lista de correspondências
            goods.append(len(good))

            # with open("hello.txt", "a") as my_file:
            #     my_file.write('###################################################################\n')
            #     my_file.write(f'#### Patch {count} ---> {len(kp1)}:{len(kp2)} -- {len(good)} ####\n')

            ## Calculo da distancia mínima, máxima e média entre cada correspondência
            if len(good) != 0:
                good_np = np.array(good)
                good_np = good_np.reshape(good_np.shape[0], )
                arr_distance = np.array([])
                repetitibilidade = good_np.shape[0] / (min(len(kp1), len(kp2)))

                ## Lista de repetitibilidade de cada key point
                rep.append(repetitibilidade)
                # app_arr = np.append(arr, [13,15,17])
                count_0 = 0
                for g in good_np:
                    arr_distance = np.append(arr_distance, g.distance)
                    if g.distance == 0:
                        count_0 += 1

                ## Lista de média de distância entre as correspondências
                distance.append(np.average(arr_distance))
                #distance.append(arr_distance)
                ##print('Repetibilidade (matching/min[qtd_kp1, qtd_kp2]): ', repetitibilidade)
                ##print('Min: ', np.min(arr_distance))
                ##print('Máx: ', np.max(arr_distance))
                ##print('Méd: ', np.average(arr_distance))
                ##print('Quantidade de correspondências com Distancia Zero: ', count_0)

                # with open("hello.txt", "a") as my_file:
                #     my_file.write(f'Repetibilidade (matching/min[qtd_kp1, qtd_kp2]): {repetitibilidade}\n')
                #     my_file.write(f'Min: {np.min(arr_distance)}\n')
                #     my_file.write(f'Máx: {np.max(arr_distance)}\n')
                #     my_file.write(f'Méd: {np.average(arr_distance)}\n')
                #     my_file.write(f'Quantidade de correspondências Zeros: {count_0}\n')
            #Image.fromarray(imagem_out).save(f"../imagens/patchs/Patch {count}.jpg")
            count+=1


    ## Gerará um arquivo info.py com a lista de repetitibilidade entre as correspondências, as correspondências e a distância média

    if n_arquivo:
        nome_arquivo = n_arquivo
    else:
        nome_arquivo = datetime.now().strftime("%d%m%H%M%S")

    with open(f"rep-good-{nome_arquivo}.py", "a") as my_file:
        my_file.write(f'rep = {rep}\n')
        my_file.write(f'good = {goods}\n')
        my_file.write(f'distance = {distance}\n')
        my_file.write(f'novas_imagens = {novas_imagens_coord}')

    with open(f"info-{nome_arquivo}.txt", "a") as my_file:
        my_file.write(f'Quantidade de Patchs = {count}\n')
        my_file.write(f'Tamanho Imagem Original = {imagem_original_numpy.shape}\n')
        my_file.write(f'Tamanho de cada Patch = {patch_numpy.shape}\n')

    return np.array(rep), np.array(goods), novas_imagens_coord

#imagem_original_pil = Image.open(r"../imagens/1.jpg")

#rep, good = crop(imagem_original_pil, 85, 85, 20)

#plt.hist(rep, rwidth=0.9)
#plt.show()