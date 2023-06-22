# **Leitura e Plotagem de Grafo**

Este código em Python permite ler uma tabela de pesos de arestas a partir de um arquivo de texto e plotar o grafo correspondente. Além disso, o código também é capaz de plotar o subgrafo gerador conexo de peso mínimo e o subgrafo gerador completo de peso mínimo.

## **Pré-requisitos**

:heavy_check_mark: Python 3.x                 
:heavy_check_mark: Bibliotecas: numpy, networkx, matplotlib

Certifique-se de ter o Python instalado em seu sistema e instale as bibliotecas necessárias executando o seguinte comando:

``` markdown
pip install numpy networkx matplotlib
```

## **Como usar**

- Clone ou faça o download do repositório contendo o arquivo Python.
- Abra o arquivo `tabela_pesos.txt` e edite-o conforme necessário. Cada linha do arquivo deve conter os pesos das arestas separados por espaços. Certifique-se de que o arquivo esteja no mesmo diretório que o arquivo Python.
- Execute o arquivo Python utilizando o seguinte comando:
``` markdown
python nome_do_arquivo.py
```
- O grafo original será plotado em uma janela separada.
- Após fechar a janela do grafo original, a janela do subgrafo gerador conexo de peso mínimo será aberta automaticamente.
- Após fechar a janela do subgrafo gerador conexo, a janela do subgrafo gerador completo de peso mínimo será aberta automaticamente.
- Para encerrar a execução do programa, feche a janela do subgrafo gerador completo.

## **Detalhes da implementação**
O código é dividido em várias funções para melhor organização e modularidade. Aqui estão as principais funções e o que elas fazem:

- `ler_tabela_arquivo(nome_arquivo)`: Lê a tabela de pesos das arestas de um arquivo de texto. Cada linha do arquivo contém os pesos das arestas separados por espaços. A função retorna uma lista com os pesos.

- `plotar_grafo(grafo, titulo)`: Plota o grafo utilizando a biblioteca networkx e exibe o gráfico na tela. O parâmetro `grafo` deve ser um objeto do tipo `networkx.Graph` e `titulo` é uma string que será exibida como título do gráfico.

- `plotar_subgrafo_gerador_conexo(grafo)`: Calcula o subgrafo gerador conexo de peso mínimo do grafo fornecido e o plota utilizando a função `plotar_grafo()`. O parâmetro `grafo` deve ser um objeto do tipo `networkx.Graph`.

O código principal lê a tabela de pesos das arestas do arquivo utilizando a função ler_tabela_arquivo(). Em seguida, a matriz de adjacências é criada a partir da tabela de pesos. O grafo é construído adicionando os nós e as arestas com os pesos correspondentes. Depois disso, o grafo original é plotado utilizando a função plotar_grafo(). Em seguida, o subgrafo gerador conexo de peso mínimo é calculado e plotado utilizando a função plotar_subgrafo_gerador_conexo(). Por fim, o subgrafo gerador completo de peso mínimo é calculado e plotado utilizando a função plotar_subgrafo_gerador_completo(). Cada gráfico é exibido em uma janela separada.

Certifique-se de ter instalado as bibliotecas necessárias para que o código funcione corretamente. Além disso, verifique se o arquivo tabela_pesos.txt está presente no mesmo diretório que o arquivo Python e se a formatação dos pesos está correta no arquivo.
