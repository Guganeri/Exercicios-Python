listagem = (str(input('Digite o nome do produto: ')), float(input('Digite o valor do produto: ')),
str(input('Digite o nome do produto: ')), float(input('Digite o valor do produto: ')),
str(input('Digite o nome do produto: ')), float(input('Digite o valor do produto: ')),
str(input('Digite o nome do produto: ')), float(input('Digite o valor do produto: ')))

for item in range(0,len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}',end='')
    else:
        print(f'R${listagem[item]:>5.2f}')