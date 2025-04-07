#Média Aritmética


#Calcule um programa que leia as duas notas de um aluno. Calcule e mostra a sua
#média.

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
média = (n1+n2)/2
print('A média entre {} e {} é igual a: {}.'.format(n1, n2, média))
print()

#Código com arredondamento

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
média = (n1+n2)/2
print('A média entre {:.1f} e {:.1f} é igual a: {:.1f}.'.format(n1, n2, média))
print()

#Código para as 4 notas do Aluno

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))
n4 = float(input('Digite a quarta nota do aluno: '))

média = (n1+n2+n3+n4)/4
print('A média entre {:.1f}, {:.1f}, {:.1f} e {:.1f} é igual a: {:.1f}.'.format(n1, n2, n3, n4, média))
print()
