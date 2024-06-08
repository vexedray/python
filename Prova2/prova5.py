# Lanchonete

# Variaveis

quantidade = int (input("Digite a quantidade de itens da lanchonete: "))
dog = 12.80
hamburguer = 26.50
x = 21.10
refri = 3
conta = 0

# Operadores

if quantidade <= 4:
    for a in range (0,quantidade):

        codigo = int (input("Insira o codigo do seu lanche: "))
        vezes = int (input("A quantidade de itens: "))

        if codigo == 102:
            conta = conta + (dog * vezes)
        if codigo == 103:
            conta = conta + (hamburguer * vezes)
        if codigo == 104:
            conta = conta + (x * vezes)
        if codigo == 105:
            conta = conta + (refri * vezes)
print ("Sua conta ficou: ", conta)