sidade= ssexo= smulher=0
while True:
    idade=int(input('idade: '))
    sexo=input('''[M] masculino\n[F]feminino 
        sexo: ''').upper()
    while sexo !='M' and sexo !='F':
        sexo=input('''invalido, tente novamente
[M] masculino\n[F]feminino 
        sexo: ''').upper()
    if idade>18:
        sidade+=1
    if sexo=='M':
        ssexo+=1
    if sexo=='F' and idade<20:
        smulher+=1
    resp= input('deseja continuar: ').upper()
    while resp not in 'NS':
        resp= input('invalido, deseja continuar: ').upper()
    if resp=='N':
        break
print(f'{sidade} pessoas maiores de 18 anos\nforam cadastrados {ssexo} homens\n{smulher} mulheres com menos de 20 anos')