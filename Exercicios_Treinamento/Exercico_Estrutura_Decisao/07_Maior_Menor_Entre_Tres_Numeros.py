""" Faça um Programa que leia três números e mostre o maior e o menor deles. """

# Solicitando os três números para usuário
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))

# Inicializando variáveis para o maior e o menor número
maior = num1
menor = num1

# Determinando o maior número
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Determinando o menor número
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

# Exibindo na tela o resultado
print(f'O MAIOR número entre {num1}, {num2} e {num3} é {maior}')
print(f'O MENOR número entre {num1}, {num2} é {num3} é {menor}')
