# Atributo de classe

class Pessoa:
    anoAtual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def getAnoNascimento(self):
        return self.anoAtual - self.idade
    

pessoa1 = Pessoa('Rogério', 38)
pessoa02 = Pessoa('Ana Vitória', 11)
pessoa03 = Pessoa('Nícolas', 7)

print(Pessoa.anoAtual)

print(pessoa1.getAnoNascimento())
print(pessoa02.getAnoNascimento())
print((pessoa03.getAnoNascimento()))