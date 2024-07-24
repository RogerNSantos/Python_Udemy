# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

#Criando uma classe carro
class Carro:
    ...

#Criando Objeto carro1 e seus atributos
carro1 = Carro()
carro1.nome = 'BMW'
carro1.cor = 'Preta'

#Criando ojeto carro2 e seus atributos
carro2 = Carro()
carro2.nome = 'FIAT'
carro2.cor = 'Azul'

print(carro1.nome)
print(carro1.cor)

print(carro2.nome)
print(carro2.cor)