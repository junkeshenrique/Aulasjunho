def calculavolume (raio: float) -> float:
    volume = 4 / 3 * raio ** 2
    return volume

raio = float (input('Informe o valor do raio:'))
volume = calculavolume(raio)
print(f'O volume total é de {volume:.2f}')