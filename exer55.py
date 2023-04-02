sexo= input('''F feminino
M masculino
    informe o sexo:''').upper()
while sexo!='M' and sexo!='F':
    sexo= input('''F feminino
M masculino
        digite um caracter valido:''').upper()
#OU
sexo= input('''F feminino
M masculino
    informe o sexo:''').upper()[0]
while sexo not in 'MmFf':
    sexo= input('''F feminino
M masculino
    informe o sexo:''').upper()[0]