numeros = list()

while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)
    choice = str(input('Deseja continuar?[S/N]')).upper()
    if choice == 'S':
        print('Guardando valores...')
    else:
        break

print(f'O tamanho da lista é: {len(numeros)}')
numeros.sort(reverse=True)
print(numeros)
if 5 in numeros:
    print(f'Existe o numero 5 na posição {numeros.index(5)}')


