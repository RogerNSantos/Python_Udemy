""" João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia
a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
 Imprima os dados do programa com as mensagens adequadas. """

# Solicitando os quilos para usuário
pesoPeixes = float(input('Informe o peso dos peixeis: '))

# Definindo o limite de peso e a taxa da multa
pesoLimite = 50.0
taxaMulta = 4.0

# Calculando o excesso de peso
excesso = max(0, pesoPeixes - pesoLimite)

# Calculando a multa
multa = excesso * taxaMulta

# Exibindo os resultados
print(f'Peso dos peixes: {pesoPeixes:.2f} KG')
print(f'Excesso de peso: {excesso:.2f} KG')
print(f'Multa a pagar: R$ {multa:.2f}')




