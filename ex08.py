from ex08funcoes import *

opcao = 0

while opcao != 3:
    opcao = obteropcao()

    if opcao == 1:
        tratarcombinacoes()
    elif opcao == 2:
        tratararranjos()
    elif opcao != 3:
        print(f'Opção inválida!')