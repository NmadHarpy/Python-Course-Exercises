import ordenador
from random import randrange
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [randrange(1000) for x in range(n)]
        return lista
    
    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)] # Faz uma lista ordenada
        lista[n//10] = -500
        return lista


    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = ordenador.Ordenador()

        print("Comparando com listas aleatórias\n")
        antes = time.time()
        o.short_bubble_sort(lista1)
        depois = time.time()
        print(f"Bolha Curta demorou {depois - antes}")

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f"Seleção direta demorou {depois - antes}")

        print("\nComparando com listas quase ordenadas")
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        antes = time.time()
        o.short_bubble_sort(lista1)
        depois = time.time()
        print(f"Bolha Curta demorou {depois - antes}")

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f"Seleção direta demorou {depois - antes}")

'''
if __name__ == '__main__':
    c = ContaTempos()
    c.compara(1000)
    c.lista_aleatoria(300)
    '''