from queue import PriorityQueue

'''
Algoritmo de busca heurística que combina os pontos fortes da busca em largura e busca de custo 
uniforme para encontrar o caminho mais curto de um ponto inicial ao destino.
'''
def a_star(maze, moves):
    pqueue = PriorityQueue() # Criando uma fila de prioridade para usar o algoritmo
    pqueue.put((0, 0, 0, 50, []))  # Custo total, posição (x, y), energia, caminho percorrido
    visited = {}

    while not pqueue.empty():
        cost, x, y, energy, path = pqueue.get()

        # Se já visitado com maior energia, pula
        if (x, y) in visited and visited[(x, y)] >= energy:
            continue
        visited[(x, y)] = energy

        # Se chegou ao destino
        if (x, y) == (9, 9):
            return path + [(x, y)], energy

        # Movimentos possíveis
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and maze[nx][ny] != 'O':
                new_energy = energy - 1
                if maze[nx][ny] == 'R5':
                    new_energy += 5
                elif maze[nx][ny] == 'R10':
                    new_energy += 10

                if new_energy > 0: # Se o robô ainda tiver energia
                    heuristic = abs(nx - 9) + abs(ny - 9) # Distância até a posição final
                    new_cost = cost + 1 + heuristic # Adiciona a estimativa heurística
                    pqueue.put((new_cost, nx, ny, new_energy, path + [(x, y)])) # Atualiza a fila

    return None, 0  # Sem solução