def cria_matriz(num_linhas, num_colunas, valor):

    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)

        matriz.append(linha)

    print(matriz)

def dimensoes(matriz):
    tamanho_matriz = (len(matriz), len(matriz[0]))
    print(f"{tamanho_matriz[0]}X{tamanho_matriz[1]}")