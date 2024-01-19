class jogador():
    def __init__(self):
        self.pecas_restantes = 6
        self.pecas_na_mao = []
        self.pecas_pesos = {
            (0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0, (0, 5): 0, (0, 6): 0,
            (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0, (1, 5): 0, (1, 6): 0,
            (2, 2): 0, (2, 3): 0, (2, 4): 0, (2, 5): 0, (2, 6): 0,
            (3, 3): 0, (3, 4): 0, (3, 5): 0, (3, 6): 0,
            (4, 4): 0, (4, 5): 0, (4, 6): 0,
            (5, 5): 0, (5, 6): 0,
            (6, 6): 0
        }
        self.pecas_porcentagem = {
            (0, 0): "0%", (0, 1): "0%", (0, 2): "0%", (0, 3): "0%", (0, 4): "0%", (0, 5): "0%", (0, 6): "0%",
            (1, 1): "0%", (1, 2): "0%", (1, 3): "0%", (1, 4): "0%", (1, 5): "0%", (1, 6): "0%",
            (2, 2): "0%", (2, 3): "0%", (2, 4): "0%", (2, 5): "0%", (2, 6): "0%",
            (3, 3): "0%", (3, 4): "0%", (3, 5): "0%", (3, 6): "0%",
            (4, 4): "0%", (4, 5): "0%", (4, 6): "0%",
            (5, 5): "0%", (5, 6): "0%",
            (6, 6): "0%"
        }

    def guardar_cabeca_jogada(self, cabeca):
        for chave in self.pecas_pesos.keys():
            for i in chave:
                if i == cabeca:
                    self.pecas_pesos[chave] += 1
                    break

    def retorna_pecas_peso(self):
        return self.pecas_pesos

    def retorna_pecas_porcentagem(self):
        return self.pecas_porcentagem

    def retorna_pecas_restantes(self):
        return self.pecas_restantes

    def diminue_quant_pecas_restantes(self):
        self.pecas_restantes -= 1
