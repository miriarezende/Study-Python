""" n= int(input('primeiro termo: '))
r=int(input('razão='))
print('progressão= ')
c=1
while c!=10:
    if c==0:
        print(n)
    else:
        n+=r
        print('{}'.format(n),end='__')
    c+=1 """
#OU
n= int(input('primeiro termo: '))
r=int(input('razão='))
termo= n
c=1
while c<=10:
    print('{}'.format(termo),end='__')
    termo+=r
    c+=1
print('fim')