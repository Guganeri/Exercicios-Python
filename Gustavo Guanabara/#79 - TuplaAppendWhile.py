list = []

while True:
    numero = int(input('Digite um numero: '))
    if numero not in list:
        list.append(numero)
        print('Adcionado com sucesso')
    else:
        print('Valor duplicado não adcionado')
    str = input('Deseja continuar? [S/N] ').upper()
    if str == 'S':
        continue
    else:
        print('-='*25)
        break
print(sorted(set(list)))




