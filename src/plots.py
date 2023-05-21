from matplotlib import pyplot as plt
import numpy as np
path = "../imagens/experimentos"
def rep(repa):
    intervalo_repa = ['<= 0.3', '> 0.3 e <= 0.7', ' > 0.7']
    repa_7 = np.count_nonzero(repa > 0.7)
    repa_03 = np.count_nonzero(repa <= 0.3)
    repa_03_07 = len(repa) - (repa_7 + repa_03)

    plt.bar(intervalo_repa, [repa_03, repa_03_07, repa_7], color="green")
    plt.xlabel("Repetitibilidade  (matching/min[qtd_kp1, qtd_kp2])")
    plt.ylabel("Quantidade de imagens")
    plt.title(f"Repetitibilidade x Imagem - Média: {sum(repa)/len(repa)}")
    plt.savefig(f'rep.png')
    #plt.show()

def cor(goods):
    plt.plot(goods, label='não ordenado')
    plt.plot(np.sort(goods), label='ordenado')
    plt.title(f'Quantidade de Correspondências por Imagem')
    plt.legend()
    plt.xlabel('Imagem')
    plt.ylabel('Qtd. de Correspondências')
    plt.savefig('cor.png')
    #plt.show()

def distancia(distance):
    plt.plot(distance, label='não ordenado')
    plt.plot(np.sort(distance), label='ordenado')
    plt.xlabel('Imagem')
    plt.ylabel('Distância')
    plt.legend()
    plt.title('Média da distância por correspondência')
    plt.savefig('dist.png')
    #plt.show()
