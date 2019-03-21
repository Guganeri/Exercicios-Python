numeros = list()


while True:
    n = int(input('Digite um numero: '))
    count = 0
    if count == 0:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(numeros[pos])
            pos += 1



    count += 1

    choice = str(input('Deseja continuar?[S/N]')).upper()
    if choice == 'S':
        print('Guardando valores...')
    else:
        break

print(f'O tamanho da lista é: {len(numeros)}')
print(f'Existe o numero 5 na posição {numeros.index+1(5)}')
print(numeros)

