nome = 'Rogério'
idade = 37
salario = 2278

print('Funcionário {} tem {} seu salário é {:,.2f}'.format(nome, idade, salario))

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)