from src.a_star_algorithm import a_star
from src.bfs import bfs
from src.generate_maze import generate_maze, show_maze, draw_maze_with_legend
from src.medir_tempo import medir_tempo
from src.medir_memoria import medir_memoria

# Movimentos possíveis
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita

# Gerando Labirinto
maze = generate_maze()


# Gerando a imagem do labirinto com a legenda
maze_image = draw_maze_with_legend(maze)

# Mostrando o labirinto
maze_image.show()
show_maze(maze)
print()

# Resolvendo com BFS e medindo tempo e memória
print("Busca em Largura (BFS):")
tempo_bfs = medir_tempo(lambda: bfs(maze, moves))
memoria_bfs = medir_memoria(lambda: bfs(maze, moves))

path, remaining_energy = bfs(maze, moves)
if path:
    print(f"Caminho encontrado: {path}")
    print(f"Energia restante: {remaining_energy}")
else:
    print("Sem solução viável.")

print(f"Tempo de execução (BFS): {tempo_bfs:.6f}s")
print(f"Memória consumida (BFS): {memoria_bfs:.2f} MB")

# Resolvendo com A* e medindo tempo e memória
print("\nAlgoritmo A*:")
tempo_a_star = medir_tempo(lambda: a_star(maze, moves))
memoria_a_star = medir_memoria(lambda: a_star(maze, moves))

path, remaining_energy = a_star(maze, moves)
if path:
    print(f"Caminho encontrado: {path}")
    print(f"Energia restante: {remaining_energy}")
else:
    print("Sem solução viável.")

print(f"Tempo de execução (A*): {tempo_a_star:.6f}s")
print(f"Memória consumida (A*): {memoria_a_star:.2f} MB")