def maior(x = int, y = int) -> int:
    return x if x > y else y

x = int(input('Informe o primeiro número:'))
y = int(input('Informe o segundo número:'))

omaior = maior(x, y)
print(f'O maior número é o {omaior:.0f}!')




