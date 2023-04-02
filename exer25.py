nome= input('digite seu nome: ').strip()
nome= nome.split()
#print('primeiro nome: {} \nultimo nome: {}'.format(nome[0], nome[len(nome)-1]))
print('primeiro nome: {} \nultimo nome: {}'.format(nome[0], nome[-1]))