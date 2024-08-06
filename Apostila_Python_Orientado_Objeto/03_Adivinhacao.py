print('*' * 30)
print('     JOGO DA ADIVINHAÇÃO      ')
print('*' * 30)

numero_secreto = 86

chute = int(input('Digite um número de 0 a 100: '))
print(f'Você digitou o número {chute}')

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print(f'Você acerto, o número é {numero_secreto}!')

elif maior:
    print('Você errou! Seu chute foi maior que o número secreto.')

elif menor:
    print('Você errou! Seu chute foi menor que o número secreto.')

print('*' *30)
print('     FIM DO JOGO      ')
print('*' * 30)