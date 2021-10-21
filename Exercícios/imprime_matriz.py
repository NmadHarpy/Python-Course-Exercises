def minha_matriz(num_linhas, num_colunas, valor):

    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
            matriz.append(linha)

        return matriz(i[0], j[0])

def imprime_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print(f'{matriz[i][j]}')
            else:
                print(f'{matriz[i][j]}', end = " ")
    print()