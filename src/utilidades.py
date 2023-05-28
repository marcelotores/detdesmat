import cv2 as cv
import numpy as np
from PIL import Image
def pontos(image, x, y, cor='B', tamanho=1):

    """ Recebe uma imagem, suas coordenas X, Y e coloca um ponto azul sobre a imagem """

    #image = cv.imread(imagem)

    center_coordinates = (int(x), int(y))
    radius = tamanho
    if cor == 'B':
        color = (255, 0, 0)
    elif cor == 'G':
        color = (0, 255, 0)
    elif cor == 'R':
        color = (0, 0, 255)

    # Line thickness of 2 px
    thickness = 1

    # Draw a circle with blue line borders of thickness of 2 px
    image = cv.circle(image, center_coordinates, radius, color, thickness)

    #cv.imshow('Imagem', image)
    #cv.imwrite('imagem_com_ponto.jpg', image)
    #cv.waitKey(0)

    return image

def corta(im, left, top, right, bottom):

    im1 = im.crop((left, top, right, bottom))
    return im1

def ndarray_pil(img, flag=True):
    """

    :param img: Imagem do tipo ndarray ou PIL
    :param flag: False para pil -> ndarray, True (default) para o oposto
    :return: Uma imagem convertida
    """
    if flag:
        img_np_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return Image.fromarray(img_np_RGB)
    else:
        img_arr = np.array(img)
        img_arr_BGR = cv.cvtColor(img_arr, cv.COLOR_RGB2BGR)
        return img_arr_BGR