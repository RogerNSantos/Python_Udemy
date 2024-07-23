""" Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
 a temperatura em graus Celsius """

# Solicitando ao usuário a temperatura em FAHRENHEIT
fahrenheit = float(input('Digite a temperastura em Fahrenheit: '))

# Conversão de FAHRENHEIT para CELSIUS
celsius = ((fahrenheit - 32) * 5 / 9)

# Exibindo o resultado da conversão
print(f" A temperatura {fahrenheit}ºF convertida para CELSIUS é {celsius:.2f}ºC ")