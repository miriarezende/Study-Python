""" numbers= list()
pares=[]
impares=[]
for c in range(0,7):
    numero= int(input('informe um valor: '))
    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)
pares.sort()
impares.sort()
numbers=pares+impares
print(numbers) """
#OU
numbers= [[], []]
for c in range(0,7):
    numero= int(input('informe um valor: '))
    if numero%2==0:
        numbers[0].append(numero)
    else:
        numbers[1].append(numero)
numbers[0].sort()
numbers[1].sort()
print(f'valores pares informados: {numbers[0]}')
print(f'valores impares informados: {numbers[1]}')