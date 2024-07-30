""" Faça um programa se a letra digitada é 'F' ou 'M'. Conforme a letra escrever:
F - Feminino
M - Masculino
Sexo inválido. """

letra = str(input('Digite "F" para feminino "M" para masculino: ')).upper()

if letra == 'F':
    print(f'{letra} - sexo FEMININO')

elif letra == 'M':
    print(f'{letra} - sexo MASCULINO')

else:
    print('Sexo INVÁLIDO!!!')
