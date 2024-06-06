#4.Faça um programa que imprima a soma dos números naturais de 0 a 10, utilizando o laço for.

soma = 0
for i in range(5):
    num = int(input('Digite 10 números: '))
    soma += num
print(f'A soma dos números Naturais é {soma}')
