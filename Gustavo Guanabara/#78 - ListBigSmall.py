valores = []
max = 0
min = 0

for contador in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if contador == 0:
        max = min = valores[contador]
    else:
        if valores[contador] > max:
            max = valores[contador]
        if valores[contador] < min:
            min = valores[contador]

print(min)
print(max)
print('Lista')
print(valores)

for indice, valor in enumerate(valores):
    if valor == max:
        print(f'A posição do maior valor no indice é:{indice}')
    if valor == min:
        print(f'A posição do menor valor no indice é:{indice}')

