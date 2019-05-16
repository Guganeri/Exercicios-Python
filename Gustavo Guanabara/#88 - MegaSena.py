from random import randint
from time import sleep
jogofull = list()
jogofinal = list()
tot = 1

print('-='*30)
print('JOGO NA MEGA SENA')
print('-='*30)

jogos = int(input('Digite a quantidade de jogos que desej gerar: '))

sleep(1)
print('\nSortendo Jogos')
sleep(1)

while tot <= jogos:
    cont = 0
    while True:
        computador = randint(1, 60)
        if computador not in jogofull:
            jogofull.append(computador)
            cont += 1
        if cont >= 6:
            break
    jogofull.sort()
    jogofinal.append(jogofull[:])
    jogofull.clear()
    tot += 1
print(jogofinal)

