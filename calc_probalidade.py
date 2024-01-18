import random as rd

dicionario_teste = {(0, 0):0, (0, 1):0, (0, 2):0, (0, 3):0, (0, 4):0, (0, 5):0, (0, 6):0,
                 (1, 1):0, (1, 2):0, (1, 3):0, (1, 4):0, (1, 5):0, (1, 6):0,
                 (2, 2):0, (2, 3):0, (2, 4):0, (2, 5):0, (2, 6):0,
                 (3, 3):0, (3, 4):0, (3, 5):0, (3, 6):0,
                 (4, 4):0, (4, 5):0, (4, 6):0,
                 (5, 5):0, (5, 6):0,
                 (6, 6):0
                 }

dicionario_pecas_peso = {(0, 0):0, (0, 1):0, (0, 2):0, (0, 3):0, (0, 4):0, (0, 5):0, (0, 6):0,
                 (1, 1):0, (1, 2):0, (1, 3):0, (1, 4):0, (1, 5):0, (1, 6):0,
                 (2, 2):0, (2, 3):0, (2, 4):0, (2, 5):0, (2, 6):0,
                 (3, 3):0, (3, 4):0, (3, 5):0, (3, 6):0,
                 (4, 4):0, (4, 5):0, (4, 6):0,
                 (5, 5):0, (5, 6):0,
                 (6, 6):0
                 }


def pegar_pecas_aleatorias_dic(pecas_disponiveis, quant_elementos_aleatorios): 
    numeros_aleatorios = rd.sample(pecas_disponiveis, quant_elementos_aleatorios)
    return numeros_aleatorios

def verifica_pecas_alea_dispo(peca_aleatoria, pecas_disponiveis):
    if peca_aleatoria in pecas_disponiveis:
        return True
    return
    
    
def verifica_peca_sorteio(pecas_disponiveis: dict, domino_dict, quant_elementos_aleatorios):
    
    resultado_sorteio = pegar_pecas_aleatorias_dic(pecas_disponiveis, quant_elementos_aleatorios)
    
    for i in resultado_sorteio:
        verificaca = verifica_pecas_alea_dispo(i, pecas_disponiveis)
        
        if verificaca == True:
            domino_dict[i] += 1
            
    return domino_dict
            
            
for i in range(100):
    s = verifica_peca_sorteio([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                                            (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                                            (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                                            (3, 3), (3, 4), (3, 5), (3, 6),
                                            (4, 4), (4, 5), (4, 6),
                                            (5, 5), (5, 6),
                                            (6, 6)], dicionario_teste, 4)
    domino_teste = s
    
domino_teste = sorted(domino_teste.items(), key=lambda x: x[1], reverse=True)
print(f'\n{domino_teste}')
