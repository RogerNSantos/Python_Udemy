#__dict__ e vars para atribuidos de instâncias

class Pessoa:
    anoAtual = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def getAnoNascimento(self):
        return Pessoa.anoAtual - self.idade



dados = {'nome': 'Rogério', 'idade': 35}
pessoa1 = Pessoa(**dados)

print(vars(pessoa1))
print(pessoa1.nome)
