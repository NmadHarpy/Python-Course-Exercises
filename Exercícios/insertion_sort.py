def insertion_sort(lista):

    fim = len(lista)

    for indice in range(fim - 1):
        posicao_do_minimo = indice

        for j in range(indice + 1, fim):
            if lista[j] < lista[posicao_do_minimo]: 
                posicao_do_minimo = j            
        lista[indice], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[indice]
    
    return lista
