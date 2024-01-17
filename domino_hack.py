pecas_disponiveis = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                 (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                 (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                 (3, 3), (3, 4), (3, 5), (3, 6),
                 (4, 4), (4, 5), (4, 6),
                 (5, 5), (5, 6),
                 (6, 6)]

domino_dict = {}
for peca in pecas_disponiveis:
    domino_dict[peca] = "0"
    
print(domino_dict)



def pecas_jogadas_jogador(jogador: int, peca_jogada: tuple, cabeca: int) -> None:
    global jogador_00_pecas_restantes
    global jogador_01_pecas_restantes
    global jogador_02_pecas_restantes
    global jogador_03_pecas_restantes
    
    match jogador:
        case 0:
            jogador_00_cabecas_jogadas.append(cabeca)
            if peca_jogada in pecas_disponiveis:
                pecas_disponiveis.remove(peca_jogada)
                jogador_00_pecas_restantes -= 1    
            else: print('Peça não disponível')
            
        case 1:
            jogador_01_cabecas_jogadas.append(cabeca)
            if peca_jogada in pecas_disponiveis:
                pecas_disponiveis.remove(peca_jogada)
                jogador_01_pecas_restantes -= 1
            else: print('Peça não disponível')
            
        case 2:
            jogador_02_cabecas_jogadas.append(cabeca)
            if peca_jogada in pecas_disponiveis:
                pecas_disponiveis.remove(peca_jogada)
                jogador_02_pecas_restantes -= 1
            else: print('Peça não disponível')
            
        case 3:
            jogador_03_cabecas_jogadas.append(cabeca)
            if peca_jogada in pecas_disponiveis:
                pecas_disponiveis.remove(peca_jogada)
                jogador_03_pecas_restantes -= 1
            else: print('Peça não disponível')

        case 4:
            dorme.append(peca_jogada)
            if peca_jogada in pecas_disponiveis:
                pecas_disponiveis.remove(peca_jogada)
            else: print('Peça não disponível')

            print(f"Add (6,6) dorme: {dorme}")

def guardar_minhas_pecas(pecas_inseridas) -> list:
    pecas_na_mao = []

    # As peças do jogador 00 são removidas da lista de peças disponíveis e retorna suas peças
    if type(pecas_inseridas) == list:

        for peca in pecas_inseridas:
            pecas_na_mao.append(peca)
            pecas_disponiveis.remove(peca)

        print(f'\nPeças salvas! (●\'◡\'●) \n{pecas_na_mao}\n')

    return pecas_na_mao

x = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (3,3)]
    
jogador_00 = guardar_minhas_pecas(x)
jogador_01 = []
jogador_02 = []
jogador_03 = []
dorme = []

jogador_00_cabecas_jogadas = []
jogador_01_cabecas_jogadas = []
jogador_02_cabecas_jogadas = []
jogador_03_cabecas_jogadas = []

jogador_00_pecas_restantes = 6
jogador_01_pecas_restantes = 6
jogador_02_pecas_restantes = 6
jogador_03_pecas_restantes = 6

rodada = 0

while True:
    rodada += 1
    print(f'\nRodada {rodada}')

    if jogador_00_pecas_restantes == 0 or jogador_01_pecas_restantes == 0 or jogador_02_pecas_restantes == 0 or jogador_03_pecas_restantes == 0:
        break
    
    print(f'\npecas restantes jogador 00: {jogador_00_pecas_restantes}\npeca restantes jogador 01: {jogador_01_pecas_restantes}\npeca restantes jogador 02: {jogador_02_pecas_restantes}\npeca restantes jogador 03: {jogador_03_pecas_restantes}\n')
    print(f'pecas disponiveis: \n{pecas_disponiveis}\n')
    
    jogador_vez, peca_jogada, cabeca = input('Insira respectivamente:\njogador-vez (peça jogada) cabeca-jogada\n').split()

    if rodada == 1 and peca_jogada != '(6,6)':
        pecas_jogadas_jogador(4, (6,6), 6)
        
    pecas_jogadas_jogador(int(jogador_vez), eval(peca_jogada), int(cabeca))


    