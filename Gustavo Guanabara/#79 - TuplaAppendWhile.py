list = []

while True:
    numero = int(input('Digite um numero: '))
    list.append(numero)
    str = input('Deseja continuar? [S/N] ').upper()
    print('Adcionado com sucesso ...')
    if str == 'S':
        continue
    else:
        print('-='*25)
        break

print(sorted(set(list)))

