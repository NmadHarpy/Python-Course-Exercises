def cria_matriz(num_linhas, num_colunas): # Função cria_matriz que recebe 3 parâmetros. cria_matriz alterada, antigo: (num_linhas, num_colunas, valor)
    '''(int, int, valor) -> matriz (lista de listas)
        Cria e retorna uma matriz com num_linhas linhas e num_colunas colunas -
        em que cada elemento é igual ao valor dado'''

    matriz = [] #lista vazia
    for i in range(num_linhas):
        # Cria a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)

        # Adiciona linha à matriz
        matriz.append(linha)
    
    return matriz

def le_matriz():
    lin = int(input("Número de Linhas da matriz: "))
    col = int(input("Número de Colunas da matriz: "))
    return cria_matriz(lin, col)