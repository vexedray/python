# VERIFICA SE O ANO É BISSEXTO

# VÁRIAVEIS

ano = int(input('Informe o ano: '))

# OPERADORES

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto')
else: 
    print('Não é bissexto')
 