total = totmil = count = menor = 0
menorProd = ''
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: '))
    total += preço
    count += 1
    if preço >= 1000:
        totmil += 1
    if count == 1:
        menor = preço
        menorProd = produto
    else:
        if preço < menor:
            menor = preço
            menorProd = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total Gasto foi {total}')
print(f'Quantidade de Produtos custando mais de R$1000 = {totmil}')
print(f'O produto mais barato é o {menorProd} e custa:R${menor}')



