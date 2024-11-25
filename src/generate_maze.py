# Geração do maze
import random


def generate_maze():
    matriz = [['C' for _ in range(10)] for _ in range(10)]  # 'C' = posição clara
    matriz[0][0] = 'S'  # Entrada (start)
    matriz[9][9] = 'E'  # Saída (end)

    # Obstáculos aleatórios ('O')
    # random.sample vai selecionar n elementos aleatórios de uma lista.
    # Neste caso, irá selecionar entre 10 e 25 números dentre as posições da matriz, com exceção de 0,0 e 9,9
    obstaculos = random.sample([(i, j) for i in range(10) for j in range(10) if (i, j) not in [(0, 0), (9, 9)]], random.randint(10, 25))
    for i, j in obstaculos:
        matriz[i][j] = 'O'

    # energy +5 ('R5') e +10 ('R10')
    # Mesma lógica dos obstáculos, porém dessa vez vamos selecionar 5 para regarga_5 e 3 para regarga_10
    recarga_5 = random.sample([(i, j) for i in range(10) for j in range(10) if matriz[i][j] == 'C'], 5)
    recarga_10 = random.sample([(i, j) for i in range(10) for j in range(10) if matriz[i][j] == 'C' and (i, j) not in recarga_5], 3)
    for i, j in recarga_5:
        matriz[i][j] = 'R5'
    for i, j in recarga_10:
        matriz[i][j] = 'R10'

    return matriz

# Função para exibir o maze
def show_maze(matriz):
    # Printando as linhas separadas por ' '
    for linha in matriz:
        print(' '.join(linha))
    print()