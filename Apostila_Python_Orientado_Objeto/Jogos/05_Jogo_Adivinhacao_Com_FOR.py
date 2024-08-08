print('-*' * 20)
print('\t JOGO DA ADIVINHAÇÃO \t')
print('*-' * 20)

numero_secreto = 40
tentativas = 3

for rodada in range(1 , tentativas + 1):
    print(f'Tentativa {rodada} de {tentativas}')

    chute = int(input('Digite um número de 1 a 40: '))
    print(f'Você digitou {chute}!')

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('PARABÉNS, você acertou!!!')
        break
    elif maior:
        print(f'Você errou! Seu chute foi maior que o número secreto.')

    elif menor:
        print(f'Você errou! Seu chute foi menor que o númeri secreto.')

else:
    print(f'Você usou todas as tentativas! O número secreto é {numero_secreto}.')

print('-*' *20)
print('\t FIM DO JOGO \t')
print('*-' * 20)