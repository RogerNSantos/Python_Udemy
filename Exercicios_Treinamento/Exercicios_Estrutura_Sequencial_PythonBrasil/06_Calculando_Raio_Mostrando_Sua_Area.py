""" Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. """

print('-*' *13)
print('USANDO A BIBLIOTECA MATH')
print('*-' *13)

import math

# Solicitando o raio do circulo ao usuário
raio = float(input('Informe o raio do círculo: '))

# Caulculando a area do círculo
area = math.pi * (raio ** 2)

# Exibe a area do círculo
print(f'A area do circulo com raio {raio} é: {area:.2f}')
print('=-' *23)
print()

print('SEM USAR A BOBLIOTECA MATH')
print('-*-' *15)

# Valor aproximado de PI
pi = 3.14159

#Solicitando o raio do círculo aoa usuário
raio = float(input('Informe o raio do círculo: '))

# Calculando a area do círculo
area = pi * (raio **2)

# Exibindo a area do círculo
print(f'A area do círculo com raio {raio} é: {area:.2f}')