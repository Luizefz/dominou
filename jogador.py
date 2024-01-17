class jogador():
    def __init__(self, pecas_na_mao):
        self.pecas_na_mao = pecas_na_mao
        self.pecas_restantes = 6
        self.pecas_disponiveis = []
        self.possibilidade_peca = {
            0: '0%', 
            1: '0%', 
            2: '0%', 
            3: '0%',
            4: '0%', 
            5: '0%', 
            6: '0%'
        }
        
    def jogar_peca(self, peca_jogada, cabeca):
        self.cabeca_jogada = self.cabeca_jogada.append(cabeca)
        self.peca_jogada = self.pecas_na_mao.append(peca_jogada)
        
        if peca_jogada in self.pecas_disponiveis:
                self.pecas_disponiveis.remove(peca_jogada)
                self.pecas_restantes -= 1

    
x = jogador

x.possibilidade_peca[3] = '30%'
print(x.possibilidade_peca)