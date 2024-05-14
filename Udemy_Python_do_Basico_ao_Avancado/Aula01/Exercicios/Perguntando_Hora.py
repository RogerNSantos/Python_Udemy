"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, 
exiba a saudação apropriada. Ex: 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = int(input('Informa as horas: '))
minuto = int(input('os minútos: '))

if horas >= 0 and horas <= 11:
    print(f'Bom dia, são {horas}:{minuto}.')
elif horas >= 12 and horas <= 17:
    print(f'Boa tarde, são {horas}:{minuto}.')
elif horas >= 18 and horas <= 23:
    print(f'Boa noite, são {horas}:{minuto}.')
else:
    print('Hora inválida!')

"""entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')"""