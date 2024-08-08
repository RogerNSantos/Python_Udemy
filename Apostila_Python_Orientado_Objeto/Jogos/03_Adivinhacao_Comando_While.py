print('*' * 30)
print('     JOGO DA ADIVINHAÇÃO      ')
print('*' * 30)

numero_secreto = 86
total_tentativas = 3
tentativa_atual = 1

while tentativa_atual <= total_tentativas:    
    print(f'Tentativa {tentativa_atual}ª de {total_tentativas}')
   
    chute = int(input('Digite um número de 0 a 100: '))
    print(f'Você digitou {chute}')

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print(f'Você acertou, o número é {numero_secreto}!')
        break
    elif maior:
        print('Você errou! Seu chute foi maior que o número secreto.')

    elif menor:
        print('Você errou! Seu chute foi menor que o número secreto.')

    tentativa_atual += 1

if tentativa_atual > total_tentativas:
    print(f"Você usou todas as suas tentativas. O número secreto era {numero_secreto}.")

print('*' *30)
print('     FIM DO JOGO      ')
print('*' * 30)


"""import random

# Gera um número secreto aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
total_de_tentativas = 5
tentativa_atual = 1

print("Bem-vindo ao jogo de adivinhação!")
print("Você tem 5 tentativas para adivinhar o número secreto entre 1 e 100.")

while tentativa_atual <= total_de_tentativas:
    print(f"Tentativa {tentativa_atual} de {total_de_tentativas}")
    
    # Solicita um chute do usuário
    chute_str = input("Digite o seu palpite: ")
    
    # Verifica se a entrada é um número válido
    try:
        chute = int(chute_str)
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    # Verifica o chute do usuário
    if chute == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif chute > numero_secreto:
        print("O seu chute foi maior que o número secreto.")
    else:
        print("O seu chute foi menor que o número secreto.")
    
    tentativa_atual += 1

if tentativa_atual > total_de_tentativas:
    print(f"Você usou todas as suas tentativas. O número secreto era {numero_secreto}.")

print("Fim do jogo.")
"""