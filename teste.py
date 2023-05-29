from datetime import datetime
from src import utilidades as ut, sift
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from src.crop_f import crop
from src.encaixa import encaix
from sewar.full_ref import mse, rmse, psnr, uqi, ssim, ergas, scc, rase, sam, msssim, vifp

img_original = cv.imread("imagens/1.jpg")
img_def = cv.imread("imagens/encaixa/0.jpg")
print("MSE: ", mse(img_original, img_def))




