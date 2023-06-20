# Trabalho_de_grafos
## Estrutura de dados - Trabalho de grafos

**O código começa importando a biblioteca numpy com a linha import numpy as np. Essa biblioteca é amplamente utilizada para trabalhar com arrays multidimensionais e é particularmente útil para manipular matrizes.**

Em seguida, temos a definição da função representar_grafo(). Essa função foi criada para lidar com grafos e matrizes de adjacências. É dentro dessa função que todo o trabalho será realizado.

Dentro da função, encontramos a declaração da tabela de pesos das arestas com a seguinte linha:

``` python
tabela_pesos = [[0, 33, 44, 22, 17, 11],
                [0, 0, 19, 45, 7, 77],
                [0, 0, 0, 0, 30, 24],
                [0, 0, 0, 0, 10, 5],
                [0, 0, 0, 0, 0, 9],
                [0, 0, 0, 0, 0, 0]]
``` 
Essa tabela representa os pesos das arestas do grafo. Cada linha e coluna representam um vértice, e o valor na posição (i, j) representa o peso da aresta que conecta o vértice i ao vértice j.

Em seguida, é criada a matriz de adjacências a partir da tabela de pesos das arestas:

```python
matriz_adj = np.array(tabela_pesos)
```
A função np.array() da biblioteca numpy é utilizada para criar uma matriz a partir da tabela de pesos das arestas.

Após criar a matriz de adjacências, o código exibe a tabela de pesos das arestas na saída. A exibição é feita com linhas e colunas demarcadas para facilitar a visualização dos dados.

Primeiro, a linha de cabeçalho das colunas é exibida com os nomes dos vértices:

```python
print("\tV1\tV2\tV3\tV4\tV5\tV6")
```
Em seguida, um loop é usado para iterar sobre cada linha da matriz de adjacências e exibir os valores correspondentes às arestas para cada vértice. A formatação é feita para garantir que os valores estejam alinhados corretamente sob cada coluna correspondente ao vértice:

```python
for i, row in enumerate(matriz_adj):
    print(f"V{i+1}\t", end="")
    for value in row:
        print(f"{value}\t", end="")
    print()
```
Dentro desse loop, a função enumerate() é usada para obter o índice (i) e a linha (row) atual da matriz. Em seguida, para cada valor na linha, é exibido o valor com um print() seguido de um caractere de tabulação (\t), para separar os valores em colunas.

Por fim, a função print() vazia é usada após o loop interno para imprimir uma nova linha, garantindo que a próxima linha seja exibida abaixo da atual.

Essa modificação no código permite a exibição da tabela de pesos das arestas na tela com linhas e colunas demarcadas, facilitando a visualização dos dados do grafo.

Com isso, será exibido no console o seguinte resultado:

Tabela de pesos das arestas:
        V1      V2      V3      V4      V5      V6
V1      0       33      44      22      17      11
V2      0       0       19      45      7       77
V3      0       0       0       0       30      24
V4      0       0       0       0       10      5 
V5      0       0       0       0       0       9 
V6      0       0       0       0       0       0 