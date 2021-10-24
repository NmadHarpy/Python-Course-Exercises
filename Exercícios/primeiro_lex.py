def primeiro_lex(lista):

    primeiro_item = lista[0]
    
    for str in lista:
        if ord(str[0]) < ord(primeiro_item[0]):
            primeiro_item = str

    return primeiro_item
