def menor_nome(nomes):
    
    tamanho = len(nomes)
    menor = ''
    lista = []
    
    
    for str in nomes:
        lista.append(str.strip())
        
    
    menor = lista[0]
    for str in lista:
        if len(str) < len(menor):
            menor = str
            
    return menor.capitalize()
