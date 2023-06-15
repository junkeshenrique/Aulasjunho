from ex05funcoes import *

escolherop = obteropcao()
print(escolherop)

if escolherop == 1:
    area = obteropcaoquadrado()
elif escolherop == 2:
    area = obteropcaocirculo()
else:
    area = obteropcaotriangulo()

print(f'A área é de {area:.2f} metros. ')