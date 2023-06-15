import random

sorteio = random.randint(0, 100)
acertou = False
for i in range(1, 11):
    num = int(input('Diga seu palpite: '))
    if num == sorteio:
        acertou = True
        print(f'Parabéns você acertou em {i} tentativas, o número sorteado é {sorteio:.0f}!')
        break
    else:
        print(f"Errado, tente novamente!")
    if num < sorteio:
        print(f'Ishh chutou muito baixo!')
    else:
        print(f'Ishh chutou muito alto!')

if acertou == False:
    print(f'Acabaram suas chances, o número sorteado foi {i}.')