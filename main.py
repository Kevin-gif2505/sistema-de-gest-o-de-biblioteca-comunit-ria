import os

# Variáveis Globais
opcao = 0
Usuários = []
Livros = []
Empréstimos = []

def clear_screen():
   os.system('cls' if os.name == 'nt' else 'clear')

def show_menu(menu):
   if(menu == 'principal'):
      print('1. Clientes')
      print('2. Produtos')
      print('3. Vendas')
      print('0. Sair')

while True:
   clear_screen()
   print('Controle de Estoque')
   show_menu('principal')

   opcao = int(input('Digite a opção desejada: '))

   if(opcao == 1):
      print('Usuarios')
      print('1. Novo Usuário')
      print('2. Listar Usuários')
      print('3. Voltar')
   elif(opcao == 2):
      print('Produtos')
   elif(opcao == 3):
      print('Vendas')
   elif(opcao == 0):
      break
   else:
      print('Opção Invalida...')
