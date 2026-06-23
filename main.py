import os

# Variáveis Globais com novos valores e quantidades aleatórias
Usuários = [
    {"username": "kevin", "nome": "Kevin", "email": "Kevin@gmail.com"},
    {"username": "diego", "nome": "Diego", "email": "Diego@gmail.com"},
    {"username": "cristney", "nome": "Cristney", "email": "Cristiney@gmail.com"},
    {"username": "robert", "nome": "Robert", "email": "Robert@gmail.com"},
    {"username": "carlos", "nome": "Carlos", "email": "Carlos@gmail.com"},
    {"username": "miguel r", "nome": "Miguel R", "email": "MiguelR@gmail.com"}
]

Livros = [
    {"codigo": "1", "nome": "Da Terra á Lua", "qtd": 14}, 
    {"codigo": "2", "nome": "Pequeno Principe", "qtd": 22}, 
    {"codigo": "3", "nome": "Os Tres Porquinhos", "qtd": 19},
    {"codigo": "4", "nome": "Harry Potter e a Pedra Filosofal", "qtd": 14},
    {"codigo": "5", "nome": "O Senhor dos Aneis", "qtd": 26}
]

Empréstimos = []
numero_emprestimo = 1

def ClearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def ShowTitle():
    print("=" * 35)
    print("     CONTROLE DE ESTOQUE DE LIVROS")
    print("=" * 35)

def ShowMenu(menu):
    if menu == "Principal":
        print("1. Usuários")
        print("2. Produtos")
        print("3. Pedidos")
        print("0. Sair")  
    else:
        print("1. Novo")
        print("2. Listar")
        print("3. Excluir")
        print("4. Voltar")

# Sistema Principal
while True:
    ClearScreen()
    ShowTitle()
    ShowMenu("Principal")
    op = input("Opção: ")

    if op == "0":
        print("Até mais!")
        break

    # Menu de Usuários 
    elif op == "1":
        while True:
            ClearScreen()
            ShowTitle()
            print("Menu Usuários")
            ShowMenu("Secundário")
            acao = input("Opção: ")

            if acao == "4":
                break
            elif acao == "1":
                user = input("Username: ")
                if any(u["username"] == user for u in Usuários):
                    print("Username já existe. ")
                else:
                    Usuários.append({
                        "username": user,
                        "nome": input("Nome: "),
                        "email": input("Email: ")
                    })
                    print("Usuário Cadastrado.")
            elif acao == "2":
                print("\n--- LISTA DE USUÁRIOS ---")
                for u in Usuários:
                    print(f"{u['username']} | {u['nome']} | {u['email']}")
            elif acao == "3":
                user = input("Username para excluir: ")
                if any(emp["username"] == user for emp in Empréstimos):
                    print("O Usuário possui um empréstimo ativo e não pode ser removido.")
                else:
                    original_len = len(Usuários)
                    Usuários = [u for u in Usuários if u["username"] != user]
                    if len(Usuários) < original_len:
                        print("Usuário removido.")
                    else:
                        print("Usuário não encontrado.")
            input("\nEnter para continuar...")

    # Menu de Produtos (Livros)
    elif op == "2":
        while True:
            ClearScreen()
            ShowTitle()
            print("Menu Produtos (Livros)")
            ShowMenu("Secundário")
            acao = input("Opção: ")

            if acao == "4":
                break
            elif acao == "1":
                cod = input("Código do Livro: ")
                if any(l["codigo"] == cod for l in Livros):
                    print("Código já existe.")
                else:
                    try:
                        nome_livro = input("Nome do Livro: ")
                        qtd_livro = int(input("Quantidade: "))
                        Livros.append({
                            "codigo": cod,
                            "nome": nome_livro,
                            "qtd": qtd_livro
                        })
                        print("Livro cadastrado.")
                    except ValueError:
                        print("Quantidade inválida.")
            elif acao == "2":
                print("\n--- ESTOQUE DE LIVROS ---")
                for l in Livros:
                    print(f"Cód: {l['codigo']} | {l['nome']} | Qtd: {l['qtd']}")
            elif acao == "3":
                cod = input("Código do Livro para excluir: ")
                if any(emp["codigo"] == cod for emp in Empréstimos):
                    print("Livro possui empréstimo ativo. Não pode ser removido.")
                else:
                    original_len = len(Livros)
                    Livros = [l for l in Livros if l["codigo"] != cod]
                    if len(Livros) < original_len:
                        print("Livro removido.")
                    else:
                        print("Livro não encontrado.")
            input("\nEnter para continuar...")

    # Menu de Empréstimos
    elif op == "3":
        while True:
            ClearScreen()
            ShowTitle()
            print("Menu Pedidos (Empréstimos)")
            ShowMenu("Secundário")
            acao = input("Opção: ")

            if acao == "4":
                break
            elif acao == "1":
                user = input("Username: ")
                cod = input("Código do livro: ")
                try:
                    qtd = int(input("Quantidade para empréstimo: "))
                except ValueError:
                    print("Quantidade inválida.")
                    input("\nEnter para continuar...")
                    continue

                usuario = next((u for u in Usuários if u["username"] == user), None)
                livro = next((l for l in Livros if l["codigo"] == cod), None)

                if usuario is None:
                    print("Usuário não encontrado.")
                elif livro is None:
                    print("Livro não encontrado.")
                elif livro["qtd"] < qtd:
                    print(f"Estoque insuficiente. Disponível: {livro['qtd']}")
                else:
                    livro["qtd"] -= qtd
                    Empréstimos.append({
                        "numero": numero_emprestimo,
                        "username": user,
                        "codigo": cod,
                        "quantidade": qtd
                    })
                    print(f"Empréstimo {numero_emprestimo} registrado.")
                    numero_emprestimo += 1

            elif acao == "2":
                print("\n--- LISTA DE EMPRÉSTIMOS ---")
                if not Empréstimos:
                    print("Nenhum empréstimo registrado.")
                for emp in Empréstimos:
                    print(f"Empréstimo nº: {emp['numero']} | Usuário: {emp['username']} | Livro Cód: {emp['codigo']} | Qtd: {emp['quantidade']}")

            elif acao == "3":
                try:
                    num = int(input("Número do empréstimo para devolver/excluir: "))
                except ValueError:
                    print("Número inválido.")
                    input("\nEnter para continuar...")
                    continue

                emp_encontrado = next((x for x in Empréstimos if x["numero"] == num), None)
                if emp_encontrado:
                    # Devolve a quantidade ao estoque do livro
                    livro = next((l for l in Livros if l["codigo"] == emp_encontrado["codigo"]), None)
                    if livro:
                        livro["qtd"] += emp_encontrado["quantidade"]
                    
                    Empréstimos.remove(emp_encontrado)
                    print("Empréstimo encerrado e livro devolvido ao estoque.")
                else:
                    print("Empréstimo não encontrado.")
            input("\nEnter para continuar...")
