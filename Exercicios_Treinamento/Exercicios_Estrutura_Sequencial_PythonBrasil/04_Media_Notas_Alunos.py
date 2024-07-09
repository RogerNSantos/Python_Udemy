# Faça um programa que peça as quatros notas bimestrais e mostre a MÉDIA

print('*-*' *15)
print('\t\tCALCULANDO A MÉDIA BIMESTRAL')
print('*-*' *15)
print()

"""# Solicitandpo as quatro notas para usuário
nota01 = float(input('Informe a Primeira nota: '))
nota02 = float(input('Informe a Segunda nota: '))
nota03 = float(input('Informe a Terceira nota: '))
nota04 = float(input('Informe a Quarta nota: '))

# Calculando a soma
soma = nota01 + nota02 + nota03 + nota04

# Calculando a média
media = soma / 4

# Inprimindo as notas e a média
print(f'As notas foram {nota01} + {nota02} + {nota03} + {nota04} = {soma}, a média foi {media}')"""

soma = 0

for i in range(1, 5):
    notas = float(input(f'Digite as quatros notas do aluno {i}: '))
    soma += notas

# Calculando a média das notas
media = soma / 4

# Imprmindo a média
print(f'A Média das notas é {media}')
