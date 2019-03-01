numero = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
count = 0
tot = 0
while count < 10:
    numero = numero + razao
    tot +=numero
    count += 1
    print('{} '.format(numero),end='-> ')
print(tot)
