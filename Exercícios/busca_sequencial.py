def busca(lista, elemento):

    for indice in range(len(lista)):
        if lista[indice] == elemento:
            return indice
    
    return False