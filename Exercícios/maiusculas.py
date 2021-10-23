def maiusculas(frase):
    
    lista = []
    string_retorna = ''
    
    for ch in frase:
        if ord(ch) >=65 and ord(ch) <= 91:
            lista.append(ch)      
    

    string_retorna = ''.join(lista)
    
    return string_retorna