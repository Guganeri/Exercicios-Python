a = int(input("area A:"))
b = int(input("area B:"))
c = int (input("area C:"))

if a == b and a == c:
    print('Equilátero')
elif ((a == b) or (a == c) ) or ((b == a) or (b == c)):
    print('Isóscaes')
else:
    print('Escalano')

