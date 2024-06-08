lista1 = []
lista2 = []
lista3 = []

for a in range (0,3):
  lista1.append (int(input("Digite um numero: ")))

for b in range (0,3):
  lista2.append(int(input("Digite um numero: ")))

lista3.insert(0, (lista1[0]))
lista3.insert(1, (lista2[0]))
lista3.insert(2, (lista1[1]))
lista3.insert(3, (lista2[1]))
lista3.insert(4, (lista1[2]))
lista3.insert(5, (lista2[2]))

print(lista1)
print(lista2)
print(lista3)