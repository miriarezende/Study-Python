""" aluno= []
sala= []
while True:
    aluno.append(input('nome aluno: '))
    nota1=float(input('nota 1: '))
    nota2=float(input('nota 2: '))
    media=(nota1+nota2)/2
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    sala.append(aluno[:])
    aluno.clear()
    resp=input('deseja continuar? ').lower()
    while resp not in 'ns':
        resp=input('tente novamente, dseja continuar? ').lower()
    if resp=='n':
        break
print('COD.  NOME  MEDIA')
for c in range(0, len(sala)):
    print(f'{c}     {sala[c][0]}    {sala[c][3]}')
while True:
    n=int(input('mostrar notas de qual aluno? (999 condição de parada)'))
    if n==999:
        break
    print(sala[n][1] ,'e', sala[n][2]) """
#OU
ficha=  list()
while True:
    nome= input('nome: ')
    nota1= float(input('nota 1: '))
    nota2= float(input('nota 2: '))
    media= (nota1+nota2)/2
    ficha.append([nome, [nota1,nota2], media])
    resp= input('quer continuar? (S/N)')
    while resp not in 'ns':
        resp=input('tente novamente, dseja continuar? ').lower()
    if resp=='n':
        break
print(f'{"COD":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    n=int(input('mostrar notas de qual aluno? (999 condição de parada)'))
    if n==999:
        break
    if n<=len(ficha) - 1:
        print(f'notas de {ficha[n][0]} são {ficha[n][1]}')
print('END')