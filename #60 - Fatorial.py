from math import factorial

numero = int(input('Digite um numero para saber sua fatorial'))
fat = numero

print('Calculando {}! = '.format(fat),end='')
while fat > 0:
    print('{}'.format(fat),end='')
    print(' x ' if fat>1 else ' = ', end='')
    fat -= 1

print('{}'.format(factorial(numero)))
