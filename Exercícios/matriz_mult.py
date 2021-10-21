def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)

        matriz.append(linha)
    
    return matriz 

def sao_multiplicaveis(m1, m2):
        num_linhas = len(m1)
        num_colunas = len(m1[0])

        num_linhasB = len(m2)
        num_colunasB = len(m2[0])

        if(num_colunas) == num_linhasB:
            return True
        else:
            return False