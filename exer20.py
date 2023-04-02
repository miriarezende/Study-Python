nome= input('informe nome completo: ').strip()
lista= nome.split()
print('nome completo em maiusculo {} \nnome completo em minusculo {}\n '.format(nome.upper(),nome.lower()))
print('o  nome completo tem {} letras\nprimeiro nome tem {} letras' .format(len(nome) - nome.count(' '), len(lista[0])))