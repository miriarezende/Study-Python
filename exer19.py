from random import shuffle
n1= input('nome aluno1: ')
n2= input('nome aluno2: ')
n3= input('nome aluno3: ')
n4= input('nome aluno4: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('ordem sorteada: {}'.format(lista)) 