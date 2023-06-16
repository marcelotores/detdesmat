# Importing Image class from PIL module
from PIL import Image
from matplotlib import pyplot as plt
from src import utilidades as ut
import numpy as np
from src import sift
import src.plots as pl
from datetime import datetime
from src.new_encaixa import encaixa
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
    te = 0
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
            nova_imagem = imagem_original_numpy

            ## Calculando descritores
            kp1, des1 = sift.sift_detectores_e_descritores(patch_numpy)
            kp2, des2 = sift.sift_detectores_e_descritores(imagem_original_numpy)

            ## Calculando Correspondências
            imagem_out, good, kp1, kp2 = sift.correspondencias(patch_numpy, imagem_original_numpy, kp1=kp1, kp2=kp2, des1=des1, des2=des2)

            ################ Recebe da função encaixa os novos nos quais o patch será encaixado
            novo_top, novo_bottom, novo_left, novo_right, distancia_total = \
                encaixa(good, kp1, kp2, imagem_original_numpy, patch_numpy, left, right, top, bottom)

            ### print(left, right, top, bottom)
            ### print(novo_left, novo_right, novo_top, novo_bottom)

            novas_imagens_coord.append([novo_left, novo_top, novo_right, novo_bottom, distancia_total])

            ## Apenas dar destaque a cor do patch
            #patch_numpy = cv.cvtColor(patch_numpy, cv.COLOR_BGR2RGB)

            ############### Teste ##############

            if novo_right > imagem_original_numpy.shape[1] or novo_bottom > imagem_original_numpy.shape[0]:

                # if novo_right > imagem_original_numpy.shape[1] and novo_bottom <= imagem_original_numpy.shape[0]:
                #     largura_patch = imagem_original_numpy.shape[1] - novo_left
                #     nova_imagem[int(novo_top):int(novo_bottom), int(novo_left):int(novo_right)] = patch_numpy[
                #                                                                                   0:85,
                #                                                                                   0:largura_patch]
                #
                # if novo_bottom > imagem_original_numpy.shape[0] and novo_right <= imagem_original_numpy.shape[1]:
                #     altura_patch = imagem_original_numpy.shape[0] - novo_top
                #     nova_imagem[int(novo_top):int(novo_bottom), int(novo_left):int(novo_right)] = patch_numpy[
                #                                                                                   0:altura_patch,
                #                                                                                   0:85]
                # if novo_right > imagem_original_numpy.shape[1] and novo_bottom > imagem_original_numpy.shape[0]:
                #     largura_patch = imagem_original_numpy.shape[1] - novo_left
                #     altura_patch = imagem_original_numpy.shape[0] - novo_top
                #     nova_imagem[int(novo_top):int(novo_bottom), int(novo_left):int(novo_right)] = patch_numpy[
                #                                                                                   0:altura_patch,
                #                                                                                   0:largura_patch]
                te+=1
                continue
            else:
                pass
                #nova_imagem[int(novo_top):int(novo_bottom), int(novo_left):int(novo_right)] = patch_numpy

            #####################################


            ################## Recorta imagem no limte da mudança ##################
            if (left < int(novo_left)) or (top < int(novo_top)):
                #novo_patch = ut.corta(ut.ndarray_pil(nova_imagem), left, top, int(novo_right), int(novo_bottom))
                patch = ut.corta(ut.ndarray_pil(imagem_original_numpy), left, top, int(novo_right), int(novo_bottom))

            elif (int(novo_left) < left) or (int(novo_bottom) < top):
                #novo_patch = ut.corta(ut.ndarray_pil(nova_imagem), int(novo_left), int(novo_top), right, bottom)
                patch = ut.corta(ut.ndarray_pil(imagem_original_numpy), int(novo_left), int(novo_top), right, bottom)

            else:
                #novo_patch = ut.corta(ut.ndarray_pil(nova_imagem), left, top, right, bottom)
                patch = ut.corta(ut.ndarray_pil(imagem_original_numpy), left, top, right, bottom)
            ###################                Fim                ##################


            ## Salva novo patch
            #cv.imwrite(f"/home/infra/PycharmProjects/mestrado/pesquisa/detdesmat/imagens/encaixa_patch/{count}.jpg", ut.ndarray_pil(novo_patch, False))

            ## Salva o patch original
            cv.imwrite(f"/home/infra/PycharmProjects/mestrado/pesquisa/detdesmat/imagens/patch_manter/{count}.jpg", ut.ndarray_pil(patch, False))

            ## Salva a imagem inteira com o patch inserido
            #cv.imwrite(f"/home/infra/PycharmProjects/mestrado/pesquisa/detdesmat/imagens/encaixa/{count}.jpg", imagem_original_numpy)


            ########################################## path of house's computer ############################################
            # cv.imwrite(f"/home/marcelo/projetos/mestrado/pesquisa/detdesmat/imagens/encaixa_patch/{count}.jpg", novo_patch)


            print('##################################################################')
            print(f'#### Patch {count} ---> {len(kp1)}:{len(kp2)} -- {len(good)} ####')

            ## Colocando as correspondências na lista de correspondências
            goods.append(len(good))

            ## Calculo da distancia mínima, máxima e média entre cada correspondência
            if len(good) != 0:
                good_np = np.array(good)
                good_np = good_np.reshape(good_np.shape[0], )
                arr_distance = np.array([])
                repetitibilidade = good_np.shape[0] / (min(len(kp1), len(kp2)))

                ## Lista de repetitibilidade de cada key point
                rep.append(repetitibilidade)

                count_0 = 0
                for g in good_np:
                    arr_distance = np.append(arr_distance, g.distance)
                    if g.distance == 0:
                        count_0 += 1

                ## Lista de média de distância entre as correspondências
                distance.append(np.average(arr_distance))
            count+=1


    ## Gerará um arquivo info.py com a lista de repetitibilidade entre as correspondências, as correspondências e a distância média

    # Define o nome do arquivo
    if n_arquivo:
        nome_arquivo = n_arquivo
    else:
        nome_arquivo = datetime.now().strftime("%d%m%H%M%S")

    ## Cria arquivo com a lista de reptibilidade, correspondências e as Distâncias e as Coordenadas dos novos patches
    with open(f"rep-good-{nome_arquivo}.py", "a") as my_file:
        my_file.write(f'rep = {rep}\n')
        my_file.write(f'good = {goods}\n')
        my_file.write(f'distance = {distance}\n')
        my_file.write(f'novas_imagens = {novas_imagens_coord}')

    ## Tabém cria um arquivo com informações gerais sobre as imagens
    with open(f"info-{nome_arquivo}.txt", "a") as my_file:
        my_file.write(f'Quantidade de Patchs = {count}\n')
        my_file.write(f'Tamanho Imagem Original = {imagem_original_numpy.shape}\n')
        my_file.write(f'Tamanho de cada Patch = {patch_numpy.shape}\n')

    return np.array(rep), np.array(goods), novas_imagens_coord

