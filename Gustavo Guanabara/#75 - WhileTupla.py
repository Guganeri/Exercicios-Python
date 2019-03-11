num =  (int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')))
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} veze(s)')
else:
    print('O valor 9 não foi digitado !')
if 3 in num:
    print(f'A posição do primeiro 3 foi a {num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado ! ')
print('Os valores pares digitados foram ', end='')
for numero in num:
    if numero % 2 == 0:
        print(numero, end=' ')
