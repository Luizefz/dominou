import random as rd

dicionario_teste = {
    (0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0, (0, 5): 0, (0, 6): 0,
    (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0, (1, 5): 0, (1, 6): 0,
    (2, 2): 0, (2, 3): 0, (2, 4): 0, (2, 5): 0, (2, 6): 0,
    (3, 3): 0, (3, 4): 0, (3, 5): 0, (3, 6): 0,
    (4, 4): 0, (4, 5): 0, (4, 6): 0,
    (5, 5): 0, (5, 6): 0,
    (6, 6): 0
}

dicionario_pecas_peso = {
    (0, 0): 1, (0, 1): 1, (0, 2): 1, (0, 3): 1, (0, 4): 1, (0, 5): 1, (0, 6): 1,
    (1, 1): 1, (1, 2): 1, (1, 3): 1, (1, 4): 1, (1, 5): 1, (1, 6): 1,
    (2, 2): 1, (2, 3): 1, (2, 4): 1, (2, 5): 1, (2, 6): 1,
    (3, 3): 1, (3, 4): 1, (3, 5): 1, (3, 6): 1,
    (4, 4): 1, (4, 5): 1, (4, 6): 1,
    (5, 5): 1, (5, 6): 1,
    (6, 6): 1
}


def pegar_pecas_aleatorias_dic(pecas_disponiveis: dict, quant_pecas_sorteadas: int, dict_pesos: dict):
    # Extrai as chaves e os pesos como listas separadas
    chaves = list(pecas_disponiveis.keys())
    pesos = list(dict_pesos.values())

    # Usa rd.choices para sortear as chaves com base nos pesos
    chaves_sorteadas = rd.choices(
        chaves, weights=pesos, k=quant_pecas_sorteadas)

    # Retorna as chaves sorteadas
    return chaves_sorteadas


def verifica_pecas_alea_dispo(peca_aleatoria, pecas_disponiveis):
    if peca_aleatoria in pecas_disponiveis:
        return True
    return


def verifica_peca_sorteio(pecas_disponiveis: dict, pecas_pesos, quant_pecas_sorteadas):

    resultado_sorteio = pegar_pecas_aleatorias_dic(
        pecas_disponiveis, quant_pecas_sorteadas, pecas_pesos)

    for i in resultado_sorteio:
        verificaca = verifica_pecas_alea_dispo(i, pecas_disponiveis)

        if verificaca == True:
            pecas_disponiveis[i] += 1

    return pecas_disponiveis


def calcula_probabilidade_pecas(pecas_disponiveis: dict, pecas_pesos: dict, quant_pecas_sorteadas: int):
    for i in range(100):
        s = verifica_peca_sorteio(
            pecas_disponiveis, pecas_pesos, quant_pecas_sorteadas)
        dicionario_probabilidades = s

    # Ordena o dicionário deacordo com os maiores valores
    dicionario_probabilidades = dict(sorted(
        dicionario_probabilidades.items(), key=lambda item: item[1], reverse=True))
    return dicionario_probabilidades


print(calcula_probabilidade_pecas(dicionario_teste, dicionario_pecas_peso, 6))

# print([dicionario_pecas_peso[peca] for peca in dicionario_pecas_peso])
