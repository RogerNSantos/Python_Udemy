# Receber numeros e mostrar a soma.- laço do while

soma = 0

while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 0:
        break
    soma += numero
print(f'As somas dos números é {soma}')
