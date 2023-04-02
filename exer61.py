n=int(input('informe qnts termos serão mostrados: '))
c=2
primeiro=0
proximo=1
print(primeiro,proximo, end=' ')
while c<n:
    c+=1
    fibo=primeiro+proximo
    primeiro=proximo
    proximo=fibo
    print(fibo, end=' ')