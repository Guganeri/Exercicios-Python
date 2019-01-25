ma = 0
me = 0
ano = 2019
for c in range(1,8,1):
    idade = int(input("Digite o ano de nascimento {}:".format(c)))
    idade = ano - idade
    if idade >= 18:
        ma += 1
    else:
        me += 1
print('O numero de maiores de idade:{}'.format(ma))
print('O numero de menores de idade:{}'.format(me))