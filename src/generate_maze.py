import random
from PIL import Image, ImageDraw, ImageFont

# Função para gerar o labirinto
def generate_maze():
    matriz = [['C' for _ in range(10)] for _ in range(10)]  # 'C' = posição clara
    matriz[0][0] = 'S'  # Entrada (start)
    matriz[9][9] = 'E'  # Saída (end)

    # Obstáculos aleatórios ('O')
    # random.sample vai selecionar n elementos aleatórios de uma lista.
    # Neste caso, irá selecionar entre 10 e 25 números dentre as posições da matriz, com exceção de 0,0 e 9,9
    obstaculos = random.sample([(i, j) for i in range(10) for j in range(10) if (i, j) not in [(0, 0), (9, 9)]], random.randint(25, 30))
    for i, j in obstaculos:
        matriz[i][j] = 'O'

    # Energy +5 ('R5') e +10 ('R10')
    # Mesma lógica dos obstáculos, porém dessa vez vamos selecionar 5 para regarga_5 e 3 para regarga_10
    recarga_5 = random.sample([(i, j) for i in range(10) for j in range(10) if matriz[i][j] == 'C'], 5)
    recarga_10 = random.sample([(i, j) for i in range(10) for j in range(10) if matriz[i][j] == 'C' and (i, j) not in recarga_5], 3)
    for i, j in recarga_5:
        matriz[i][j] = 'R5'
    for i, j in recarga_10:
        matriz[i][j] = 'R10'

    return matriz

# Função para desenhar o labirinto com legenda
def draw_maze_with_legend(matriz):
    # Configurações de tamanho
    cell_size = 50  # Tamanho de cada célula
    maze_size = len(matriz) * cell_size

    # Criando a imagem principal do labirinto
    img = Image.new("RGB", (maze_size, maze_size + 200), "white")  # +200 para a legenda
    draw = ImageDraw.Draw(img)

    # Definindo cores para cada tipo de célula
    color_map = {
        'C': (240, 240, 240),  # Caminho claro (cinza claro)
        'O': (169, 169, 169),  # Obstáculo (cinza escuro)
        'R5': (34, 139, 34),   # Recarga de +5 (verde floresta)
        'R10': (30, 144, 255), # Recarga de +10 (azul dodger)
        'S': (255, 165, 0),    # Ponto inicial (laranja)
        'E': (255, 0, 0)       # Ponto final (vermelho brilhante)
    }

    # Desenhando o labirinto
    for i, row in enumerate(matriz):
        for j, cell in enumerate(row):
            x0 = j * cell_size
            y0 = i * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            draw.rectangle([x0, y0, x1, y1], fill=color_map[cell], outline="black")

    # Adicionando a legenda
    legend_start_y = maze_size + 10
    legend_x = 10
    legend_gap = 35  # Espaçamento entre os itens da legenda

    font = ImageFont.load_default()  # Fonte padrão

    # Legenda com as cores
    for i, (key, color) in enumerate(color_map.items()):
        y = legend_start_y + i * legend_gap
        # Quadrado colorido da legenda
        draw.rectangle([legend_x, y, legend_x + 20, y + 20], fill=color, outline="black")
        # Texto da legenda
        label = {
            'C': "Caminho livre",
            'O': "Obstaculo",
            'R5': "Recarga de energia +5",
            'R10': "Recarga de energia +10",
            'S': "Ponto inicial",
            'E': "Ponto final"
        }[key]
        draw.text((legend_x + 30, y), label, fill="black", font=font)

    return img

# Gerar e salvar o labirinto
if __name__ == "__main__":
    maze = generate_maze()
    for row in maze:
        print(' '.join(row))  # Exibe no console para verificar

    # Gerar a imagem do labirinto com a legenda
    maze_image = draw_maze_with_legend(maze)
    
    maze_image.show()  # Exibe a imagem.

# Função para exibir o maze
def show_maze(matriz):
    # Printando as linhas separadas por ' '
    for linha in matriz:
        print(' '.join(linha))
    print()