# CRIAR UMA LISTA DE NÚMEROS ALEATÓRIOS 

# BIBLIOTECAS

from random import randint

# OPERADORES

def lista(tamanho):
    numeros = []
    for a in range (tamanho):
        numeros.append(randint(1,10))
    return numeros, max(numeros), min(numeros)

lst, maior, menor = lista(5)
print(lst)
print(maior)
print(menor)
