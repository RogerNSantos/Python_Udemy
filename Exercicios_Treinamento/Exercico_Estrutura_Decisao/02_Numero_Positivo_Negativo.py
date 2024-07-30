""" Faça um programa que peça um valor e mostre na tela se o valor é positivo
 ou negativo """

# Solicitando o número para usuário
num = int(input('Informe um número para saber se é POSITIVO ou NEGATIVO: '))

if num > 0:
    print(f'Número {num} POSITIVO!')

elif num < 0:
    print(f'Número {num} NEGATIVO!')

else:
    print(f'O número é {num}')