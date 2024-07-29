# Escopo da classe e de métodos da classe
class Animal:  # Criando uma CLASSE
    # nome = 'Leão'

    def __init__(self, nome):  # Inicializando os ATRIBUTOS
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):  # Criando o MÉTODO comer
        return f'{self.nome} está comando {alimento}'

    def executar(self, *args, **kwargs):  # Criando o MÉTODO executar
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))