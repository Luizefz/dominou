from domino_classes import jogador, dorme
from calc_probabilidade import calcula_probabilidade_pecas


def pecas_jogadas_jogador(jogador: int, peca_jogada: tuple, cabeca: str) -> None:
    global jogador_00
    global jogador_01
    global jogador_02
    global jogador_03

    match jogador:
        case 0:
            for i in range(6):
                minha_peca_jogada = eval(input(f'\nInsira sua {i+1}ª\npeça Ex: (0, 0)\n'))
                if minha_peca_jogada in pecas_disponiveis:
                    del pecas_disponiveis[minha_peca_jogada]
                else:
                    print('Peça não disponível')

        case 1:
            jogador_01.guardar_cabeca_jogada(cabeca)
            pecas_dorme.guardar_cabeca_jogada(cabeca)
            if peca_jogada in pecas_disponiveis:
                del pecas_disponiveis[peca_jogada]
                jogador_01.diminue_quant_pecas_restantes()
            else:
                print('Peça não disponível')

        case 2:
            jogador_02.guardar_cabeca_jogada(cabeca)
            pecas_dorme.guardar_cabeca_jogada(cabeca)
            if peca_jogada in pecas_disponiveis:
                del pecas_disponiveis[peca_jogada]
                jogador_02.diminue_quant_pecas_restantes()
            else:
                print('Peça não disponível')

        case 3:
            jogador_03.guardar_cabeca_jogada(cabeca)
            pecas_dorme.guardar_cabeca_jogada(cabeca)
            if peca_jogada in pecas_disponiveis:
                del pecas_disponiveis[peca_jogada]
                jogador_03.diminue_quant_pecas_restantes()
            else:
                print('Peça não disponível')

        case 4:
            pecas_dorme.guardar_cabeca_jogada(cabeca)
            if peca_jogada in pecas_disponiveis:
                del pecas_disponiveis[peca_jogada]
                pecas_dorme.diminue_quant_pecas_restantes()
            else:
                print('Peça não disponível')


pecas_disponiveis = {(0, 0): 1, (0, 1): 1, (0, 2): 1, (0, 3): 1, (0, 4): 1, (0, 5): 1, (0, 6): 1,
                     (1, 1): 1, (1, 2): 1, (1, 3): 1, (1, 4): 1, (1, 5): 1, (1, 6): 1,
                     (2, 2): 1, (2, 3): 1, (2, 4): 1, (2, 5): 1, (2, 6): 1,
                     (3, 3): 1, (3, 4): 1, (3, 5): 1, (3, 6): 1,
                     (4, 4): 1, (4, 5): 1, (4, 6): 1,
                     (5, 5): 1, (5, 6): 1,
                     (6, 6): 1}


jogador_00 = jogador()
jogador_01 = jogador()
jogador_02 = jogador()
jogador_03 = jogador()
pecas_dorme = dorme()

rodada = -1

while True:
    rodada += 1
    print(f'\nRodada {rodada}')

    if jogador_01.retorna_pecas_restantes() == 0 or jogador_02.retorna_pecas_restantes() == 0 or jogador_03.retorna_pecas_restantes() == 0:
        break

    print(f'\npecas restantes jogador 00: {jogador_00.retorna_pecas_restantes()}\npeca restantes jogador 01: {jogador_01.retorna_pecas_restantes()}\npeca restantes jogador 02: {jogador_02.retorna_pecas_restantes()}\npeca restantes jogador 03: {jogador_03.retorna_pecas_restantes()}\n')
    print(f'pecas disponiveis: \n{list(pecas_disponiveis.keys())}\n')

    jogador_vez, peca_jogada, cabeca = input(
        'Insira respectivamente:\njogador da vez | peça jogada Ex: (0, 0) | cabeca-jogada\n').split()
    pecas_jogadas_jogador(int(jogador_vez), eval(peca_jogada), int(cabeca))

    # Caso na primeira rodada ninguém tenha o (6,6) o jogador 4 (dorme) está com o (6,6)
    if rodada == 1 and peca_jogada != '(6,6)':
        pecas_jogadas_jogador(4, (6, 6), 6)

    todo_mundo_jogou = rodada % 3 == 0

    if todo_mundo_jogou:
        print('\nCalculando probabilidade das peças...')

        probalidade_pecas_jogador_01 = calcula_probabilidade_pecas(
            pecas_disponiveis, jogador_01.retorna_pecas_peso(), jogador_01.retorna_pecas_restantes(), 1000)
        probalidade_pecas_jogador_02 = calcula_probabilidade_pecas(
            pecas_disponiveis, jogador_02.retorna_pecas_peso(), jogador_02.retorna_pecas_restantes(), 1000)
        probalidade_pecas_jogador_03 = calcula_probabilidade_pecas(
            pecas_disponiveis, jogador_03.retorna_pecas_peso(), jogador_03.retorna_pecas_restantes(), 1000)
        probalidade_pecas_dorme = calcula_probabilidade_pecas(
            pecas_disponiveis, pecas_dorme.retorna_pecas_peso(), pecas_dorme.retorna_pecas_restantes(), 1000)

        print(f'\nJogador 01: {probalidade_pecas_jogador_01}')
        print(f'\nJogador 02: {probalidade_pecas_jogador_02}')
        print(f'\nJogador 03: {probalidade_pecas_jogador_03}')
        print(f'\nDorme: {probalidade_pecas_dorme}\n')

        print(f'\nAnalise e escolha a melhor peça para jogar.')
