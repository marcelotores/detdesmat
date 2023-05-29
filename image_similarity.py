import cv2 as cv
from os import listdir
from os.path import join
#from sewar.full_ref import mse, rmse, psnr, uqi, ssim, ergas, scc, rase, sam, msssim, vifp
import sewar.full_ref as s

from src import plots

img_original = cv.imread("imagens/1.jpg")

print('Padrão: ', s.rmse(img_original, img_original))

path_img_def_caminho = 'imagens/encaixa'

mse = []
rmse = []
psnr = []
ssim = []
uqi = []
msssim = []
ergas = []
scc = []
rase = []
sam = []
vifp = []
for filename in listdir(path_img_def_caminho):
    if filename.endswith(''):
        with open(join(path_img_def_caminho, filename)) as f:
            path_img_def_caminho_comp = path_img_def_caminho + '/' + filename
            img_def = cv.imread(path_img_def_caminho_comp)
            ## Calculando a similaridade em cada método
            #mse.append(s.mse(img_original, img_def))
            #rmse.append(s.rmse(img_original, img_def))
            #psnr.append(s.psnr(img_original, img_def))
            #ssim.append(s.ssim(img_original, img_def))
            #uqi.append(s.uqi(img_original, img_def))
            #msssim.append(s.msssim(img_original, img_def))
            #ergas.append(s.ergas(img_original, img_def))
            #scc.append(s.scc(img_original, img_def))
            #rase.append(s.rase(img_original, img_def))
            #sam.append(s.sam(img_original, img_def))
            vifp.append(s.vifp(img_original, img_def))

#print(mse)

#plots.hist(mse, 'Similaridade', 'Quantidade de Imagens', f'MSE (Padrão - {s.mse(img_original, img_original)})')
#plots.hist(rmse, 'Similaridade', 'Quantidade de Imagens', f'RMSE (Padrão - {s.rmse(img_original, img_original)})')
#plots.hist(psnr, 'Similaridade', 'Quantidade de Imagens', f'PSNR (Padrão - {s.psnr(img_original, img_original)})')
#plots.hist(ssim, 'Similaridade', 'Quantidade de Imagens', f'SSIM (Padrão - {s.ssim(img_original, img_original)})')
#plots.hist(uqi, 'Similaridade', 'Quantidade de Imagens', f'UQI (Padrão - {s.uqi(img_original, img_original)})')
#plots.hist(msssim, 'Similaridade', 'Quantidade de Imagens', f'MSSSIM (Padrão - {s.msssim(img_original, img_original)})')
#plots.hist(ergas, 'Similaridade', 'Quantidade de Imagens', f'ERGAS (Padrão - {s.ergas(img_original, img_original)})')
#plots.hist(scc, 'Similaridade', 'Quantidade de Imagens', f'SCC (Padrão - {s.scc(img_original, img_original)})')
#plots.hist(rase, 'Similaridade', 'Quantidade de Imagens', f'RASE (Padrão - {s.rase(img_original, img_original)})')
#plots.hist(sam, 'Similaridade', 'Quantidade de Imagens', f'SAM (Padrão - {s.sam(img_original, img_original)})')
plots.hist(vifp, 'Similaridade', 'Quantidade de Imagens', f'VIFP (Padrão - {s.vifp(img_original, img_original)})')


