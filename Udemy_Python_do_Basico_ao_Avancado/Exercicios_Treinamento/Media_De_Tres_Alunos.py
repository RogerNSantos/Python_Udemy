#  5.Faça um programa que receba o nome de 5 alunos, três notas para cada um, calcule a média e
#  mostre ao final os nomes e a média de cada estudante.

num_alunos = 2
for i in range(num_alunos):
    nome = str(input('Digite o nome do aluno: '))
    soma = 0

    for i in range(1, 4):
        nota = float(input(f"Digite a {i}ª nota: "))
        soma += nota
    media = soma / 3

    if media < 5:
        print(f'Aluno {nome}, está REPROVADO!')
    elif media <= 7:
        print(f'Aluno {nome} em RECUPERAÇÃO!')
    else:
        print(f'Aluno {nome}APROVADO!')




