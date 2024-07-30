""" Faça um programa que leia TRÊS números e mostre o maior deles. """

# Solicitando as informações para usuário
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))

# Determine o maior entre os três números
if num1 > num2 and num1 > num3:
    maior = num1

elif num2 > num1 and num2 > num3:
    maior = num2

else:
    maior = num3

print(f'O maior número entre {num1}, {num2} e {num3} é {maior}.')