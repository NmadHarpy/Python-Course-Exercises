def busca(lista, elemento):

    primeiro_elemento = 0
    ultimo_elemento = len(lista) -1

    while primeiro_elemento <= ultimo_elemento:
        meio = (primeiro_elemento + ultimo_elemento) // 2
        if lista[meio] == elemento:
            print(meio)
            return meio
        else:
            if elemento < lista[meio]:
                ultimo_elemento = meio -1
                print(meio)
            else:
                primeiro_elemento = meio +1
                print(meio)
    return False
