# Escolha do produto com o menor preço

preco_produto1 = float(input('Informe o preço do produto 1: '))
preco_produto2 = float(input('Informe o preço do produto 2: '))
preco_produto3 = float(input('Informe o preço do produto 3: '))

menor_preco = min(preco_produto1, preco_produto2, preco_produto3)

print('Compre o produto com o preço: {}'.format(menor_preco))

