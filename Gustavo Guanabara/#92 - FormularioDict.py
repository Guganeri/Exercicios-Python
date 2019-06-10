ficha = dict()

ficha['Nome'] = str(input('Digite seu nome: '))
ano = int(input('Digite seu ano de nascimento: '))
anofinal = (2019-ano)
ficha['nascimento'] = anofinal
ctp = int(input('Carteira de trabalho: (0 não tem) '))

if ctp != 0:
    ficha['ctp'] = ctp
    ficha['contratacao'] = int(input('Digite o ano de contratação: '))
    ficha['salario'] = float(input('Digite o valor do salário: '))
    ficha['aposentadoria'] = (2019 - ficha['contratacao']) + 35
else:   
    ficha['ctp'] = ctp


print('-='*30)
print(ficha)
for k, v in ficha.items():
    print(f'{k} tem o valor {v}.')
