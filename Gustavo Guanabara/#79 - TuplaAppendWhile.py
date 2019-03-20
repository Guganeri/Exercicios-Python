list = []

while True:
    numero = int(input('Digite um numero: '))
    list.append(numero)
    str = input('Deseja continuar? S/N').upper()
    if str == 'S':
        continue
    else:
        print('='*25)
        break

print(list)