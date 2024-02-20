# Ideia Principal 👨‍💻

Calculador de probabilidade para peças de dominó utilizando o método de Monte Carlo.


# Processo de Adivinhação 🔮

1. Construção do Dicionário de Peças:
Durante as rodadas do jogo, os jogadores registram as peças jogadas pelos outros participantes, juntamente com o número que cada jogador deixa disponível para o próximo. A cada jogada, incrementa-se um dicionário que registra as chances de cada jogador possuir uma peça correspondente ao número deixado disponível.

2. Sorteio com Método Monte Carlo:
Utilizamos o método Monte Carlo para realizar o sorteio, levando em conta o dicionário de cada jogador com as respectivas chances de possuir uma peça correspondente ao número disponível. Isso permite um sorteio mais preciso, considerando a probabilidade de um jogador ter uma peça jogável com o número anteriormente deixado disponível.

3. Cálculo de Porcentagens:
Ao dividir a quantidade de vezes que uma peça aparece pelo total de repetições na simulação e transformar esse resultado em porcentagem, obtemos uma lista que oferece uma visão clara da probabilidade de cada peça ser sorteada.

Esta abordagem proporciona uma maneira eficaz de estimar as chances de cada jogador ter uma determinada peça, proporcionando maiores margens de vitória para o utilizador do algorítmo.

# Modo de Utilização 🚀

## Requisitos:
Python 3.x
Biblioteca random do Python

## Instruções de Uso:

1. Clone o repositório.

```bash
git clone https://github.com/luizefz/dominou.git
```

2. Navegue até o diretório do projeto:

```bash
cd dominou
```

3. Execute o script Python para iniciar o sorteio:

```bash
python domino_hack.py 
```

# Como jogar? 🎮

Ao iniciar a execução do algoritmo, insira as peças que você possui em mãos digitando `0 0 0`. Como no exemplo:

![exemplo-minhas-peças-input](https://github.com/Luizefz/dominou/assets/67990430/c1ece647-0f51-4d90-b2cf-136911bee7e1)

Em seguida, insira as peças jogadas pelos outros jogadores a cada rodada do jogo informando 

1. **quem jogou**,
2. **peça jogada**
3. **número dispinível para outros jogadores**.
   
Assim como o exemplo abaixo:

![exemplo-utilizar-plataforma](https://github.com/Luizefz/dominou/assets/67990430/dde0bffa-d1fb-425e-b838-67c628761380)


# Nota sobre o Projeto 
Este projeto foi desenvolvido como parte da disciplina de Matemática Discreta 2, como parte dos requisitos de avaliação.

Alunos:
Luiz Eduardo - Github.com/luizefz
Luis Filipe - Github.com/LuisFilipeOliveiraSantos