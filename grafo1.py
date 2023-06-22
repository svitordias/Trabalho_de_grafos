import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

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

    # Criando uma string com a tabela formatada
    tabela_formatada = "Tabela de pesos das arestas:\n"
    tabela_formatada += "\tV1\tV2\tV3\tV4\tV5\tV6\n"
    for i, row in enumerate(matriz_adj):
        tabela_formatada += f"V{i+1}\t"
        for value in row:
            tabela_formatada += f"{value}\t"
        tabela_formatada += "\n"

    # Salvando a tabela formatada em um arquivo de texto
    with open("grafo.txt", "w") as file:
        file.write(tabela_formatada)

    # Criando o objeto grafo
    G = nx.Graph()

    # Adicionando os nós
    G.add_nodes_from(range(1, len(matriz_adj) + 1))

    # Adicionando as arestas com os respectivos pesos
    for i in range(len(matriz_adj)):
        for j in range(i + 1, len(matriz_adj)):
            if matriz_adj[i][j] != 0:
                G.add_edge(i + 1, j + 1, weight=matriz_adj[i][j])

    # Plotando o grafo
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Exibindo o gráfico
    plt.show()

# Executando a função para representar o grafo, salvar a tabela em um arquivo de texto e plotar o grafo
representar_grafo()