# Ideia principal 👨‍💻

A ideia agora é utilizar Monte Carlo com rd.choices para calcular a possibilidade de uma peça de dominó está na mão de um dos jogores. 

# Processo de advinhação 🔮

1. Ao longo das rodadas do jogo, com as peças jogadas, cada jogador vai construindo o seu próprio dicionário com as vezes que cada peça / número da peça foi jogado.

2. Quando for realizar o sorteio com o método monte carlo, ele usará o dicionário de cada jogador com seus respectivos pesos, visando sortear uma estimativa mais correta da quantidade de vezes que a peça pode aparecer na mão do jogador.

3. Contar quantas vezes uma peça apareceu, dividir essa quantidade pelo total de repetições feitas na simulação e, em seguida, utilizar esse resultado para transformá-lo em porcentagem e inseri-lo na lista de porcentagens
