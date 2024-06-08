# Maior e menor números

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print('O maior número é: {} '.format(maior))
print('O menor número é: {} '.format(menor))