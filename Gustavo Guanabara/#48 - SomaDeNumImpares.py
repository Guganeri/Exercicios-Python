sum = 0
count = 0
for c in range(1,501,2):
    if c % 3 == 0:
        sum = sum + c
        count = count + 1
print('Soma = {}\n Numeros = {}'.format(sum,count))
