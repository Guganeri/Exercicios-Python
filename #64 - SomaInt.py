numero = 0
soma = 0
count = 0

while numero != 999:
    print('Digite 999 quando desejar sair')
    numero = int(input('numero: '))
    if numero != 999:
        soma += numero
        count += 1
print('A soma dos numeros digitados é:{}'.format(soma))
print('A quantidade de numeros atribuidos foi:{}'.format(count))