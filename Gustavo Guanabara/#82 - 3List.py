valores = list()
impares = list()
pares = list()

while True:
    n = int(input('Digite um numero: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar == 'S':
        continuar
    else:
        break


print(f'Lista Geral: {sorted(valores)}')
print(f'Lista Pares: {sorted(pares)}')
print(f'Listas Impares: {sorted(impares)}')