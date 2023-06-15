def valorabsoluto(num: int) -> int:
    if num < 0:
        return num * -1
    else:
        return num
    return valorabsoluto

num = int(input('Informe um número:'))

absoluto = valorabsoluto(num)
print(f'O valor absoluto de {num} é {absoluto}!')
valorabsoluto(num)
