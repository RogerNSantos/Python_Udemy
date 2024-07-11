""" Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área
 para o usuário. """


# Solicitando as medias do quadrado ao usuário
base = float(input('Informa a base do quadrado: '))
altura = float(input('Informe a altura do quadrado: '))

# Calculando a area do quadrado
area = base * altura

# Calculando o dobro da area
dobroArea = area + area

# Exibindo os resultados
print(f'A area do quadra é {area} o seu dobro é {dobroArea:.2f}.')
print('-*' *24)
print()

# Solicitando o valor do lado do quadrado ao usuário
lado = float(input('Informe o valor do lado do quadrado: '))

# Calculando a area do quadrado
area = lado ** 2

# Calculando o bobro da area
dobra_Area = 2 * area

# Exibindo a area do quadrado e o dobro da área
print(f'A área do quadrado com o lado {lado} é {area:.2f}')
print(f'O dobro da área do quadrado é: {dobra_Area:.2f}')
