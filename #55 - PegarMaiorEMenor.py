mpeso = 0
npeso = 0
for c in range(1,6):
    peso = float(input('Digite o peso: '))
    if c == 1:
        mpeso = peso
        npeso = peso
    else:
        if peso > mpeso:
            mpeso = peso
        elif npeso > peso:
            npeso = peso
print('Maior Peso {}'.format(mpeso))
print('Menor Peso {}'.format(npeso))
