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
print(f'Os elementos estão ordenados de forma decrescente: {sorted(numeros[::-1])}')
for indice, valores in enumerate(numeros):
    if 5 in numeros:
        print(f'Existe o valor 5 na posição {indice}')
        break
    else:
        continue
    indice += 1