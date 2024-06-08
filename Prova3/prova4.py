# VERIFICAR NO DICIONARIO

# DICIONÁRIO

dic = {"hand" : "mão", "blue" : "azul", "book" : "livro", "pen" : "caneta"}

# VÁRIAVEIS

ler = input("Digite uma palavra: ")

# OPERADORES

for chave in dic.keys():
    if ler == chave:
        print("A tradução é: "+ dic.get(chave))
