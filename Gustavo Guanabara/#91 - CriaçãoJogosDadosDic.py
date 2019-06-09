from random import randint
from time import sleep
from operator import  itemgetter

jogo = { 'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6),
         'jogador5': randint(1, 6),
         'jogador6': randint(1, 6)}

ranking = dict()

print('Valores sorteados:')
for keys, values in jogo.items():
    print(f'{keys} tirou {values} no dado.')
    sleep(1)

#Os valores no dicionario original jogo não pode ser alterado com sorted, por isso criar um novo dicionario chamado ranking
#com o dicionario ranking habilita o sorted e usa para ler a key na posição 1 ativando o reverse True pois por default
#é setado como false
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

#print(ranking)
print('-='*30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

