import cv2 as cv

def encaix(good, kp1, kp2, imagem_original_numpy, patch_numpy, left, right, top, bottom):

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

        # print('Distancia entre pixels: ', (novo_x - x2), (novo_y - y2))
        ############################################################################

        ## Somando todos os y e x para ver a diferença de posição entre as coordenadas do patch e da imagem orig
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
    print(f'novo_bottom = {bottom} + {dif_y}')
    print(novo_bottom)
    print(int(novo_bottom))

    ## Apenas dar destaque a cor do patch
    ##patch_numpy = cv.cvtColor(patch_numpy, cv.COLOR_BGR2RGB)

    ## Encaixando o patch na imagem original
    #imagem_original_numpy[int(novo_top):int(novo_bottom), int(novo_left):int(novo_right)] = patch_numpy
    #cv.imshow('', imagem_original_numpy)
    #cv.waitKey(0)

    return int(novo_top), int(novo_bottom), int(novo_left), int(novo_right), distancia_total