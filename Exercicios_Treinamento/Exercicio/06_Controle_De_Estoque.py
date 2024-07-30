"""Escreva um programa que leia o número de chuteiras de uma loja de esporte. Os valores
deverão ser inseridos por meio do teclado. Como saída, o programa deve apresentar o
número de chuteiras e suas marcas"""

print('\n*-*-*- CONTROLE DE ESTOQUE *-*-*')

"""# Solicitando os dados para o usuário
nike = int(input('\nInforme a quantidade de chuteira da Nike: '))
adidas = int(input('\nInforme a quantidade da chuteira Adidas: '))
olimpicos = int(input('\nInforme a quantidade de chuteira Olimpicos: '))

# Exibindo as quantidades de chuteiras
print(f'Nike {nike}')
print(f'Adidas {adidas}')
print(f'Plimpicos {olimpicos}')

totalchuteiras = nike + adidas + olimpicos
print(f'A quantidade de chuteiras no estoque é {totalchuteiras}')
"""

# Lista de marcas de chuteiras
marcasChuteira = ['Nike', 'Adidas', 'Olympikus']
quantidadesChuteira = []  # Lista para armazenar as quantidades de chuteiras

# Solicitar a quantidade de chuteiras para cada marca
for marca in marcasChuteira:
    quantidade = int(input(f"Informe a quantidade de chuteiras da marca {marca}: "))
    quantidadesChuteira.append(quantidade)

# Exibir as quantidades de chuteiras para cada marca
for i in range(len(marcasChuteira)):
    print(f"\nExistem {quantidadesChuteira[i]} chuteiras da marca {marcasChuteira[i]}.")

# Exibir o total de chuteiras
totalChuteiras = sum(quantidadesChuteira)
print(f"\nTotal de chuteiras no estoque: {totalChuteiras}")
