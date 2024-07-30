""" Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
comprar, sabendo que a decisão é sempre pelo mais barato. """

# Solicitando as informações para usuário
produto01 = float(input('Informe o preço do Desktop R$ '))
produto02 = float(input('Informe o preço do notebook R$ '))
produto03 = float(input('Informe o preço do celular R$ '))

# determinando qual produto é menor
if produto01 < produto02 and produto01 < produto03:
    produtoMaisBarato = 'Desktop'
    menor = produto01

elif produto02 < produto01 and produto02 < produto03:
    produtoMaisBarato = 'Notebook'
    menor = produto02

else:
    produtoMaisBarato = 'Celular'
    menor = produto03

print(f'O produto mais barato é o {produtoMaisBarato} com o preço R$ {menor:.2f}')
