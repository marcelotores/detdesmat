import cv2 as cv
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
    thickness = 2

    # Draw a circle with blue line borders of thickness of 2 px
    image = cv.circle(image, center_coordinates, radius, color, thickness)

    #cv.imshow('Imagem', image)
    #cv.imwrite('imagem_com_ponto.jpg', image)
    #cv.waitKey(0)

    return image

def corta(im, left, top, right, bottom):

    im1 = im.crop((left, top, right, bottom))
    return im1