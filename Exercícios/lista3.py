# Soma e multiplicação

lista = []
multiplicacao = 1

for a in range (0,3):
    lista.append(int(input("Digite o número {}: ".format(a+1))))
    multiplicacao = multiplicacao * lista [a]

soma = sum (lista)

print(soma)
print(multiplicacao)