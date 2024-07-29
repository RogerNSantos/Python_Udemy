""" Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
  que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e 
sempre arredonde os valores para cima, isto é, considere latas cheias. """

import math

# Solicita o tamanho da área a ser pintada
area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# Cálculo da quantidade de tinta necessária, considerando 10% de folga
cobertura_por_litro = 6
litros_necessarios = (area * 1.10) / cobertura_por_litro

# Situação 1: Apenas latas de 18 litros
litros_por_lata = 18
num_latas = math.ceil(litros_necessarios / litros_por_lata)
custo_latas = num_latas * 80
print(f"\nComprando apenas latas de 18 litros:")
print(f"Quantidade de latas necessárias: {num_latas}")
print(f"Custo total: R$ {custo_latas:.2f}")

# Situação 2: Apenas galões de 3,6 litros
litros_por_galao = 3.6
num_galoes = math.ceil(litros_necessarios / litros_por_galao)
custo_galoes = num_galoes * 25
print(f"\nComprando apenas galões de 3,6 litros:")
print(f"Quantidade de galões necessários: {num_galoes}")
print(f"Custo total: R$ {custo_galoes:.2f}")

# Situação 3: Mistura de latas e galões para menor desperdício
# Calcula o número de latas e galões necessários para o menor desperdício
num_latas_mistura = math.floor(litros_necessarios / litros_por_lata)
litros_restantes = litros_necessarios - (num_latas_mistura * litros_por_lata)
num_galoes_mistura = math.ceil(litros_restantes / litros_por_galao)
custo_mistura = (num_latas_mistura * 80) + (num_galoes_mistura * 25)

print(f"\nMisturando latas e galões para menor desperdício:")
print(f"Quantidade de latas necessárias: {num_latas_mistura}")
print(f"Quantidade de galões necessários: {num_galoes_mistura}")
print(f"Custo total: R$ {custo_mistura:.2f}")
