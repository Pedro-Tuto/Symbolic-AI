from queue import Queue

'''
O algoritmo BFS explora todos os caminhos possíveis no labirinto de forma ordenada. 
Ele usa uma fila para garantir que o caminho seja analisado nível por nível.
'''
def bfs(maze, moves):
    queue = Queue() # Cria uma fila dos possíveis passos
    queue.put((0, 0, 50, []))  # posição (x, y), energia, caminho percorrido
    visited = set() # Conjunto para guardar as posições já visitadas

    while not queue.empty():
        x, y, energy, path = queue.get() # Retira a próxima posição da fila

        # Se já visitado, pula
        if (x, y) in visited:
            continue
        visited.add((x, y)) # Adiciona a posição no conjunto de visitados

        # Se chegou ao destino
        if (x, y) == (9, 9):
            return path + [(x, y)], energy # Retorna o caminho que percorreu (definido em []) + energia restante

        # Movimentos possíveis
        for dx, dy in moves: # Testa todos os movimentos possíveis (cima, baixo, esquerda, direita)
            nx, ny = x + dx, y + dy # Calcula a nova posição
            # Verifica se:
            # O robô está dentro dos limites do labirinto
            # O robô não está em um quadrado já visitado
            # O robô não está tentando percorrer um obstáculo
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in visited and maze[nx][ny] != 'O':
                new_energy = energy - 1 # Atualiza a energia gasta
                if maze[nx][ny] == 'R5': # Repara a energia, caso esta seja a posição
                    new_energy += 5
                elif maze[nx][ny] == 'R10':
                    new_energy += 10

                if new_energy > 0: # Se o robô ainda tiver energia
                    queue.put((nx, ny, new_energy, path + [(x, y)])) # Atualiza a fila

    return None, 0  # Sem solução