""" Faça um programa que verifica se uma letra digitada é VOGAL ou CONSOANTE. """

letra = str(input("Digite uma letra: ")).upper()

vogais = 'AEIOU'

if letra in vogais:
    print(f'A letra {letra} é uma VOGAL!')

elif letra != vogais:
    print(f'A letra {letra} é uma CONSOANTE!')

else:
    print('Entrada inválida! Digite apenas uma letra.')

