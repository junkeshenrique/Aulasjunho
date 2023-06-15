def obteropcao() -> int:
    print('** Menu de Opções **\n'
          '1 - Calcular combinação\n'
          '2 - Calcular Arranjo\n'
          '3 - Sair')
    opcao = int(input('Informe a opção desejada ==> '))

    if not opcaovalida(opcao):
        print('** Opção inválida, tente novamente! **')

    return opcao

def opcaovalida(opcao: int) -> bool:
    return opcao in (1, 2, 3)

def calcular_fatorial(num: int) -> int:
    if num == 1:
        return 1

    return num * calcular_fatorial(num -1)

def calcular_arranjos(n: int, p:int) -> float:
    return calcular_fatorial(n) / calcular_fatorial(n - p)

def calcular_combinacoes(n: int, p: int) -> float:
    return calcular_fatorial(n) / (calcular_fatorial(p) * calcular_fatorial(n - p))

def tratarcombinacoes():
    print(f'Opção escolhida ==> Calcular combinação!')
    n = int(input('Informe o número de elementos(n):'))
    p = int(input('Informe o tamanho dos agrupamentos(p):'))
    result = calcular_combinacoes(n, p)
    print(f'O total de combinações é {result:.2f}')
def tratararranjos():
    print(f'Opção escolhida ==> Calcular arranjo!')
    n = int(input('Informe o número de elementos(n):'))
    p = int(input('Informe o tamanho dos agrupamentos(p):'))
    result = calcular_arranjos(n, p)
    print(f'O total de arranjos é de {result:.2f}')