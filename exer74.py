palavras= ('papa', 'date', 'garantia')
for c in palavras:
    print(f'\nna palavra {c.upper()} temos= ', end='')
    for letra in c:
        if letra in 'AaEeIiOoUu':
            print(letra, end=' ')