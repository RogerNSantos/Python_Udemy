"""
Introdução ao empacotamento e desempacotamento
"""

# DESEMPACOTAMENTO

#nomes = ['Rogério', 'Maria', 'Helena']
#nomes1, nomes2, nomes3 = ['Rogério', 'Maria', 'Helena']

#nome1, *resto = ['Rogério', 'Maria', 'Helena']
#print(nome1, resto)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)