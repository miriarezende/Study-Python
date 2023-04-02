n= int(input('primeiro termo: '))
r=int(input('razão='))
termo= n
c=1
total=0
mais=10
while mais !=0:
    total+= mais
    while c<=total:
        print('{}'.format(termo),end='__')
        termo+=r
        c+=1
    mais= int(input('quantos termos voce quer mostrar: '))
print('finalizada com {} termos mostrados'.format(total))