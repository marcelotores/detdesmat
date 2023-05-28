from datetime import datetime
from src import utilidades as ut, sift
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from src.crop_f import crop

imagem_original_pil = Image.open(r"imagens/1.jpg")

rep, good, novas_imagens = crop(imagem_original_pil, 85, 85, 20, 'em_jpg')