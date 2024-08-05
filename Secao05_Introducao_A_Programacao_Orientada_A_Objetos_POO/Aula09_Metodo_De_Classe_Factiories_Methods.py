# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2024 # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

pessoa1 = Pessoa('Rogério', 34)
pessoa2 = Pessoa.criar_com_50_anos('Santos')
pessoa3 = Pessoa('Anônima', 23)
pessoa4 = Pessoa.criar_sem_nome(25)

print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)
print('Anônina', 23)
print(pessoa4.nome, pessoa4.idade)
