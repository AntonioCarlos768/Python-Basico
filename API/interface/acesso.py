import requests
from PySimpleGUI import PySimpleGUI as sg

sg.theme('BluePurple')

layout=[

[sg.Text("Qual id?:"), sg.Input(key='parametro')],
[sg.Button('ACESSAR')],
[sg.Text("-------------", size =(90, 50), key='exibir')]


]

janela = sg.Window("Tela API", layout,resizable=True)

while True:

      eventos, valores = janela.read()

      if eventos == sg.WINDOW_CLOSED:

         break

      if eventos == 'ACESSAR':
        print('entra')
        cod = valores['parametro']
      
        #request= requests.get(" https://jsonplaceholder.typicode.com/comments?postId='{0}' ".format(cod))
        request= requests.get('https://jsonplaceholder.typicode.com/comments?postId={0}'.format(cod))
        print(request.content)
        janela['exibir'].update(request.content)   
        




