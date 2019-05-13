maior = menor = contador = 0
pessoas = list()
cont = True

while cont == True:
    pessoas[0].append(str(input('Nome: ')))
    pessoas[0].append(float(input('Peso: ')))
    contador += 1
    if pessoas[0]:
        maior = pessoas[0]
        menor = pessoas[0]

    cont = input('Deseja adicionar outra pessoa? [S/N]').upper()
    if (cond == 'S'):
        continue
    elif (cond == 'N'):
        break

