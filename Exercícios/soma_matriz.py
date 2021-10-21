def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)

        matriz.append(linha)
    
    return matriz    

def soma_matrizes(m1, m2):
    num_linhas = len(m1)
    num_colunas = len(m1[0])

    num_linhasB = len(m2)
    num_colunasB = len(m2[0])
    
    if num_linhas == num_linhasB and num_colunas == num_colunasB:
        C = cria_matriz(num_linhas, num_colunas, 0)
        for lin in range(num_linhas):
            for col in range(num_colunas):
                C[lin][col] = m1[lin][col] + m2[lin][col]
        return C
    else:
        return False