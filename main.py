import os


# Variáveis Globais com novos valores e quantidades aleatórias
Usuários = [{"username": "kevin", "nome": "Kevin"}, {"username": "diego", "nome": "Diego"}, {"username": "cristney", "nome": "Cristney"}, {"username": "robert", "nome": "Robert"}, {"username": "carlos", "nome": "Carlos"}, {"username": "miguel r", "nome": "Miguel R"}]
Livros = [
   {"codigo": "1", "nome": "Da Terra á Lua", "qtd": 14}, 
   {"codigo": "2", "nome": "Pequeno Principe", "qtd": 22}, 
   {"codigo": "3", "nome": "Os Tres Porquinhos", "qtd": 19},
   {"codigo": "4", "nome": "Harry Potter e a Pedra Filosofal", "qtd": 14},
   {"codigo": "5", "nome": "O Senhor dos Aneis", "qtd": 26}
]
Empréstimos = []


while True:
   os.system('cls' if os.name == 'nt' else 'clear')
   print('=== CONTROLE DE ESTOQUE ===')
   print('1. Usuários | 2. Produtos | 3. Empréstimos | 0. Sair')
   opcao = input('Digite a opção desejada: ')


   if opcao == "0": 
      print("Saindo do sistema... Até mais!")
      break


   # MENU 1: USUÁRIOS
   elif opcao == "1":
      print('\n=== MENU: USUÁRIOS ===')  # <- ADICIONADO AQUI
      print('1. Novo Usuário | 2. Listar | 3. Excluir')
      acao = input('Escolha a ação: ')
      if acao == "1":
            user = input("Username único: ")
            existe = False
            for u in Usuários:
               if u['username'] == user: existe = True
            
            if existe:
               print("Erro: Username já existe!")
            else: 
               Usuários.append({"username": user, "nome": input("Nome: ")})
               print("Cadastrado!")
      elif acao == "2":
            for u in Usuários: print(f" Username: {u['username']} | Nome: {u['nome']}")
      elif acao == "3":
            user = input("Username para remover: ")
            Usuários = [u for u in Usuários if u['username'] != user]

   # MENU 2: PRODUTOS
   elif opcao == "2":
      print('\n=== MENU: PRODUTOS ===')  # <- ADICIONADO AQUI
      print('1. Novo Produto | 2. Listar | 3. Excluir')
      acao = input('Escolha a ação: ')
      if acao == "1":
            cod = input("Código único: ")
            existe = False
            for l in Livros:
               if l['codigo'] == cod: existe = True
               
            if existe: 
               print("Erro: Código já existe!")
            else: 
               Livros.append({"codigo": cod, "nome": input("Nome do Livro: "), "qtd": int(input("Qtd: "))})
               print("Livro Cadastrado!")
      elif acao == "2":
            for l in Livros: print(f" Código: {l['codigo']} | Livro: {l['nome']} | Estoque: {l['qtd']}")
      elif acao == "3":
            cod = input("Código para remover: ")
            Livros = [l for l in Livros if l['codigo'] != cod]

   # MENU 3: VENDAS (EMPRÉSTIMOS)
   elif opcao == "3":
      print('\n=== MENU: VENDAS (EMPRÉSTIMOS) ===')  # <- ADICIONADO AQUI
      print('1. Novo Empréstimo | 2. Listar | 3. Excluir')
      acao = input('Escolha a ação: ')
      if acao == "1":
            user = input("Username: ")
            cod = input("Código do Livro: ")
            
            livro_encontrado = None
            for l in Livros:
               if l['codigo'] == cod:
                  livro_encontrado = l
            
            if livro_encontrado and livro_encontrado['qtd'] > 0:
               livro_encontrado['qtd'] -= 1  
               Empréstimos.append({"user": user, "codigo": cod})
               print("Empréstimo feito!")
            else: 
               print("Erro: Sem estoque! Não permitido estoque negativo.")
      elif acao == "2":
            for e in Empréstimos: print(f" Usuário: {e['user']} | Livro Código: {e['codigo']}")
      elif acao == "3":
            cod = input("Código do livro para devolver: ")
            for l in Livros:
               if l['codigo'] == cod: l['qtd'] += 1  
            Empréstimos = [e for e in Empréstimos if e['codigo'] != cod]

   else: 
      print('Opção Inválida...')
      
   input('\nPressione Enter para continuar...')
