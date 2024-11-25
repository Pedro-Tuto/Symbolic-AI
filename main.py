from src.a_star_algorithm import a_star
from src.bfs import bfs
from src.generate_maze import generate_maze, show_maze


# Movimentos possíveis
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita

# Gerando Labirinto
maze = generate_maze()
show_maze(maze)

# Resolvendo com BFS
print("Busca em Largura (BFS):")
path, remaining_energy = bfs(maze, moves)
if path:
    print(f"Caminho encontrado: {path}")
    print(f"Energia restante: {remaining_energy}")
else:
    print("Sem solução viável.")

# Resolvendo com A*
print("\nAlgoritmo A*:")
path, remaining_energy = a_star(maze, moves)
if path:
    print(f"Caminho encontrado: {path}")
    print(f"Energia restante: {remaining_energy}")
else:
    print("Sem solução viável.")
