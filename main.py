# crie um programa que pede ao usuario
# seu nome e depois da as boas vindas dizendo
# x seja bem vindo onde x e o nome do usuario

# nome = input('Informe o seu nome:\n')
# print(f'seja bem vindo !{nome} .')
# crie um progrma que receba dois valores 
# e exibe qual é o maior numero entre eles 
# nume1 = str(input('informe o primeiro numero\n'))
# nume2 = str(input('informe o segundo numero\n'))

# if nume1 > nume2:
#     print('o primeiro numero é maior : ')
# elif nume2 > nume1:
#     print('Osegundo numero é maior:')   
# else:
#     print('opção invalida')     
#crie um progrma que rebe um numero e imprima seu fatorial
#inporta a fatorial no python
# from math import factorial
# n = int(input('Digite um numero para calcular seu fatorial:'))
# f = factorial(n)
# print('O fatorial de {} é {}.'.format(n,f))
#modo tradicional
n = int(input('Digite um numero para calcular seu fatorial:'))
c = n
f = 1
while c > 0:
    print('{}'.format(c),end='')
    print(' x'if c>1 else '=',end='')
    f = f * c
    c -=1
print('{}'.format(f))    


 