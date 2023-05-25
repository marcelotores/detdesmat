# detdesmat

SIFT
O objeto cv2.KeyPoint possui alguns atributos:

'angle', 'class_id', 'convert', 'octave', 'overlap', 'pt', 'response', 'size'

Os descritores são matrizes numpy, com dimensão de 128.

O objeto cv2.DMatch possui os seguintes atributos:
'distance', 'imgIdx', 'queryIdx', 'trainIdx'

O atributo queryIdx retorna o índice do keypoint da imagem 1. Atente que esse índice também serve para obter o descritor.
Exemplo: 
```
for g in good:
    print(g[0], kp1[g[0].queryIdx], kp2[g[0].trainIdx])
    print(g[0], des1[g[0].queryIdx], g[0].trainIdx)

```
