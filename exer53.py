for c in range(0,5):
    peso= float(input('pessoa {}, peso: '.format(c+1)))
    if c==0:
        maior=peso
        menor=peso
    else: 
        if peso>maior:
            maior=peso
        elif peso<menor:
            menor=peso
print('maior peso lido: {}\nmenor peso lido: {}'.format(maior, menor))