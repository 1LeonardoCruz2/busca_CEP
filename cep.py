import requests
import json
import PySimpleGUI as sg

class TelaPython:

    def __init__(self):
        layout = (
            [sg.Text('CEP'), sg.Input(size=(25, 0), key='CEP')],
            [sg.Button('Buscar')],
            [sg.Output(size=(35, 10))]
        )
        self.tela = sg.Window('Busca de CEP', layout)

    def busca_cep(self, cep):
        url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if url.status_code == 200:
            print('Encontrado')
        elif url.status_code == 400:
            print(f"O CEP {cep} não foi encontrado")
        endereco = url.json()
        return endereco

    def janela(self):
        while True:
            self.button, self.values = self.tela.Read()
            try:
                valores = self.busca_cep(self.values['CEP'])
                for k, v in valores.items():
                    print(k.upper(), ':', v)
            except:
                print('Erro')
            print('--------------------------')

janela = TelaPython()
janela.janela()