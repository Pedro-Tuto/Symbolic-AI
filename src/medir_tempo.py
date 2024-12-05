import time

def medir_tempo(funcao):
    start_time = time.time()
    funcao()  # Chama a função que você deseja medir
    end_time = time.time()
    return end_time - start_time
