nota1 = float(input('Digite a sua primeira nota'))
nota2 = float(input('Digite a segunda nota'))

media = (nota1+nota2)/2

if media>=7:
    print('Aprvoado{}'.format(media))
elif media < 4.99:
    print('Reprovado {}'.format(media))
elif media<7 and media >5:
    print('Recuperação {}'.format(media))