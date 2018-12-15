from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')

computador = randint(0,2)

print('''Make you choice
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input("Qual é a sua jogada? "))
while jogador <0 or jogador>=3:
    print('Opção Invalida')
    jogador = int(input("Qual é a sua jogada? "))
print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-='*15)
if computador == 0:
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('Você venceu !')
    elif jogador == 2:
        print('Perdeu pra um computador? tsc tsc')
elif computador == 1:
    if jogador == 0:
        print('Você venceu, quem é o bom?!')
    elif jogador == 1:
        print('Empatou')
    elif jogador ==2:
        print('Perdeu, Noob !!')
elif jogador == 2:
    if jogador == 0:
        print('Perdeu,nobão')
    elif jogador == 1:
        print('Ganhou É TETRAA !! !')
    elif jogador == 2:
        print('Empate')