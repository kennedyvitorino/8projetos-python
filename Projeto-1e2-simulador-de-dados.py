# Simulador de dado
# Simular o uso de um ado, gerando um valor de 1 até 6
from random import randint
import PySimpleGUI as sg


class SimuladorDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esses valores
        try:
            if self.eventos == 'Sim':
                self.GerarValorDoDado()
            elif self.eventos == 'Não':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar Sim ou Não!')
        except (Exception,):
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDado()
simulador.iniciar()
