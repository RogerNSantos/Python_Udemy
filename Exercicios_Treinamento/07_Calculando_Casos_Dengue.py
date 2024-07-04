''' Escreva um programa em C para o Ministério da Saúde que o auxilie nas informações sobre
a dengue em Brasília. Esse programa deve receber os dados sobre o número de casos
suspeitos, o número de casos confirmados e o número de mortes '''

#import os
print('\n=-=-=- Ministéria da Saúde -=-=-=')
print('=- Dados Referente aos casos de dengue -= ')
casosSuspeitos = int(input('\nInforme os casos SUSPEITOS: '))
casosConfirmados = int(input('Informe os casos CONFIRMADOS: '))
casosObtos = int (input('Informe os caos de Óbtos: '))
total = casosSuspeitos + casosConfirmados + casosObtos

#os.system('cls')

print('=-=-=- Relatório Final -=-=-=')
print(f'{casosSuspeitos} -> casos SUSEITOS de dengue.')
print(f'{casosConfirmados} -> casos CONFIRMADOS  de dengue.')
print(f'{casosObtos} -> casos de óBTOS de dengue.')
print(f'Total de casos de DENGUE -> {total} ')
print('=-=' * 20)

