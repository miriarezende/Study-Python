""" def area(l, c):
    terreno=l*c
    print(f'area de um terreno {l} x {c} é de {terreno}m².')


area(l=float(input('largura= ')), c=float(input('comprimento= '))) """

#ou

def area(larg, comp):
    a=larg*comp
    print(f'area de um terreno {larg} x {comp} é de {a}m².')


l=float(input('largura (m): '))
c=float(input('comprimento (m): '))
area(l,c)