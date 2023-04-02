frase= input('digite sua frase:').strip().split()
words=''.join(frase)
cont=len(words)
words.lower()
poli=0
for c in range(0,cont):
    if words[c]==words[cont-c-1]:
        poli+=1
if poli==cont:
    print('polindromo')
else:
    print('frase normal')