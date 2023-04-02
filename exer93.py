def soma(*num):
    for i in range(0,len(num)):
        if i==len(num)-1:
            print(end='' f'{num[i]}')
        else:
            print(f'{num[i]} + ', end='')
    s=sum(num)
    print(end='' f'= {s}')
    print()
soma(3,1,3)
soma(3,6)
soma(5,2)