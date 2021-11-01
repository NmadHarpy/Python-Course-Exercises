import ordenador
import pytest
import tempo_execucao

class TestaOrdenador():

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()
    
    @pytest.fixture
    def l_quase(self):
        c = tempo_execucao.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c  = tempo_execucao.ContaTempos()
        return c.lista_aleatoria(100)
    
    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

    def test_short_bubble_sort_aleat(self, o, l_aleat):
        o.short_bubble_sort(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_selecao_direta_aleat(self, o, l_aleat):
        o.short_bubble_sort(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_short_bubble_sort_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_short_bubble_sort_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)
