numero = 0
count = 0
tot = 0
while numero != 'srt':
    numero = int(input('Quer vcer a tabuada de qual valor? '))
    if numero < 0:
        break
    else:
        while count <= 9:
            tot = numero * count
            print(f'{numero} x {count} = {tot}')
            count += 1