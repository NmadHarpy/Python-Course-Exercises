def conta_letras(frase, contar="vogais"):

    posicao = len(frase) - 1
    contador = 0

    while posicao >= 0:
        if frase[posicao] in 'aeiou':
            contador+=1
        posicao-=1
    
    if contar == 'consoantes':
        frase = frase.replace(' ', '')
        return len(frase) - contador
    else:
        return contador