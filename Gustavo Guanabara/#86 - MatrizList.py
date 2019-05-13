matriz = [[], [] ,[]]
numero = 0
for n in range(9):
    numero = (int(input(f'Digite o {n+1} valor: ')))
    if n<=2:
        matriz[0].append(numero)
    elif n>=4 and n<=6:
        matriz[1].append(numero)
    else:
        matriz[2].append(numero)
print('-=' *30)
print(f'Matriz 1 {matriz[0]}')
print(f'Matriz 2 {matriz[1]}')
print(f'Matriz 3 {matriz[2]}')

### Resolução Guanabara ###
matriz2 = [[0,0,0], [0, 0, 0], [0, 0, 0]]
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz2[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}] : '))
print('-=' *30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz2[linha][coluna]:^5}]', end='')
    print()