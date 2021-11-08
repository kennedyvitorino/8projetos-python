# Projeto 3 - Chute o número
# Objetivo: Criar um algorítmo que gera um valor
# aleatório e eu tenho que ficar tentando o número até acertar.
# objetivo: Criar um algorítimo que gera um valor aleatório e eu tenho que ficar tentando o número até eu acertar
from random import randint
import PySimpleGUI as sg


class ChuteONumero:
    evento: object
    valores: object

    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 20
        self.tentar_novamente = True

    def iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu Chute', size=(39, 0))],
            [sg.Input(size=(18, 0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39, 10))]
        ]

        # criar uma janela
        self.janela = sg.Window('Chute o numero!', layout=layout)
        self.gerar_numero_aleatorio()
        try:
            while True:
                # receber os valores
                self.evento, self.valores = self.janela.Read()
                # Fazer alguma coisa com estes valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABÉNS VOCÊ ACERTOU!! \n'
                                  'Fim do programa')
                            break
        except:
            print('Favor digitar apenas números!')
            self.iniciar()

    def gerar_numero_aleatorio(self):
        self.valor_aleatorio = randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.iniciar()
