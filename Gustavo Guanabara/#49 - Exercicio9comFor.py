count = 0
num = int(input('Digite o numero que deseja calcular: '))
for c in range(0,11,):
    print('{}x{}={}'.format(num,count,count*num))
    count += 1
