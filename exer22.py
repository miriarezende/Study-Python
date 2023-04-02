#validação string
cdd = input('digite nome da sua cidade: ')
cdd= cdd.upper()
cdd= cdd.split()
if cdd[0] == 'SANTO':
    print('começa com SANTO')
else:
    print('não começa com SANTO') 

cdd = input('digite nome da sua cidade: ').upper()
cdd= cdd.split()
print('Sua cidade começa com SANTO: {}'.format('SANTO' in cdd))