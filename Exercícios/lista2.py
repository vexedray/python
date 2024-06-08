# Ímpar Par

lista = []
par = []
impar = []

for a in range (0,3):
    lista.append(int(input("Digite o número {}: ".format(a+1))))
    if lista [a] % 2 == 0:
        par.append(lista[a])
    else:
        impar.append(lista[a])
        
print ("Os pares são: ", par)
print ("Os ímpares são: ", impar)
print("Os números da lista são: ", lista)
