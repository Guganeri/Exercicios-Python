### Resolução Guanabara ###
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somatot = 0
somaterceiracoluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz2[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}] : '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz2[linha][coluna]:^5}]', end='')
    print()

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz2[linha][coluna] % 2 == 0:
            somatot = matriz2[linha][coluna]

somaterceiracoluna += matriz2[0][3]
somaterceiracoluna += matriz2[1][3]
somaterceiracoluna += matriz2[2][3]

print('-=' * 30)
print(f'A soma dos numeros pares é: {somatot}')
print(f'Soma dos valores da terceira coluna é: {somaterceiracoluna}')