import psutil
import os
# Mede a quantidade de memória utilizada por um processo ao executar uma função específica.
# Parâmetros: funcao: A função cuja memória consumida será medida.
# Retorna: A quantidade de memória utilizada pela função (em MB).

def medir_memoria(funcao):
    process = psutil.Process(os.getpid())  # Pega o processo atual
    start_memory = process.memory_info().rss / (1024 * 1024)  # Em MB
    
    funcao()  # Chama a função que você deseja medir
    
    end_memory = process.memory_info().rss / (1024 * 1024)  # Em MB
    return end_memory - start_memory  # Calcula a diferença entre o uso final e inicial de memória

