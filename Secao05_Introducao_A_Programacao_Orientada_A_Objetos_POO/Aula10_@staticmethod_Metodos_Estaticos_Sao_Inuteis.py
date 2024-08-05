# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Olá', args, kwargs)

def funcao(*args, ** kwargs):
        print('Oi', args, kwargs)

classe1 = Classe()
classe1.funcao_que_esta_na_classe(1, 2, 3)

funcao(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeada=18)
funcao(nomeada=18)
