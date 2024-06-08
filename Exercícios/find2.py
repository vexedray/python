# FUNÇÃO QUE VERIFICA ONDE ESTÁ OS "A" DA STRING

# VÁRIAVEIS

frase = str (input("Digite uma frase: "))
ases = 0

# OPERADORES

for a in frase:
    if a == "a":
        ases += 1

last = frase.rfind("a")
first = frase.find("a")

# RESULTADO

print("Primeiro a {} posição".format(first))
print("Ultimo a {} posição".format(last))
print("Teve {} as".format(ases))

