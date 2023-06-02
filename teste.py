from datetime import datetime
from src import utilidades as ut, sift
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from src.crop_f import crop
from src.encaixa import encaix
from os import listdir
from os.path import join


#img_original = cv.imread("imagens/1.jpg")


path_img_def_caminho = 'imagens/encaixa_patch'
#path_img_def_caminho = 'imagens/patch_manter'

tamanhos = []
for filename in listdir(path_img_def_caminho):
    if filename.endswith(''):
        with open(join(path_img_def_caminho, filename)) as f:
            path_img_def_caminho_comp = path_img_def_caminho + '/' + filename
            img_def = cv.imread(path_img_def_caminho_comp)
            print(f'{filename}: ', img_def.shape[:2])
            #tamanhos.append(f'{filename}:  {img_def.shape[:2]}')
            #tamanhos.append(f'{img_def.shape[:2]}')

tamanhos = np.array(tamanhos)
#print(tamanhos[:, :])
#print(np.count_nonzero(tamanhos[:, 0] == 85))
#for t in tamanhos:
#    print(t)