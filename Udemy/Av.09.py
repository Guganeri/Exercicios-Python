def up_low(s):
    up = 0
    low = 0
    especial = 0

    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
        else:
            especial += 1

    print(f'Numero de caracteres Maiúsculos:{up}')
    print(f'Numero de caracteres Minúsculos:{low}')
    print(f'Numero de caracteres Especial ou Vazio:{especial}')

up_low('Olá, mundo!')

 