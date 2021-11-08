# projeto 5 - Decida por mim
# Faça uma pergunta para o programa e ele terá que retornar uma resposta.
from random import choice
import PySimpleGUI as sg


class DecidaPorMim:
    eventos: object
    valores: object

    def __init__(self):
        self.resposta = [
            'Com certeza você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso não!',
            'Acho que ta na hora certa'
        ]

    def iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(45, 10))],
            [sg.Button('Decida por mim')]
        ]
        # Criar a janela
        self.janela = sg.Window('Decida por mim', layout=layout)
        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(choice(self.resposta))


decida = DecidaPorMim()
decida.iniciar()
