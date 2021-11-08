# Projeto 3 - Chute o número
# Objetivo: Criar um algorítmo que gera um valor
# aleatório e eu tenho que ficar tentando o número até acertar.
from random import randint
import PySimpleGUI as gs

class ChuteNumero:
    def __init__(self):
        self.valor_chute = input('Chute um número (999 para encerrar):')
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 20
        self.tente_novamente = True

    def iniciar(self):
        self.gerar_numero_aleatorio()
        self.pedir_valor_aleatorio()

        try:
            while self.valor_chute != '999':
                self.valor_chute = input('Chute um número (999 para encerrar):')
                if int(self.valor_chute) == self.valor_aleatorio:
                    print('Parabéns, você acertou!')
                    break
                elif int(self.valor_chute) < self.valor_aleatorio:
                    print('chute um valor mais alto!')
                    self.pedir_valor_aleatorio()
                elif int(self.valor_chute) > self.valor_aleatorio:
                    print('Chute um valor mais baixo!')
                    self.pedir_valor_aleatorio()
            print('Fim do programa!')

        except (Exception,):
            print('Por favor, digit apenas números:!')
            iniciar()

    def pedir_valor_aleatorio(self):
        pass

    def gerar_numero_aleatorio(self):
        self.valor_aleatorio = randint(self.valor_minimo, self.valor_maximo)


chute = ChuteNumero()
chute.iniciar()
