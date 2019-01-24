t = int(input("Primeiro termo: "))
r = int(input("Razão: "))
dcm = t + (10-1)*r
for c in range(t,dcm+r,r):
    print('{}'.format(c),end='->')
print(" Acabou")