""" Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 """

# Solicitando a altura para usuário
altura = float(input('Digite sua altura: '))

# Solicitando a opção sexual para usuário
opcao = str(input('Sexo M ou F? ')).upper()

# Calculando o peso ideal com base no sexo
if opcao == 'M':
    peso = ((72.7 * altura) - 58)
    print(f'Para o sexo {opcao}, com altura de {altura:.2f} o pessoa ideal é {peso:.2f} KG')

elif opcao == 'F':
    peso = ((62.1 * altura) - 44.7)
    print(f'Para o sexo {opcao}, com altura de {altura:.2f} o pessoa ideal é {peso:.2f} KG')

else:
    print('Opção invalida, digite "M" para MASCULINO ou "F" para FEMININO ')

