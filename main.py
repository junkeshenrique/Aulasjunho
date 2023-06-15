import sys

maior = -sys.maxsize
menor = sys.maxsize

for i in range(10):
    num = int(input('Informe um número inteiro: '))

    if num > maior:
        maior = num

    if num < menor:
        menor = num

print(f'O maior número informado foi: {maior:.0f}')
print(f'O menor número informado foi: {menor:.0f}')