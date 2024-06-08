# FUNÇÃO QUE CRIA UMA LISTA DE NÚMEROS ALEATÓRIOS ENTRE 1 A 10

# BIBLIOTECA

import random

# OPERADORES

def a (t):
    n1 = [] 
    for a in range (0, t):
        n1.append(random.randint(1,10))
    return print(n1)

# CHAMADA DE FUNÇÃO

print(a(10))

