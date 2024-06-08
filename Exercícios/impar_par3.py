# Soma ímpar
soma = 0 
for a in range (1,7):
    numero = int (input("Digite um número: "))
    impar = numero % 3
    if impar == 0:
        soma = soma + numero
print(soma)