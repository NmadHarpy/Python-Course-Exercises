import math

class Bhaskara:
    def delta(self, a, b, c):
        return b ** 2 - 4 * a * c


    def main(self):
        a_digitando = float(input("Digite o valor de a: "))
        b_digitando = float(input("Digite o valor de b: "))
        c_digitando = float(input("Digite o valor de c: "))
        print(self.calcula_raizes(a_digitando, b_digitando, c_digitando))


    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            return 1, raiz1
        else:
            if d < 0:
                return 0
            else:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                raiz2 = (-b - math.sqrt(d)) / (2 * a)
                return 2, raiz1, raiz2
