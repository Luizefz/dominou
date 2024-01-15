class jogador():
    def __init__(self, pecas_na_mao):
        self.pecas_na_mao = pecas_na_mao
        self.pecas_restantes = 6
        self.pecas_disponiveis = []
        
    def jogar_peca(self, peca_jogada, cabeca):
        self.cabeca_jogada = self.cabeca_jogada.append(cabeca)
        self.peca_jogada = self.pecas_na_mao.append(peca_jogada)
        
        if peca_jogada in self.pecas_disponiveis:
                self.pecas_disponiveis.remove(peca_jogada)
                self.pecas_restantes -= 1