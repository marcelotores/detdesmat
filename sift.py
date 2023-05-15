import cv2 as cv

def sift_detectores_e_descritores(imagem, n=None):

    """ Recebe uma imagem (numpy) e um valor n que representa a quantidade dos n melhores pontos, e retorna uma tupla com os detectores e descritores """

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


