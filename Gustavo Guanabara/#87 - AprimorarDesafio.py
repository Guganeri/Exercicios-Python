### Resolução Guanabara ###
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maiorsegundalinha = somatot = 0
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

somaterceiracoluna += matriz2[0][2] + matriz2[1][2] + matriz2[2][2]

if maiorsegundalinha == 0:
    maiorsegundalinha = matriz2[1][0]
    if maiorsegundalinha < matriz2[1][1]:
        maiorsegundalinha = matriz2[1][1]
    if maiorsegundalinha <matriz2[1][2]:
        maiorsegundalinha = matriz2[1][2]

print('-=' * 30)
print(f'A soma dos numeros pares é: {somatot}')
print(f'Soma dos valores da terceira coluna é: {somaterceiracoluna}')
print(f'O maior valor da segunda linha {maiorsegundalinha}')