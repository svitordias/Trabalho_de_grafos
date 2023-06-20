import numpy as np

# Definindo a função para representar o grafo com base na tabela de pesos das arestas
def representar_grafo():
    # Tabela de pesos das arestas
    tabela_pesos = [[0, 33, 44, 22, 17, 11],
                    [0, 0, 19, 45, 7, 77],
                    [0, 0, 0, 0, 30, 24],
                    [0, 0, 0, 0, 10, 5],
                    [0, 0, 0, 0, 0, 9],
                    [0, 0, 0, 0, 0, 0]]

    # Criando a matriz de adjacências
    matriz_adj = np.array(tabela_pesos)

    # Exibindo a tabela com linhas e colunas demarcadas
    print("Tabela de pesos das arestas:")
    print("\tV1\tV2\tV3\tV4\tV5\tV6")
    for i, row in enumerate(matriz_adj):
        print(f"V{i+1}\t", end="")
        for value in row:
            print(f"{value}\t", end="")
        print()

# Executando a função para representar o grafo
representar_grafo()