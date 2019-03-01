valor = float(input('Digite o valor do produto: '))
print('Forma de pagamento')
print('1 - A vista dinheiro')
print('2 - A vista cartão')
print ('3 - Dividir em 2x')
print('4 - Dividir em 3x ou mais')
op =  int(input())

if op == 1:
    valorf  =  valor - valor*10/100
    print(valorf)
elif op == 2:
    valorf = valor - valor*5/100
    print(valorf)
elif op == 3:
    print(valor)
elif op == 4:
    valorf = valor + valor*20/100
    print(valorf)



