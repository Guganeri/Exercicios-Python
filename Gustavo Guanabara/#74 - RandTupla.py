from random import randint
numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100),)
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO Maior numero sorteado foi:{max(numeros)}')
print(f'O Menor numero sorteado foi:{min(numeros)}')




