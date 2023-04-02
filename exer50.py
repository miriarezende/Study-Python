n1=int(input('informe um numero: '))
primo=0
for c in range(1,n1+1):
    if n1%c==0:
        primo+=1
if primo>2:
    print('numero não é primo')
elif n1==0:
    print('numero informado é 0, não é primo nem composto')
else:
    print('numero primo')