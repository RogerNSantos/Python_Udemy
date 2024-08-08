print('=*' * 22)
print('\tBEM VINDO AO JOGO DA FORCA')
print('*=' * 22)

palavra_secreta = 'Banana'
letras_acertadas = ['*', '*', '*', '*', '*', '*']
acertou = False
erros = 0

print(letras_acertadas)
while not acertou and erros < 6:
    chute = str(input('Digite uma letra: ')).upper()

    if chute in palavra_secreta.upper():
        posicao = 0
        for letra in palavra_secreta:
            if chute == letra.upper():
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1

    print(letras_acertadas)
    print(f'Erros: {erros}')

    acertou = '*' not in letras_acertadas

    print('Jogando...')

if acertou:
    print('Parabéns, você ganhou!!!')
else:
    print('Que pena, você perdeu!!!')

print(f'A palavra secreta era: {palavra_secreta}')
print('*** FIM DO JOGO ***')

