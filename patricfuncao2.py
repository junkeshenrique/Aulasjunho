def soma(x: int, y: int):
    if x > y:
        print(f'O maior valor é {x:.0f}!')
    elif y > x:
        print(f'O maior valor é {y:.0f}!')
    else:
        print(f'Os números são iguais!')

x = int(input('Informe o valor de x:'))
y = int(input('Informe o valor de y:'))

soma(x, y)