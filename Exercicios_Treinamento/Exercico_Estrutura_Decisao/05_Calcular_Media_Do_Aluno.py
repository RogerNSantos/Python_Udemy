""" Faça um programa para leitura de duas notas parciais de um aluno. O programa deve
 calcular a média alcançada por aluno e apresentar:
 A mensagem "APROVADO", se a média alcançada for maior ou igual a sete
 A mensagem "REPROVADO", se a média for menor do que sete
 A mensagem "APROVADO COM DISTINÇÃO", se a média for igual a dez"""

print("=*" * 20)
print('\t\t\tBOLETIM ESCOLAR')
print('*=' * 20)

# Solicitando as informações para usuário
nomeAluno = str(input('Nome do aluno: '))
nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))

# Calculando a média
mediaAluno = (nota1 + nota2) / 2

if mediaAluno == 10:
    print(f'Média {mediaAluno}, aluno {nomeAluno} APROVADO COM DISTINÇÃO!')

elif mediaAluno >= 7:
    print(f'MÉDIA {mediaAluno} aluno {nomeAluno} APROVADO!')

else:
    print(f'Média {mediaAluno}, aluno {nomeAluno} REPROVADO!')
