data = int(input('Digite o ano de nascimento'))
ano = 2018
idade = ano - data

if idade <= 9:
    print('Categoria MIRIM')
elif idade >= 10 and idade <=14:
    print('INFANTIL')
elif idade >= 15 and idade<=19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
elif idade>=21:
    print('MASTER')


