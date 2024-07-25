""" Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. """

# Solicita o tamanho da área a ser pintada
area = float(input('Informa o tamanho da área em metros quadrados: '))

coberturaPorLitro = 3  # Define a cobertura da tinta (1 litro para cada 3 metros quadrados)

capacidadeLata = 18  # Define a capacidade de uma lata de tinta (18 litros)

custoLata = 80.00  # Define o preço de uma lata de tinta (R$ 80,00)

litrosNecessario = area * coberturaPorLitro  # Calcula a quantidade de tinta necessária em litros

# Calcula a quantidade de latas de tinta necessárias (arredondando para cima)
import math
latasNecessaria = math.ceil(litrosNecessario / capacidadeLata)

# Calcula o preço total
precoTotal = latasNecessaria * custoLata

# Exibe a quantidade de latas de tinta a serem compradas e o preço total
print(f"Quantidade de latas de tinta a serem compradas: {latasNecessaria}")
print(f"Preço total: R$ {precoTotal:.2f}")
