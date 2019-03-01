nasc = int(input('Digite o ano do seu nascimento'))
ano = 2018
idade = ano-nasc

if idade <= 17:
    print('Você ainda ira se alistar')
    print('Faltam {}anos para você se alistar'.format(18-idade))
elif idade == 18:
    print('Você deve se alistar esse ano')
else:
    print('Você já passou do periodo de alistamento')
    print('Você dveria ter se alistado a {}anos'.format(idade-18))


