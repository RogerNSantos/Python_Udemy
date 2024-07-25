""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no
 mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$ """

print('=*' *20)
print('\t\tFOLHA DE PAGAMENTO')
print('=*' *20)
print()

# Criando variáveis
descontoImpostoRenda = 0.11
descontoINSS = 0.08
descontoSindicato = 0.05

# Solicitando as informações para usuário, quando ganha por hora e dias trabahados
ganhoHora = float(input('Quanto você ganha por hora? R$ '))
horasTrabalhadas = int(input('Informe total de horas trabalhadas no mês: '))

# Calculando salario BRUTO
salarioBruto = ganhoHora * horasTrabalhadas

# Calculando a porcentagem dos descontos
porcentagemIR = salarioBruto * descontoImpostoRenda
porcentagemINSS = salarioBruto * descontoINSS
porcentagemSindicato = salarioBruto * descontoSindicato

# Calculando o salário Liquido
salarioLiquido = salarioBruto - porcentagemIR - porcentagemINSS - porcentagemSindicato

print()

print(f'Salário bruto = R$ {salarioBruto:.2f}')
print(f'- IR (11%) = R$ {porcentagemIR:.2f}')
print(f'- INSS (8%) = R$ {porcentagemINSS:.2f}')
print(f'- SINDICATO (5%) = R$ {porcentagemSindicato:.2f}')
print(f'Salário Liquido = R$ {salarioLiquido:.2f}')

