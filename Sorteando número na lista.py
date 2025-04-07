#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude-o, lendo o nome deles e escrevendo o nome escolhido.

import random
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('-'*15)
print('O aluno escolhido foi: {}'.format(escolhido))
print()

from random import choice
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('-'*15)
print('O aluno escolhido foi: {}'.format(escolhido))
