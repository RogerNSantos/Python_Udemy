""" Receba numeros inteiros e mostre a soma.Crie uma estrutura
de validação para continuar ou finalizar. """

"""while True:
    print('*-' * 25)
    print('SOMA DOS NÚMEROS INTEIROS')
    print('*-' * 25)

    # Recebe dois números inteiros
    num1 = int(input('\nDigite o 1º número inteiro: '))
    num2 = int(input('Digite o 2º número inteiro: '))

    # Calculando a soma
    soma = num1 + num2
    print(f'\n A SOMA dos números {num1} + {num2} = {soma}')

    # Pergunta se o usuário deseja continuar
    opcao = str(input('Deseja continuar? Digite "S" para continuar ou qualquer tecla para finalizar.')).upper()
    if opcao != 'S':
        break

print('\n FIM DO PROGRAMA!!!')"""

print('*-' * 25)
print('         SOMA DOS NÚMEROS INTEIROS')
print('*-' * 25)

soma = 0
while True:
    num = 1
    while num != 0:  # laço while
        num = int(input("\nInforme um numero (0 para parar): "))
        soma += num

    resp = input("\nPara continuar digite 's', FIM outra letra: ").lower()
    if resp != 's':
        break
    print("\033[H\033[J", end="")  # Limpa a tela no terminal

print(f"\nSoma = {soma}")
