import random as rd

def resultado_probaliddade_num(pecas_disponiveis):   
    return rd.sample(pecas_disponiveis, 4)
        

def verifica_probabilidade(i, resultado_sorteio) -> bool:
    if i in resultado_sorteio:
        return True
    return
    
def verifica_peca_sorteio(pecas_disponiveis: dict, domino_dict):
    for i in pecas_disponiveis:
        resultado_sorteio = resultado_probaliddade_num(pecas_disponiveis)
        verificaca = verifica_probabilidade(i, resultado_sorteio)
        
        if verificaca == True:
            domino_dict[i] += 1
            
    return print(f'dicionario com o valores que apareceram no sortei:\n{domino_dict},\nResultado do sorteio:\n{resultado_sorteio}')
            
            
            
dicionario_teste = {(0, 0):0, (0, 1):0, (0, 2):0, (0, 3):0, (0, 4):0, (0, 5):0, (0, 6):0,
                 (1, 1):0, (1, 2):0, (1, 3):0, (1, 4):0, (1, 5):0, (1, 6):0,
                 (2, 2):0, (2, 3):0, (2, 4):0, (2, 5):0, (2, 6):0,
                 (3, 3):0, (3, 4):0, (3, 5):0, (3, 6):0,
                 (4, 4):0, (4, 5):0, (4, 6):0,
                 (5, 5):0, (5, 6):0,
                 (6, 6):0
                 }

print(verifica_peca_sorteio([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                 (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                 (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                 (3, 3), (3, 4), (3, 5), (3, 6),
                 (4, 4), (4, 5), (4, 6),
                 (5, 5), (5, 6),
                 (6, 6)], dicionario_teste))

    
    



print(resultado_probaliddade_num([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                 (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                 (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                 (3, 3), (3, 4), (3, 5), (3, 6),
                 (4, 4), (4, 5), (4, 6),
                 (5, 5), (5, 6),
                 (6, 6)]))

