# detdesmat

## SIFT
O objeto `cv2.KeyPoint` é um objeto que representa um keypoint e possui alguns atributos:

'angle', 'class_id', 'convert', 'octave', 'overlap', 'pt', 'response', 'size'

Os descritores são representados por matrizes numpy, com dimensão de M x 128. Sendo M a quantidade de descritores e 128 
números que representam o descritor.

O objeto `cv2.DMatch` representa uma correspondência e possui os seguintes atributos:
'distance', 'imgIdx', 'queryIdx', 'trainIdx'

distance -> Retorna a distância entre os descritores encontrados nas duas imagens. Quanto menor a distância, melhor.
queryIdx ->  Retorna o índice do keypoint da imagem 1. Atente que esse índice também serve para obter o descritor.
Exemplo: 
```
for g in good:
    print(g[0], kp1[g[0].queryIdx], kp2[g[0].trainIdx])
    print(g[0], des1[g[0].queryIdx], g[0].trainIdx)
## 

```
Observe no código acima que o kp1 é uma lista de pontos de interesse. Dessa forma, pode-se passar um número como índice, e ele retornará aquele ponto correspondente. Assim, você pode usar o `g[0].queryIdx` para identificar o índice do keypoint naquela correspondência. Experimente usar também `kp1[g[0].queryIdx].pt` para retornar as coordenasa do ponto.

trainIdx -> Retorna o índice do keypoint da imagem 2.

Observe que duas uma correspondência ocorre entre duas imagens. Dessa forma a primeira imagem pe chamada de query, e a segunda de train.
