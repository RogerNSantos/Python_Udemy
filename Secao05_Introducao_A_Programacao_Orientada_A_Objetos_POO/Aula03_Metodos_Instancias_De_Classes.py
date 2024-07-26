# -*- coding: utf-8 -*-

""" 
Método em instância de classe Python
Hard coded - É algo que foi escrito diretamente no código
"""  

# Criando a classe Carro
class Carro:
    def __init__(self, nome, cor): # Inicializando os atributos
        self.nome = nome
        self.cor = cor

    def acelerar(self):  # Criando função acelerar
        print(f'{self.nome} {self.cor} está acelerando...')


corsa = Carro('Corsa', 'Preto')
print(corsa.nome, corsa.cor)
corsa.acelerar()
print()
gol = Carro('Gol', 'Prata')
print(gol.nome, gol.cor)
gol.acelerar()