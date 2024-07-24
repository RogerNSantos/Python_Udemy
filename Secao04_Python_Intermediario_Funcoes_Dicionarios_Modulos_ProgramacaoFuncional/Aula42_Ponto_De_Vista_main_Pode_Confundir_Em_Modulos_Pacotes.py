"""from sys import path
# from sys import path

import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import *
# import aula99_package.modulo
# from aula99_package import modulo
# from aula99_package.modulo import *

# from aula99_package.modulo import soma_do_modulo
# # from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula99_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)
# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
from aula99_package.modulo import fala_oi, soma_do_modulo

print(__name__)
fala_oi()

#     'soma_do_modulo',
#     'nova_variavel',
# ]
from aula99_package.modulo_b import fala_oi

variavel = 'Alguma coisa'

@@ -12,3 +13,4 @@ def soma_do_modulo(x, y):


nova_variavel = 'OK'
# fala_oi()
 2 changes: 2 additions & 0 deletions2
aula99_package/modulo_b.py
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,2 @@
def fala_oi():
    print('oi')"""