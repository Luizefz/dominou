class jogador():
    def __init__(self):
        self.pecas_restantes = 6
        self.pecas_na_mao = []
        self.pecas_pesos = {
            (0, 0): 1, (0, 1): 1, (0, 2): 1, (0, 3): 1, (0, 4): 1, (0, 5): 1, (0, 6): 1,
            (1, 1): 1, (1, 2): 1, (1, 3): 1, (1, 4): 1, (1, 5): 1, (1, 6): 1,
            (2, 2): 1, (2, 3): 1, (2, 4): 1, (2, 5): 1, (2, 6): 1,
            (3, 3): 1, (3, 4): 1, (3, 5): 1, (3, 6): 1,
            (4, 4): 1, (4, 5): 1, (4, 6): 1,
            (5, 5): 1, (5, 6): 1,
            (6, 6): 1
        }
        self.pecas_porcentagem = {}

    def guardar_cabeca_jogada(self, cabeca):
        for chave in self.pecas_pesos.keys():
            if cabeca in chave:
                self.pecas_pesos[chave] += 1


    def retorna_pecas_peso(self):
        return self.pecas_pesos

    def retorna_pecas_porcentagem(self):
        return self.pecas_porcentagem

    def retorna_pecas_restantes(self):
        return self.pecas_restantes

    def diminue_quant_pecas_restantes(self):
        self.pecas_restantes -= 1


class dorme:
    def __init__(self):
        self.pecas_restantes = 4
        self.pecas_dorme = []
        self.pecas_pesos = {
            (0, 0): 1, (0, 1): 1, (0, 2): 1, (0, 3): 1, (0, 4): 1, (0, 5): 1, (0, 6): 1,
            (1, 1): 1, (1, 2): 1, (1, 3): 1, (1, 4): 1, (1, 5): 1, (1, 6): 1,
            (2, 2): 1, (2, 3): 1, (2, 4): 1, (2, 5): 1, (2, 6): 1,
            (3, 3): 1, (3, 4): 1, (3, 5): 1, (3, 6): 1,
            (4, 4): 1, (4, 5): 1, (4, 6): 1,
            (5, 5): 1, (5, 6): 1,
            (6, 6): 1
        }
        self.pecas_porcentagem = {}

   
    def guardar_cabeca_jogada(self, cabeca):
        for chave in self.pecas_pesos.keys():
            if cabeca != chave:
                self.pecas_pesos[chave] += 1

    def diminue_quant_pecas_restantes(self):
        self.pecas_restantes -= 1

    def retorna_pecas_restantes(self):
        return self.pecas_restantes

    def retorna_pecas_peso(self):
        return self.pecas_pesos

    def retorna_pecas_porcentagem(self):
        return self.pecas_porcentagem

    def remove_peca_dorme(self, peca):
        self.pecas_dorme.remove(peca)
