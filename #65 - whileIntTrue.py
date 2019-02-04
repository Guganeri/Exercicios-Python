continuar = 'S'
count = 0
maior = 0
menor = 0
tot = 0
while continuar in 'S':
    numero = int(input('Digite um numero: '))
    tot += numero
    count += 1
    if count == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    continuar = str(input('Deseja continuar? [S]ou[N]')).upper()
media = tot/count
print('A média foi:{} '.format(media))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
