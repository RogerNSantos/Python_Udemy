""" Faça um Programa que peça a temperatura em graus Celsius, transforme e
 mostre em graus Fahrenheit.
 """

# Solicitando para usuária a temperatura em CELSIUS
celsius = float(input('Digite a temperatura em CELSIUS: '))

# Convertendo para FAHRENHEIT
fahrenheit = ((celsius * 5/9) + 32)

# Exibindo o resultado na tela 
print(f'A temperatura {celsius}ºC convertendo para FAHRENHEIT é {fahrenheit}ºF')