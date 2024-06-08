# Notas

lista_notas = []

for nota in range (0,4):
    lista_notas.append(int(input("Digite a nota {}: ".format(nota+1))))

soma = sum(lista_notas)
divisao = soma / 4
print(divisao)
print(lista_notas)