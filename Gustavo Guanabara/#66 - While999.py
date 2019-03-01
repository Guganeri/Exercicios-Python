numero = 0
tot = 0
count = 0

while numero != 999:
    numero = int(input('Digite um numero (999 para parar) '))
    if numero == 999:
        break
    else:
        tot += numero
        count += 1
print(f'A soma dos {count} valores foi {tot}!')
