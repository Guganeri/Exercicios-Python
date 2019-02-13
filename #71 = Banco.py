print('='*30)
print('{:^30}'.format('BANCO'))
print('='*30)
valorSacado = int(input('Que valor você deseja sacar? R$'))
total = valorSacado
céd = 50
coutCed = 0
while True:
    if total >= céd:
        total -= céd
        coutCed += 1
    else:
        print(f'Total de {coutCed} cédulasa de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        coutCed = 0
        if total == 0:
            break
print('='*30)
print('Finalizado')