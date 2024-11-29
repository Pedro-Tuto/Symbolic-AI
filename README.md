# Symbolic-AI

## Descrição

O projeto **Symbolic-AI** é uma implementação de algoritmos de busca simbólica, focado em técnicas clássicas de inteligência artificial, como busca em largura (BFS) e algoritmo A*. O objetivo é fornecer um conjunto de ferramentas para explorar conceitos fundamentais de busca e resolução de problemas em IA, com suporte à geração de labirintos para simulações.

## Estrutura do Projeto

- **`main.py`**: Script principal para execução do projeto.
- **`src/`**: Contém a lógica principal do projeto.
  - **`a_star_algorithm.py`**: Implementação do algoritmo A*.
  - **`bfs.py`**: Implementação do algoritmo de busca em largura.
  - **`generate_maze.py`**: Script para geração de labirintos para testes.
- **`.gitignore`**: Arquivo para ignorar arquivos e diretórios no controle de versão.
- **`README.md`**: Documentação do projeto.

## Pré-requisitos

- **Python 3.8+**
- Todas as bibliotecas utilizadas fazem parte da biblioteca padrão do Python.

## Instalação

```bash
1. Clone este repositório:
   git clone <URL_DO_REPOSITORIO>
   cd Symbolic-AI

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows

3. Para executar o projeto principal:
   python main.py

4. Execute os scripts individualmente para testar algoritmos específicos:
   Teste o A*:
   python src/a_star_algorithm.py

   Teste a busca em largura:
   python src/bfs.py

5. Geração de Labirintos:
   python src/generate_maze.py
