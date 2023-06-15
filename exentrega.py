num1 = int(input('Digite um número:'))
num2 = int(input('Digite um número:'))

i = num1 + num2

while i != 0:
    if num1 % i == 0 and num2 % i == 0:
        mdc = i
        break
    else:
        i -= 1
print(f'O maior divisor comum entre {num1:.0f} e {num2:.0f} é {mdc:.0f}')