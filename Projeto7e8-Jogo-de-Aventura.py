# Projeto 7 e 8 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar vários finais diferentes
# baseado nas respostas que foram dadas

# Eu quero chegar a finais diferentes na minha história,
# de acordo com as resposta que eu passo para o programa

# Qual é o cenário: Eu estou numa guerra entre duas nações, e nós temos 2 lados: Lado A e Lado B
# Somente o lado A irá vencer, e o lado B irá perder! Então tenho que tomar as decisões corretas
# para chegar até a vitória, que somenta o lao A irá conseguir

class JogoAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no Norte ou Sul [N/S] ?'  # Norte = Lado A, Sul = Lado B
        self.pergunta2 = 'Você prefe as espada ou escudo [Espada/Escudo] ?'  # Espada = Lado A, escudo = Lado B
        self.pergunta3 = 'Qual é a sua especialidade [linha de frente/tático] ?'  # Linha de frente = Lado A, tático = Lado B
        self.historia_final1 = 'Você será um HEROI na linha de frente!'
        self.historia_final2 = 'Você será um HEROI protegendo todas as nossas tropas!'
        self.historia_final3 = 'Você irá se sacrificar na BATALHA!'
        self.historia_final4 = 'Você não é capaz de lutar nessa BATALHA!'

    def iniciar(self=None):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'n':
            resposta_1B = input(self.pergunta2)
            if resposta_1B == 'espada':
                print(self.historia_final1)
            if resposta_1B == 'escudo':
                print(self.historia_final2)
        if resposta1 == 's':
            resposta_1B = input(self.pergunta3)
            if resposta_1B == 'linha de frente':
                print(self.historia_final3)
            if resposta_1B == 'tatico':
                print(self.historia_final4)


jogo = JogoAventura()
jogo.iniciar()
