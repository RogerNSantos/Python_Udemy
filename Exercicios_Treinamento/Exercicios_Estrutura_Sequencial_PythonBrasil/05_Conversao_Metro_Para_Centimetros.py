# Faça um Programa que converta metros para centímetros.

print('=*=' * 13)
print(' Conversão de Metros para Centímetros.')
print('=*=' * 13)

"""centimetros = 100

metros = float(input('Informe o metro a ser convertido: '))
conversao = metros * centimetros

print(f'{metros} metros convertido para centimetros é {conversao:.0f}')"""

""" Solicita a quantidade de metros ao usuário
metros = float(input("Por favor, informe a quantidade de metros: "))

# Converte metros para centímetros
centimetros = metros * 100

# Imprime o resultado
print(f"{metros} metros é igual a {centimetros} centímetros.")"""


# VERSÃO MAIS DETALHADA
""" 1- Define uma função para converter metros para centímetros.
    2- Define uma função para solicitar a quantidade de metros ao usuário, 
       com validação para garantir que a entrada seja um número positivo.
    3- Implementa um loop principal que permite ao usuário realizar várias 
       conversões ou sair do programa.
    4- Valida a entrada do usuário para continuar ou sair do programa.
    5- Se precisar de mais alguma coisa, estou à disposição!"""


def converter_metros_para_centimetros(metros):
    return metros * 100

def solicitar_metros():
    while True:
        try:
            metros = float(input("Por favor, informe a quantidade de metros: "))
            if metros < 0:
                print("A quantidade de metros deve ser um valor positivo. Tente novamente.")
            else:
                return metros
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def main():
    while True:
        metros = solicitar_metros()
        centimetros = converter_metros_para_centimetros(metros)
        print(f"{metros} metros é igual a {centimetros} centímetros.")

        while True:
            continuar = input("Você deseja realizar outra conversão? (s/n): ").lower()
            if continuar in ['s', 'n']:
                break
            else:
                print("Resposta inválida. Por favor, responda 's' para sim ou 'n' para não.")

        if continuar == 'n':
            print("Obrigado por usar o conversor de metros para centímetros!")
            break

if __name__ == "__main__":
    main()



