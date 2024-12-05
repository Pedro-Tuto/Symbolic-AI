import time

def medir_tempo(funcao): # Mede o tempo de execução de uma função específica.
    start_time = time.time() # Marca o tempo inicial em segundos desde a Época (Unix epoch)
    funcao()  # Chama a função que você deseja medir
    end_time = time.time() # Marca o tempo final após a execução da função
    return end_time - start_time # Calcula a diferença entre o tempo final e inicial
