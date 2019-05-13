numero = [[], []]
valor = 0

for n in range(7):
    valor = (int(input(f'Digite o {n + 1}º valor:')))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print('-=' * 30)
numero[0].sort()
numero[1].sort()
print(f'Os valores pares ditados são:{numero[0]}')
print(f'Os valores impares digitados são:{numero[1]}')
