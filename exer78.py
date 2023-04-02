numeros= list()
for c in range(0,5):
    n=int(input('informe um valor: '))
    if c==0:
        numeros.append(n)
    else:
        qnt=0
        while qnt<len(numeros):
            if n<=numeros[qnt]:
                numeros.insert(qnt,n)
                break
            qnt+=1
print(numeros)