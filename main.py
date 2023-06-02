import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import src.plots as pl
from src.crop_f import crop
from skimage.util import random_noise
from src import utilidades as ut

# Cria um vetor com a lista e ruído
# Após, aplica o ruído a imagem por um laço para todos os ruídos do vetor,
# Dentro do laço, para cada imagem com ruído, já vai calculando a repetibilidade e correspondêncis.

img_original = cv.imread("imagens/1.jpg")
rep, good, novas_imagens_coord = crop(ut.ndarray_pil(img_original), 85, 85, 20, 'segundo_teste')

exit()

img_original = cv.imread("imagens/1.jpg")
#imagem_original_pil = Image.open(r"imagens/1.jpg")

imagem_original_pil = Image.open(r"imagens/1.jpg")


ruidos = ['s&p', 'speckle']


for r in ruidos:
    noise_img = random_noise(img_original, mode=f'{r}')
    noise_img = np.array(255 * noise_img, dtype='uint8')
    #rep, good = crop(ut.ndarray_pil(noise_img), 85, 85, 20, r)

## OU

img_original = cv.imread("imagens/1.jpg")
rep, good, novas_imagens_coord = crop(ut.ndarray_pil(img_original), 85, 85, 20, 'segundo_teste')