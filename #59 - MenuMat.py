n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
op = 0
while op != 5:

    print('[1]somar')
    print('[2]multiplicar')
    print('[3]maior')
    print('[4]novos numeros')
    print('[5]sair do programa')
    op = int(input('Digite uma opção: '))

    if op == 1:
       n1 = n1+n2
       print('O resultado da soma é {}'.format(n1))
    elif op == 2:
        n1 = n1*n2
        print('O resultado da multiplicação é {}'.format(n1))
    elif op == 3:
        if n1>n2:
            print('Primeiro numero {} é maior que o segundo {}!! '.format(n1,n2))
        elif n1<n2:
            print('Segundo numero {} é maior que o primeiro {} !! '.format(n2,n1))
        else:
            print('Iguais {} e {}'.format(n1,n2))
    elif op == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))

print('Obrigado e volte sempre ! kk')
