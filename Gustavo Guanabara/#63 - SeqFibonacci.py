seq = int(input('Digite a qtd de números mostrados na tela: '))
count = 1
t1 = 0
t2 = 1
count = 3
print('{} -> {}'.format(t1,t2), end='')
while count <= seq:
    t3 = t1 + t2
    print(' -> {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    count += 1
print(' -> FIM')
