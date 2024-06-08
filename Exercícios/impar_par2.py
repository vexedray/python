# Número pares in repetição
soma = 0

for a in range (1,100):
    par = a % 2
    if par == 0:
        soma = soma + a
        
print(soma)