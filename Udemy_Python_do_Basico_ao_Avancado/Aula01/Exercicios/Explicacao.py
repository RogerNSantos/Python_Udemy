""" Interando STRINGS com While """

#   01234678910

#  nome = 'Rogério Santos'

#   1110987654321

"""tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3] )"""


nome = 'Rogério Santos'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
    
novo_nome += '*'
print(novo_nome)

