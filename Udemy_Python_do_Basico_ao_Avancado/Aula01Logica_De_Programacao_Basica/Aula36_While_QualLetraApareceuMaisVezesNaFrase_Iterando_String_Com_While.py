
frase = 'Alguns minutos de estudo por dia valem a pena. Pesquisas mostram que os alunos \
que fazem do estudo um hábito têm maior probabilidade de alcançar suas metas. Reserve \
um tempo para estudar e receba lembretes usando seu programador de aprendizado.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_atual_apareceu_mais_vezes = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_letra_atual_apareceu_mais_vezes:
        qtd_apareceu_mais_vezes = qtd_letra_atual_apareceu_mais_vezes
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)