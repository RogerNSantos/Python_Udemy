valores = [0, 1, 2, 3]
menor_valor = min(valores)
print(menor_valor)

print('######################################')

valores = [1, 2, 3, 4]
print(min(valores))
print(max(valores))
print('######################################')

print([valores[2]]) #Acessando o indice

valores[0] = 8 #Adicionando 8 no lugar do 0
print(valores) 

print('Tamanho da lista')
print(len(valores))

print(8 in valores)
print(0 in valores)

valores.append(10) # Adicionando 10 na ultima  posição
print(valores)

removido = valores.pop(4)
print(f'Valor removido {removido}')
print(f'Listá atualizada {valores}')