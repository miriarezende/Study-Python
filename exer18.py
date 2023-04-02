from random import choice

n1= input('nome aluno1: ')
n2= input('nome aluno2: ')
n3= input('nome aluno3: ')
n4= input('nome aluno4: ')
lista = [n1, n2, n3, n4]
escolha= choice(lista)
print('aluno sorteado foi {}'.format(escolha))