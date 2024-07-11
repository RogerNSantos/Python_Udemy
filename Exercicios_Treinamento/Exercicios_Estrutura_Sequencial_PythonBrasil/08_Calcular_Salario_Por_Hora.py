""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês """

# Solicitando o valor do trabalho e horas trabalhadas para o usuário
print('\n*-* CALCULO SALARIAL *-*')
print()

mes = str(input('Mês atual: '))
horaTrabalhada = float(input('Informe o valor da hora trabalhada R$ '))
horasPorDia = int(input('Informe as horas trabalhadas no mês: '))

salarioMes = horaTrabalhada * horasPorDia

print(f'Seu salário no mês de {mes} é: R$ {salarioMes}')



