# SOMA, MÉDIA, MAIOR E MENOR 

# FUNÇÕES


def soma (*numeros):
    c1 = 0
    for a in numeros:
        c1 = c1 + a
    print(c1)
soma(2,2)
soma(3,4,5,6)

def media (*numeros):
    c2 = 0
    for b in numeros:
        tamanho = len(numeros)
        c2 = c2 + b
        media = c2 / tamanho
    print(media)
media(5,6,7)

def maior_menor(*numeros):
    print("O maior é: ", max(numeros))
    print("O menor é: ", min(numeros))

maior_menor(5,8,1)