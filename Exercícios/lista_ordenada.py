def ordenada(lista):
    esta_ordenada = True

    for indice in range(len(lista) -1):
        if lista[indice] > lista [indice + 1]:
            esta_ordenada = False
    
    return esta_ordenada
