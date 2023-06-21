
def obter_valor_por_categoria(categoria):
    if categoria == 1:
        return 15.00
    elif categoria == 2:
        return 20.00
    elif categoria == 3:
        return 30.00
def obter_fator_tamanho(tamanho):
    if tamanho == 'm':
        return 1.00
    elif tamanho == 'g':
        return 1.20
    elif tamanho == 'gg':
        return 1.40
def calcular_valor_pizza(categoria_sabor1, categoria_sabor2, categoria_sabor3, tamanho_pizza):

    valor_sabor1 = obter_valor_por_categoria(categoria_sabor1)
    valor_sabor2 = obter_valor_por_categoria(categoria_sabor2)
    valor_sabor3 = obter_valor_por_categoria(categoria_sabor3)

    valor_pizza = (valor_sabor1 + valor_sabor2 + valor_sabor3) * obter_fator_tamanho(tamanho_pizza)

    return valor_pizza