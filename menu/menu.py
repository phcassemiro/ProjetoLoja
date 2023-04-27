from database import comandos_db as cdb


class menu:

    def __init__(self):
        while True:
            print()
            print("Escolha uma opção:")
            print("-=-" * 10)
            print("""
            1 - Cadastrar produto
            2 - Cadastrar fornecedor
            3 - Excluir produto
            4 - Excluir fornecedor
            5 - Listar produto(s)
            6 - Listar fornecedor(s) 
            7 - Sair
            """)
            print("-=-" * 10)
            opcao = int(input("Digite o número da opção desejada: "))

            if opcao == 1:
                print("*" * 20)
                print('\033[1:32mCadastrar produto\033[m')
                print()
                id = int(input("Digite o id do produto: "))
                nome = str(input("Digite o nome do produto: "))
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                cdb.cadastrar_produto(id, nome, preco, quantidade)

            elif opcao == 2:
                print("*" * 20)
                print('\033[1:31mCadastrar fornecedor\033[m')
                print()
                id = int(input("Digite o id do fornecedor: "))
                nome = str(input("Digite o nome do fornecedor: "))
                cep = str(input("Digite o CEP do fornecedor: "))
                cdb.cadastrar_fornecedor(id, nome, cep)

            elif opcao == 3:
                print("*" * 20)
                print('\033[1:31mExcluir produto\033[m')
                print()
                id = int(input("Digite o id do produto: "))
                cdb.remover_produto(id)

            elif opcao == 4:
                print("*" * 20)
                print('\033[1:31mExcluir fornecedor\033[m')
                print()
                id = int(input("Digite o id do fornecedor: "))
                cdb.remover_fornecedor(id)

            elif opcao == 5:
                print("*" * 20)
                print('\033[1:31mLista produto(s)\033[m')
                print()
                cdb.listar_produto()

            elif opcao == 6:
                print("*" * 20)
                print('\033[1:31mLista fornecedor(es)\033[m')
                print()
                cdb.listar_fornecedor()
            elif opcao == 7:
                print("Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
