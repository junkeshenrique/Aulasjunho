# Informar números até a somar ser maior que 100

soma = 0

while soma < 100:
    num = int(input('Informe um número:'))
    soma += num
    print(f'A soma está em {soma}.')

print(f'A soma é {soma}')