from random import randint
from time import sleep
jogofull = list()

while len(jogofull) <= 6:
   computador = randint(0, 60)
   jogofull.append(computador)

print('-='*30)
print('JOGO NA MEGA SENA')
print('-='*30)

jogos = int(input('Digite a quantidade de jogos que desej gerar: '))

sleep(1)
print('\nSortendo Jogos')
sleep(1)
for n in range(jogos):
    sleep(1)
    print(f'Jogo[{n+1}] -> {jogofull}] ')