from ex07funcoes import *

categoria_sabor1 = int(input("Digite a categoria do primeiro sabor (1 - Normal, 2 - Gourmet, 3 - Premium): "))
categoria_sabor2 = int(input("Digite a categoria do segundo sabor (1 - Normal, 2 - Gourmet, 3 - Premium): "))
categoria_sabor3 = int(input("Digite a categoria do terceiro sabor (1 - Normal, 2 - Gourmet, 3 - Premium): "))

tamanho_pizza = input("Digite o tamanho da pizza (m - Média, g - Grande, gg - Gigante): ")

valor_final = calcular_valor_pizza(categoria_sabor1, categoria_sabor2, categoria_sabor3, tamanho_pizza)

print(f"O valor final a ser pago pela pizza é: R$ {valor_final:.2f}")
