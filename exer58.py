n1= int(input('digite um numero: '))
c=n1
f=1
while c>0:
    print('{}'.format(c), end='')
    print('x' if c> 1 else '=', end='')
    f*= c
    c-=1
print('{}'.format(f))
#OU
for c in range(1,n1):
    if c ==1:
        fatorial= n1
    else:
        fatorial*=c
    print(fatorial)