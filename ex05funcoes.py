def areaquadrado (lado: float) -> float:
    return lado ** 2

def areacirculo (raio: float) -> float:
    return 3.14 * raio ** 2

def areatriangulo (base: float, altura: float) -> float:
    return (base * altura) / 2

def obteropcao() -> int:
    opcao = 0
    while not opcaovalida(opcao):
        print('** Menu de Opções **\n'
              '1 - Área do Quadrado\n'
              '2 - Área do Círculo\n'
              '3 - Área do Triângulo')
        opcao = int(input('===> '))

        if not opcaovalida(opcao):
            print('** Opção inválida, tente novamente! **')
    return opcao

def opcaovalida(opcao: int) -> bool:
    return opcao in (1, 2, 3)

def obteropcaoquadrado() -> float:
    lado = float(input('Informe qual o tamanho do lado do quadrado: '))
    area = areaquadrado(lado)
    return area

def obteropcaocirculo() -> float:
    raio = float(input('Informe qual o tamanho do raio do círculo: '))
    area = areacirculo(raio)
    return area

def obteropcaotriangulo() -> float:
    base = float(input('Informe o tamanho da base do triângulo: '))
    altura = float(input('Informe a altura do triângulo: '))
    area = areatriangulo(base, altura)
    return area