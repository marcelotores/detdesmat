import cv2 as cv

def sift_detectores_e_descritores(imagem, n=None):

    """ Recebe uma imagem (numpy) e um valor n que representa a quantidade dos n melhores pontos, e retorna uma tupla com os ns detectores e descritores """

    # Converte para cinza
    gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)

    # Cria o objeto sift
    sift = cv.SIFT_create()

    # Encontra keypoints
    kp = sift.detect(gray, None)

    # N principais características
    n_kp = sorted(kp, key=lambda x: -x.response)[:n]

    kp, des = sift.compute(gray, n_kp)

    return kp, des

def imprime_detectores(kp):

    """ Dado os pontos de interesse, imprime uma saída formatada """

    if len(kp) == 0:
        print('Não há pontos')
        return

    print('Quantidade de Pontos: ', len(kp))
    print('Coordenadas')
    for i in range(len(kp)):
        print(kp[i], ' - ', kp[i].pt)

    print('Relevância')
    for i in range(len(kp)):
        print(kp[i], ' - ', kp[i].response)


def correspondencias(img1, img2, qtd_match=None, k_best=2, kp1=None, kp2=None, des1=None, des2=None):
    """ Recebe duas imagens (numpy), a (qtd_match) quantitade
        de correspondências que serão desenhadas na imagem, as k melhores correspondências
        que serão calculadas, opcionalmente os kp1, kp2, des1, des2 e retorna uma tupla (kp1, kp2, correspondencias[]) """

    if des1 is None or des2 is None or kp1 is None or kp2 is None:
        kp1, des1 = sift_detectores_e_descritores(img1)
        kp2, des2 = sift_detectores_e_descritores(img2)


    bf = cv.BFMatcher()
    correspondencias = bf.knnMatch(des1, des2, k=k_best)

    # Apply ratio test
    good = []
    for m, n in correspondencias:
        if m.distance < 0.75 * n.distance:
            good.append([m])

    if qtd_match is not None:
        image_out = cv.drawMatchesKnn(img1, kp1, img2, kp2, good[:qtd_match], None,
                                      flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    else:
        image_out = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, None,
                                      flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    #return kp1, kp2, good
    #print(correspondencias)
    return image_out, good, kp1, kp2, correspondencias

