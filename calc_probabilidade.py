import random as rd


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


def calcula_probabilidade_pecas(pecas_disponiveis: dict, pecas_pesos: dict, quant_pecas_sorteadas: int, num_repeticoes: int):

    # Verifica quais elementos não estão na segunda lista de pesos
    elementos_faltando = set(pecas_pesos.keys()) - \
        set(pecas_disponiveis.keys())

    # Remove os pesos correspondentes dos elementos ausentes
    for elemento in elementos_faltando:
        pecas_pesos.pop(elemento, None)

    for _ in range(num_repeticoes):
        s = verifica_peca_sorteio(
            pecas_disponiveis, pecas_pesos, quant_pecas_sorteadas)
        dicionario_probabilidades = s

        total_soma = sum(dicionario_probabilidades.values())

        # Normaliza os valores para que a soma seja 100%
        for chave, elem in dicionario_probabilidades.items():
            dicionario_probabilidades[chave] = round(100 * elem/total_soma, 2)

    # Ordena o dicionário deacordo com os maiores valores
    dicionario_probabilidades = dict(sorted(
        dicionario_probabilidades.items(), key=lambda item: item[1], reverse=True))

    # Transforma os valores em strings para adicionar o símbolo de porcentagem
    for chave, valor in dicionario_probabilidades.items():
        dicionario_probabilidades[chave] = f"{valor}%"

    return dicionario_probabilidades
