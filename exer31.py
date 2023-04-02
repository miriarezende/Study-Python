n1= int(input('informe primeiro numero: '))
n2= int(input('informe segundo numero: '))
n3= int(input('informe terceiro numero: '))
if n1>n2 and n1>n3:
    print('{} maior numero informado'.format(n1))
if n2>n1 and n2>n3:
    print('{} maior numero informado'.format(n2))
if n3>n1 and n3>n1:
    print('{} maior numero informado'.format(n3))
if n1<n2 and n1<n3:
    print('{} menor numero informado'.format(n1))
if n2<n1 and n2<n3:
    print('{} menor numero informado'.format(n2))
else:
    print('{} menor numero informado'.format(n3))