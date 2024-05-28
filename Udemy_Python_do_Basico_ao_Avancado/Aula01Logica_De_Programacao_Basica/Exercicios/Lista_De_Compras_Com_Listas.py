"""
 Faça uma lista de compras com listas. O usuário deve ter a possibilidade de inserir, apagar e listar valores
 da sua lista. Não permita que o pragrama quebre com erros de indices inexistentes na lista.
 """
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para apagar')
            continue

        for i, valor in enumerate(lista):
            print(f'{i}: {valor}')

        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception as e:
            print(f'Erro desconhecido: {e}')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        else:
            for i, valor in enumerate(lista):
                print(f'{i}: {valor}')
    elif opcao == 's':
        break
    else:
        os.system('cls')
        print('Por favor, escolha uma opção válida: [i]nserir, [a]pagar, [l]istar ou [s]air.')