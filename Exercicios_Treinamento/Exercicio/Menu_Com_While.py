# *Fazer um MENU a partir do recebimento de dois numeros,
# calcule e mostre: a soma, subtracao,produto,divisao,potencia
# e raiz da soma.
import math

while True:
    print("\n******************************")
    print("      O P E R A C O E S")
    print("********************************")

    print('\n****** Opções disponíveis ******')

    print("\nDigite '1' para -> SOMAR")
    print("Digite '2' para -> SUBTRAIR")
    print("Digite '3' para -> MULTIPLICAR")
    print("Digite '4' para -> DIVISAO")
    print("Digite '5' para -> POTENCIA")
    print("Digite '6' para -> RAIZ DA SOMA")

    print("\nDigite uma das opções do MENU: ")

    opcao = int(input())

    if opcao == 1:
        print('Você escolheu SOMAR')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        soma = num1 + num2
        print(f'A SOMA de {num1} + {num2} = {soma}')

    elif opcao == 2:
        print('Você escolheu SUBTRAIR')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        subtrair = num1 - num2
        print(f'A SUBTRÇÃO  dos números {num1} - {num2} = {subtrair}')

    elif opcao == 3:
        print('Você escolheu MULTIPLICAR')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        multiplicar = num1 * num2
        print(f'A MULTIPLICAÇÃO dos números {num1} * {num2} = {multiplicar}')

    elif opcao ==4:
        print('Você escolheu DIVISÃO')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        divisao = num1 / num2
        print(f'A DIVISÃO dos números {num1} / {num2} = {divisao}')

    elif opcao == 5:
        print('Você escolheu POTÊNCIA')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        #potencia = num1 ** num2
        #print(f'A POTÊNCA de {num1} ** {num2} = {potencia}')
        potencia = math.pow(num1, num2)
        print(f"\n\tA POTÊNCIA de {num1:.2f} ** {num2:.2f} = {potencia:.2f}")

    elif opcao == 6:
        print('Você escolheu RAIZ DA SOMA')
        num1 = float(input('Digite o primiro número: '))
        num2 = float(input('Digite o segundo número: '))
        soma = num1 + num2
        if soma >= 0:
            raizQuadrada = math.sqrt(soma)
            print(f'A RAIZ DA SOMA de {num1:.2f} - {num2:.2f} = {raizQuadrada}')
        else:
            print("\n\tErro: Não existe raiz quadrada de número negativo.")
    else:
        print('OPÇÃO INVÁLIDA NO MENU!!!')

    resp = str(input('Deseja continuar? Digite se sim digite "S" ou qualquer teclar para finalizar.')).upper()
    if resp != 'S':
        break

print('FIM DO PROGRAMA!')







