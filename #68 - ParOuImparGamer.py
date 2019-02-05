from random import randint
from time import sleep
win = 'true'
result = 0
nome = 'unk'
count = 0
while win in 'true':
    computador = randint (1,20)
    if computador % 2 == 0:
        result = 1
        nome = 'PAR'
    else:
        result = 2
        nome = 'IMPAR'
    print('='*14)
    choice = str(input('Par ou Impar? ')).upper()
    print('='*14)
    sleep(1)
    if choice == nome:
        print(f'Você venceu escolhendo {choice} o numero foi {computador}')
        win == 'true'
        count += 1
    else:
        print(f'Você perdeu escolhendo {choice} o numero foi {computador}')
        break
print(f'O total de vitorias foi:{count}')

