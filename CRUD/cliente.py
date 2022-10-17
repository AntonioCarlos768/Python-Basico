from tkinter.tix import InputOnly
from PySimpleGUI import PySimpleGUI as sg
import mysql.connector
from tkinter.messagebox import showinfo
from tkinter import simpledialog

sg.theme('BluePurple')
#Tela
layout = [
       
      [sg.Text('Nome:'),sg.Input(key= 'nomes')],
      [sg.Text('Idade:'), sg.Input(key= 'idade')],
      [sg.Text('Cidade:'), sg.Input(key= 'cidade')],
      [sg.Button('confirma')],
      [sg.Text('----------', key='campoNome')],
      [sg.Text('OPÇÕES')], [sg.Button('Ver_Todos')],  [sg.Button('Excluir')], [sg.Button('Alterar')],
      [ sg.Cancel('FINALIZAR')]
 
       ]

# Janela
janela = sg.Window('tela', layout, resizable=True) 

#Atributos Banco de dados
conexao = mysql.connector.connect (

    host = 'localhost',
    user = 'root',
    database = 'empresa',
    password = 'antonio123!'

)

cursor = conexao.cursor()

# Verifica se a conexão foi efetuada
if conexao.is_connected:
    verifica = conexao.get_server_info()
    print('Conexão Realizada com Sucesso')

else:
   print('Conexão Falhou')


while True:

      eventos, valores = janela.read()

      if eventos == sg.WINDOW_CLOSED:

         break


      # quando o botão confirma é acionado
      if eventos == 'confirma':
            #verifica se o campo nome não é vazio
            if valores['nomes'] != '':
                 
                  janela['campoNome'].update(valores['nomes'])
                  n = valores['nomes']
                  i = valores['idade']
                  c = valores['cidade']
                
                  query = "INSERT INTO cliente(nome,idade,cidade) VALUES ('{0}','{1}','{2}')".format(n,i,c)                 
                  cursor.execute(query)
                  
      if eventos == 'Ver_Todos':
         #Seleciona todos os clientes
         cursor.execute("SELECT*FROM cliente")
         tabela = cursor.fetchall()
          #Percorre todos os Campos
         for x in tabela:
            print(x)
           # janela['table'].update(x)
      if eventos == 'Excluir':
        #showinfo(title="msg" , message= "QUEM DESEJA EXCLUIR?(Nem Pega)" )
        nome_exclusao = simpledialog.askstring(title="exclusão", prompt="Quem Deseja Excluir?:")
        print("zzZZ:"+nome_exclusao)
        sql_delete =" DELETE FROM cliente WHERE nome = '{0}'".format(nome_exclusao)
        cursor.execute(sql_delete) 

      if eventos == 'Alterar':
         nome_alterar = simpledialog.askstring(title="alteracao", prompt="Quem Deseja Alterar?:")
         print("Nome de Where:"+nome_alterar)
         novo_nome =simpledialog.askstring(title="novo", prompt="Qual nome Deseja Colocar?:")
         print("Nome de Update(novo)"+novo_nome)
         #sql_altera =" UPDATE cliente SET nome ='{0}'".format(novo_nome), " WHERE nome = '{0}' ".format(nome_alterar)
         sql_altera =" UPDATE cliente SET nome ='{0}' WHERE nome = '{1}' ".format(novo_nome,nome_alterar)
         cursor.execute(sql_altera) 

      if eventos =='FINALIZAR':
         # Salva
         conexao.commit()
         # Encerra
         cursor.close()

         conexao.close()