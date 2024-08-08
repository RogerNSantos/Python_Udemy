print('-*' * 20)
print('\t JOGO DA ADIVINHAÇÃO \t')
print('*-' * 20)

import random

# Função para exibir o menu de níveis
def escolhendo_nivel():
    while True:
        print('Escolha o nível de dificuldade:')
        print('nível 1 - Fácil (20 Tentativas)')
        print('Nível 2 - Médio (10 Tentatívas)')
        print('Nível 3 - Difícil (5 Tentativas)')
        nivel = int(input('Escolha o nível: '))
        if nivel in [1, 2, 3]:
            return nivel
        else:
            print('Nível inválido. escolha de 1 a 3.')

# Função para definir o número de tentativas baseado no nível
def numero_tentativas(nivel):
    if nivel == 1:
        return 20
    
    elif nivel == 2:
        return 10
    
    elif nivel == 3:
        return 5
    
# Função para calcular pontuação
def calculando_pontuacao(pontuacao, chute, numero_secreto):
    return pontuacao - abs(chute - numero_secreto)

nivel = escolhendo_nivel()
tentativas = numero_tentativas(nivel)
numero_secreto = random.randint(1, 40) # Número secreto aleatória 1 a 40
pontuacao = 1000

print(f'Você escolheu o nível {nivel}. Tentativas: {tentativas}')
print('O número secreto está entre 1 a 40.')

for rodada in range(1 , tentativas + 1):
    print(f'Tentativa {rodada} de {tentativas}')

    while True:
        chute = int(input('Digite um número: '))
        if 1 <= chute <= 40:
            break
        else:
            print('Por favor, digite um número válido entre 1 e 40.')
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

    # Atualizando a pontua~ção
    pontuacao = calculando_pontuacao(pontuacao, chute, numero_secreto)
    print(f'Sua pontuação é: {pontuacao}')

else:
    print(f'Você usou todas as tentativas! O número secreto é {numero_secreto}.')

print('-*' *20)
print('\t FIM DO JOGO \t')
print('*-' * 20)
