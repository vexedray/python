# DESAFIO DADO

# BIBLIOTECAS
import random

# VÁRIAVEIS
n = []
resultado = []

jogador = {"Nome": [], "Dado": [], "Ganhador": ""}

for a in range(0, 4):
    n.append(input("Insira seu nome: "))
    resultado.append(random.randint(1, 6))

    jogador["Nome"].append(n[a])
    jogador["Dado"].append(resultado[a])

if resultado[0]>resultado[1]:
    jogador["Ganhador"] = resultado[0]
if resultado[1]>resultado[0] and resultado [1]>resultado[2]:
    jogador["Ganhador"] =resultado[1]
if resultado[2]>resultado[1] and resultado[2]> resultado[3]:
    jogador["Ganhador"] =resultado[2]
if resultado[3]>resultado[2]:
    jogador["Ganhador"] = resultado[3]

print("Nome:", jogador['Nome'][0], "\nDado:", jogador['Dado'][0])
print("Nome:", jogador['Nome'][1], "\nDado:", jogador['Dado'][1])
print("Nome:", jogador['Nome'][2], "\nDado:", jogador['Dado'][2])
print("Nome:", jogador['Nome'][3], "\nDado:", jogador['Dado'][3])
print("Ganhador:", jogador['Ganhador'],)