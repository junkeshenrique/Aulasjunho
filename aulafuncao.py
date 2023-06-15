def dizer_ola():
    print(f'Olá, mundo!')


def exibir_saudacoes(nome: str, periodo: int):
    if periodo == 1:
        print(f'Bom dia, {nome}!')
    elif periodo == 2:
        print(f'Boa tarde, {nome}!')
    else:
        print(f'Boa noite, {nome}!')

dizer_ola()
exibir_saudacoes('Henrique', 3)
exibir_saudacoes('Aparicio', 1)

def somar(x: float, y: float):
    soma = x + y
    print(f'A soma é {soma:.2f}!')

x = float(input('Informe o valor de x:'))
y = float(input('Informe o valor de y:'))

somar(x, y)