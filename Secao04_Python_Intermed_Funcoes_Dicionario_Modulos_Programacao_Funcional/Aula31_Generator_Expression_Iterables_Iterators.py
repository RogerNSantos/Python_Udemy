import sys

#Generator expression, Iterables e Iterators em Python
iterable = ['Rogério', 'Carro', '__Iter__']
iterador = iter(iterable)
lista = [n for n in range(100)]
genertor = (n for n in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(genertor))

print(genertor)
#print(lista)