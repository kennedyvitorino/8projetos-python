# Projeto 7 e 8 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar vários finais diferentes
# baseado nas respostas que foram dadas

# Eu quero chegar a finais diferentes na minha história,
# de acordo com as resposta que eu passo para o programa

# Qual é o cenário: Eu estou numa guerra entre duas nações, e nós temos 2 lados: Lado A e Lado B
# Somente o lado A irá vencer, e o lado B irá perder! Então tenho que tomar as decisões corretas
# para chegar até a vitória, que somenta o lao A irá conseguir
import PySimpleGUI as sg


class JogoAventura:
    valores: object
    evento: object

    def __init__(self):
        self.janela = None
        self.pergunta1 = 'Você nasceu no Norte ou Sul \n[N/S] ?'  # Norte = Lado A, Sul = Lado B
        self.pergunta2 = 'Você prefere a espada ou escudo \n[Espada/Escudo] ?'  # Espada = Lado A, escudo = Lado B
        self.pergunta3 = 'Qual é a sua especialidade \n[linha de frente/tático] ?'  # Linha de frente = Lado A, tático = Lado B
        self.historia_final1 = 'Você será um HEROI na linha de frente!'
        self.historia_final2 = 'Você será um HEROI protegendo \ntodas as nossas tropas!'
        self.historia_final3 = 'Você irá se sacrificar na BATALHA!'
        self.historia_final4 = 'Você não é capaz de lutar nessa BATALHA!'

    def iniciar(self=None):
        # Layout
        layout = [
            [sg.Output(size=(40, 20), key='respostas')],
            [sg.Input(size=(40, 15), key='escolha')],
            [sg.Button('Iniciar'), sg.Button('Responder')],
        ]

        # Criar a janela
        self.janela = sg.Window('⚔️ Jogo de Aventura ⚔️', layout=layout)

        while True:
            # Ler os dados
            self.ler_valores()
            # Fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.ler_valores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.ler_valores()
                    if self.valores['escolha'] == 'espada':
                        print(self.historia_final1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.historia_final2)
                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.ler_valores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.historia_final3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.historia_final4)

    def ler_valores(self):
        self.evento, self.valores = self.janela.Read()


jogo = JogoAventura()
jogo.iniciar()
