print('Calculando IMC corporal')

nome = str(input('Informe seu nome: '))
altura = float(input('Informe sua Altura: '))
peso = float(input('Informe seu peso: '))
#imc = peso / (altura * altura)
imc = peso / altura ** 2

print(f'{nome} você tem {altura:.2f} de altura, pesa {peso:.3f} KG, seu IMC corporal é {imc:.2f}')