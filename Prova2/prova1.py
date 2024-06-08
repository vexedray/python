# Par e Ímpar

# Variáveis

par = 0
impar = 0

# Operadores

for a in range (1,9):
    numero = int (input ("Digite um número: "))
    if numero % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print ("A quantidade de números pares é igual á {} ".format(par))
print ("A quantidade de números ímpares é igual á {} ".format(impar))