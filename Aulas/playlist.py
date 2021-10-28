class Musica:
    def __init__(self, titulo, interprete, compositor, ano):
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano

class Buscador:
    def busca_por_titulo(self, playlist, titulo):
        for indice in range(len(playlist)):
            if playlist[indice].titulo == titulo:
                return indice
        return -1

    def vamos_buscar(self):
        playlist = [Musica("Ponta de Areia", "Milton Nascimento", "Milton Nascimento", 1975),
                    Musica("Podres Poderes", "Caetano Veloso", "Caetano Veloso", 1984),
                    Musica("Baby", "Gal Costa", "Caetano Veloso", 1969)]

        onde_achou = self.busca_por_titulo(playlist, "Baby")

        if onde_achou == -1:
            print("Música não está na playlist")
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano, sep = ", ")

if __name__ == '__main__':
    b = Buscador()
    b.vamos_buscar()