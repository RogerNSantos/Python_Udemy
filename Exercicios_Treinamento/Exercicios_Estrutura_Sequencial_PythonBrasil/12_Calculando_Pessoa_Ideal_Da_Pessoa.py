""" Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 """

# Campo para usuário digitar sua ALTURA
altura = float(input('Digite sua altura: '))

# Formula para calcular peso ideal
peso = ((72.7 * altura) - 58)

# Exibindo na tela
print(f'O peso ideal de uma pessoal com {altura} altura é: {peso}')


