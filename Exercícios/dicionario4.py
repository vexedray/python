# CRIA UMA LISTA E MOSTRA O DOBRO

def dobro(lista):
    lista_dobro = []
    for numero in lista:
        lista_dobro.append(numero*2)
    return lista_dobro

tamanho = int(input("Insira tamanho da sua lista: "))
qtd = []

for a in range (tamanho): 
    n = int(input("Insira o número: "))
    qtd.append(n)

lst = dobro(qtd)
print("O dobro da sua lista é: ", lst)
