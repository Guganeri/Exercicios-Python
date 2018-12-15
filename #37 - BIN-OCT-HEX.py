numero = int(input('Digite um numero inteiro:'))
op = int(input('1- Para binario \n2- Para octal \n3- Para hexadecial \n'))

if op == 1:
    print('Em binario o valor é {}'.format(bin(numero)))
elif op == 2:
    print('Em octal o valor ´de {}'.format(oct(numero)))
elif op == 3:
    print('Em hexadecial o valor é de: {}'.format(hex(numero)))
else:
    print('Opção invalida !!')
